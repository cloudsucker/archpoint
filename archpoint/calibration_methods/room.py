from __future__ import annotations

import os
import cv2
import json
import numpy as np
from typing import TypedDict

from archpoint.calibration_methods import CalibrationMethodAbstract


class HistoryEntry(TypedDict):
    """Словарь содержащий информацию о конкретной операции с точкой.

    Attributes:
        id (str): Уникальный идентификатор точки.
        method (str): Тип операции "add", "edit", "remove", "rename".
        old_id (str | None): Старый ID точки (для rename).
        new_id (str | None): Новый ID точки (для rename).
        old_point (tuple[float, float] | None): Старые координаты точки на изображении (для edit).
        new_point (tuple[float, float] | None): Новые координаты точки на изображении (для edit).
    """

    id: str
    method: str
    old_id: str | None
    new_id: str | None
    old_point: tuple[float, float] | None
    new_point: tuple[float, float] | None


class RoomCalibrationMethod(CalibrationMethodAbstract):
    def __init__(self):
        self.images_handler = RoomImagesHandler()

    def __eq__(self, value):
        return isinstance(value, str) and value == "room"

    def initialize(
        self, image_paths: list[str], second_image_paths: list[str] | None = None
    ) -> None:
        self.images_handler.initialize(image_paths, second_image_paths)

    def calibrate(self, image_paths: list) -> dict:
        if not image_paths:
            raise ValueError("Недостаточно изображений для калибровки.")
        if not self.is_completed():
            raise SomeImagesHaveNoDots("Не все изображения были размечены.")

        initial_imgpoints, initial_objpoints = self.__get_img_and_obj_points(
            image_paths
        )

        if len(initial_imgpoints) == 0 or len(initial_objpoints) == 0:
            raise ValueError("Не удалось извлечь точки для калибровки.")

        image = cv2.imread(image_paths[0])
        if image is None:
            raise ValueError(
                f"Ошибка калибровки: Не удалось загрузить изображение: {image_paths[0]}"
            )

        image_height, image_width = image.shape[:2]
        img_size = (image_width, image_height)

        final_objpoints = [initial_objpoints[0]] * len(image_paths)

        initial_camera_matrix = cv2.initCameraMatrix2D(
            objectPoints=final_objpoints,
            imagePoints=initial_imgpoints,
            imageSize=img_size,
            aspectRatio=1.0,
        )

        flags = cv2.CALIB_USE_INTRINSIC_GUESS

        (
            retval,
            camera_matrix,
            distortion_coeffs,
            rotation_vectors,
            translation_vectors,
        ) = cv2.calibrateCamera(
            objectPoints=final_objpoints,
            imagePoints=initial_imgpoints,
            imageSize=img_size,
            cameraMatrix=initial_camera_matrix,
            distCoeffs=None,
            flags=flags,
        )
        if not retval:
            raise RuntimeError("Калибровка камеры не удалась.")

        rotation_matrices = []
        transformation_matrices = []
        for rvec, tvec in zip(rotation_vectors, translation_vectors):
            R, _ = cv2.Rodrigues(rvec)
            rotation_matrices.append(R)
            RT = np.vstack((np.hstack((R, tvec)), [0, 0, 0, 1]))
            transformation_matrices.append(RT)

        new_matrix, roi = cv2.getOptimalNewCameraMatrix(
            camera_matrix, distortion_coeffs, img_size, 1, img_size
        )
        if new_matrix is None or roi is None:
            raise RuntimeError("Ошибка получения оптимальной новой матрицы камеры.")

        if np.sum(roi) == 0:
            roi = (0, 0, image_width - 1, image_height - 1)

        return {
            "object_points": initial_objpoints,
            "camera_matrix": camera_matrix,
            "distortion_coeffs": distortion_coeffs,
            "roi": roi,
            "new_camera_matrix": new_matrix,
            "rotation_vectors": rotation_vectors,
            "rotation_matrices": rotation_matrices,
            "extrinsic_parameters": transformation_matrices,
            "translation_vectors": translation_vectors,
        }

    def calibrate_stereo(
        self, left_image_paths: list[str], right_image_paths: list[str]
    ) -> dict:
        if not self.is_completed():
            raise SomeImagesHaveNoDots("Не все изображения были размечены.")
        if len(left_image_paths) != len(right_image_paths):
            raise ValueError("Количество изображений слева и справа должно совпадать.")
        if len(left_image_paths) < 1:
            raise ValueError("Недостаточно изображений для стереокалибровки.")

        left_imgpoints, left_objpoints = self.images_handler.get_img_and_obj_points(
            left_image_paths
        )
        right_imgpoints, right_objpoints = self.images_handler.get_img_and_obj_points(
            right_image_paths
        )

        if len(left_imgpoints) == 0 or len(right_imgpoints) == 0:
            raise ValueError("Не удалось извлечь точки для калибровки.")

        left_image = cv2.imread(left_image_paths[0])
        right_image = cv2.imread(right_image_paths[0])
        if left_image is None or right_image is None:
            raise ValueError("Не удалось загрузить одно из изображений.")

        img_size_left = left_image.shape[1], left_image.shape[0]
        img_size_right = right_image.shape[1], right_image.shape[0]

        if img_size_left != img_size_right:
            raise ValueError(
                "Изображения левого и правого каналов должны иметь одинаковый размер."
            )

        flags = cv2.CALIB_USE_INTRINSIC_GUESS

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-6)

        # Калибровка каждой камеры отдельно
        mtx_left_init = cv2.initCameraMatrix2D(
            objectPoints=left_objpoints,
            imagePoints=left_imgpoints,
            imageSize=img_size_left,
            aspectRatio=1.0,
        )

        ret_left, mtx_left, dist_left, rvecs_left, tvecs_left = cv2.calibrateCamera(
            left_objpoints,
            left_imgpoints,
            img_size_left,
            cameraMatrix=mtx_left_init,
            distCoeffs=None,
            flags=cv2.CALIB_USE_INTRINSIC_GUESS,
        )

        mtx_right_init = cv2.initCameraMatrix2D(
            objectPoints=right_objpoints,
            imagePoints=right_imgpoints,
            imageSize=img_size_right,
            aspectRatio=1.0,
        )

        ret_right, mtx_right, dist_right, rvecs_right, tvecs_right = (
            cv2.calibrateCamera(
                right_objpoints,
                right_imgpoints,
                img_size_right,
                cameraMatrix=mtx_right_init,
                distCoeffs=None,
                flags=cv2.CALIB_USE_INTRINSIC_GUESS,
            )
        )

        if not (ret_left and ret_right):
            raise RuntimeError("Не удалось выполнить калибровку отдельных камер.")

        # Стереокалибровка
        ret_stereo, mtx_left, dist_left, mtx_right, dist_right, R, T, E, F = (
            cv2.stereoCalibrate(
                left_objpoints,
                left_imgpoints,
                right_imgpoints,
                mtx_left,
                dist_left,
                mtx_right,
                dist_right,
                img_size_left,
                criteria=criteria,
                flags=cv2.CALIB_USE_INTRINSIC_GUESS,
            )
        )

        if not ret_stereo:
            raise RuntimeError("Стереокалибровка не удалась.")

        # Получение карт смещения (rectification maps)
        R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(
            mtx_left,
            dist_left,
            mtx_right,
            dist_right,
            img_size_left,
            R,
            T,
            flags=0,
            alpha=0,
        )

        stereo_params = {
            "left_camera_matrix": mtx_left,
            "left_distortion_coeffs": dist_left,
            "right_camera_matrix": mtx_right,
            "right_distortion_coeffs": dist_right,
            "rotation_between_cameras": R,
            "translation_between_cameras": T,
            "essential_matrix": E,
            "fundamental_matrix": F,
            "rectification_transform_left": R1,
            "rectification_transform_right": R2,
            "projection_matrix_left": P1,
            "projection_matrix_right": P2,
            "disparity_to_depth_map": Q,
            "roi_left": roi1,
            "roi_right": roi2,
        }

        return stereo_params

    def __get_img_and_obj_points(
        self, image_paths: list[str]
    ) -> tuple[list, np.ndarray]:
        imgpoints = []
        objpoints = []
        imgpoints, objpoints = self.images_handler.get_img_and_obj_points(image_paths)
        return imgpoints, objpoints

    def is_completed(self) -> bool:
        return (
            self.images_handler.are_all_image_dots_set()
            and self.images_handler.are_all_real_coordinates_completed()
        )


class RoomImagesHandler:
    def __init__(self):
        self.images: list[RoomImageDotsEditor] = []
        self.points: dict[str, dict[str, tuple[float, float]]] = {}
        self.points_true_coords: dict[str, tuple[float, float, float]] = {}
        self.unique_ids: set[str] = set()
        self.current_image_index = 0
        self.is_initialized = False
        self.stereo_mode = False
        self.real_coords_file_extensions = (".txt", ".TXT", ".csv", ".CSV")

    def initialize(
        self, image_paths: list[str], second_image_paths: list[str] | None = None
    ) -> None:
        if not image_paths:
            raise NoImagesInDirectoryError(
                "Нет изобрважений для инициализации метода калибровки."
            )

        all_image_paths = image_paths

        if second_image_paths:
            self.stereo_mode = True
            all_image_paths += second_image_paths

        for image_path in all_image_paths:
            self.images.append(RoomImageDotsEditor(image_path))

        self.__self_sync()
        self.is_initialized = True

    def __self_check(self) -> None:
        if len(self.images) == 0:
            raise RoomImagesManagerSelfCheckError(
                "Менеджер изображений не инициализирован."
            )

    def __self_sync(self) -> None:
        self.__collect_all_images_points()
        self.__collect_all_unique_points_ids()

    def __collect_all_images_points(self) -> None:
        for image in self.images:
            if image.image_path not in self.points:
                self.points[image.image_path] = {}
            self.points[image.image_path].update(image.image_points)

    def __collect_all_unique_points_ids(self) -> None:
        self.unique_ids = set()
        for image in self.images:
            self.unique_ids.update(image.image_points.keys())

    def __validate_point_real_coords(
        self, real_coords: tuple[float, float, float]
    ) -> None:
        if not real_coords:
            raise ValueError("Точка не имеет координат.")

        if not isinstance(real_coords, tuple) or len(real_coords) != 3:
            raise ValueError("Неккоректный формат координат.")

    def get_previous_image(self) -> RoomImageDotsEditor | None:
        if self.__is_index_valid(self.current_image_index - 1):
            self.current_image_index -= 1
            return self.images[self.current_image_index]

    def get_current_image(self) -> RoomImageDotsEditor:
        self.__self_sync()
        return self.images[self.current_image_index]

    def get_next_image(self) -> RoomImageDotsEditor | None:
        if self.__is_index_valid(self.current_image_index + 1):
            self.current_image_index += 1
            return self.images[self.current_image_index]

    def get_image_by_image_path(self, image_path: str) -> RoomImageDotsEditor | None:
        for image in self.images:
            if image.image_path == image_path:
                return image

    def __is_index_valid(self, index: int) -> bool:
        self.__self_check()
        return index >= 0 and index < len(self.images)

    def get_image_by_index(self, index: int) -> RoomImageDotsEditor | None:
        if self.__is_index_valid(index):
            return self.images[index]

    def are_all_image_dots_set(self) -> bool:
        self.__self_check()
        self.__self_sync()
        return all(image.are_all_image_dots_set() for image in self.images)

    def set_dot_real_coordinates(
        self, point_id: str, coords: tuple[float, float, float]
    ) -> None:
        self.__self_check()
        self.__self_sync()
        self.__validate_point_real_coords(coords)

        if point_id not in self.unique_ids:
            raise DotWithCurrentIdNotFound(f"Точка с id {point_id} не существует.")

        self.points_true_coords[point_id] = coords

    def get_dot_real_coordinates(self, point_id: str) -> tuple[float, float, float]:
        self.__self_check()
        self.__self_sync()
        return self.points_true_coords.get(point_id)

    def are_all_real_coordinates_completed(self) -> bool:
        self.__self_check()
        if not self.points_true_coords:
            return False
        if not self.points_true_coords.keys() == self.unique_ids:
            return False
        return all(
            isinstance(coords, tuple) and len(coords) == 3
            for coords in self.points_true_coords.values()
        )

    def load_dots_real_coords_from_file(self, file_path: str) -> None:
        if not file_path:
            raise DotsRealCoordinatesLoadingFromFileError(
                "Путь к файлу внутренних координат точек не указан."
            )

        if not os.path.exists(file_path):
            raise DotsRealCoordinatesLoadingFromFileError(
                "Указанный файл внутренних координат точек не существует."
            )

        try:
            self.__load_dots_real_coords(file_path)
        except Exception as e:
            raise DotsRealCoordinatesLoadingFromFileError(
                f"Ошибка загрузки координат: {e}"
            ) from e

    def __load_dots_real_coords(self, file_path: str) -> None:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        parser = self.__detect_parser(lines)
        if not parser:
            raise DotsRealCoordinatesLoadingFromFileError(
                "Не удалось определить структуру файла. Требуется 4 элемента на строку."
            )

        for line in lines:
            parsed = parser(line)
            if parsed is None:
                raise DotsRealCoordinatesLoadingFromFileError(
                    f"Строка не соответствует ожидаемой структуре: {line.strip()}"
                )
            point_id, x, y, z = parsed
            if not point_id in self.unique_ids:
                # TODO: ADD THIS THING INTO LOGS OR USER NOTIFICATION
                continue
            self.set_dot_real_coordinates(point_id, (float(x), float(y), float(z)))

    def __detect_parser(self, lines: list[str]):
        separators = [",", ";", "\t", "|"]
        for sep in separators:
            try:
                if all(len(self.__try_parse_line(line, sep)) == 4 for line in lines):
                    return lambda line: self.__try_parse_line(line, sep)
            except Exception:
                continue

        try:
            if all(len(self.__try_parse_line_auto(line)) == 4 for line in lines):
                return self.__try_parse_line_auto
        except Exception:
            pass

        return None

    def __try_parse_line(self, line: str, sep: str) -> list[str]:
        parts = line.strip().split(sep)
        if len(parts) == 4:
            return parts
        raise ValueError("Неверное количество элементов.")

    def __try_parse_line_auto(self, line: str) -> list[str]:
        parts = line.strip().split()
        if len(parts) == 4:
            return parts
        raise ValueError("Неверное количество элементов.")

    def get_img_and_obj_points(self, image_paths: list[str]) -> tuple[list, np.ndarray]:
        processing_images = self.images

        if self.stereo_mode:
            processing_images = [
                self.get_image_by_image_path(image_path) for image_path in image_paths
            ]

        imgpoints = []
        for image in processing_images:
            pts = np.array(image.get_points_list(), dtype=np.float32)
            if pts.ndim == 2 and pts.shape[1] == 2:
                pts = pts.reshape(-1, 1, 2)
            imgpoints.append(pts)

        obj_single = np.array(list(self.points_true_coords.values()), dtype=np.float32)
        if obj_single.ndim == 2 and obj_single.shape[1] == 2:
            obj_single = obj_single.reshape(-1, 1, 2)

        objpoints = [obj_single for _ in processing_images]
        return imgpoints, objpoints

    def clear(self) -> None:
        self.images.clear()
        self.current_image_index = 0


class RoomImageDotsEditor:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image_name = os.path.basename(image_path).split(".")[0]
        self.image_points: dict[str, tuple[float, float]] = {}
        self.history: list[HistoryEntry] = []
        self.__self_preprocess()

    def are_all_image_dots_set(self) -> bool:
        return len(self.image_points) >= 4

    def __self_check(self) -> None:
        if not os.path.exists(self.image_path):
            raise RoomImageDotsEditorCreatingError(
                f"Изображение по указанному пути {self.image_path} не существует."
            )

    def __self_preprocess(self) -> None:
        self.__self_check()
        if self.is_dots_file_exist():
            self.load_points_from_file()

    def __update_history(
        self,
        id: str,
        method: str,
        old_point: tuple[float, float] | None = None,
        new_point: tuple[float, float] | None = None,
        old_id: str | None = None,
        new_id: str | None = None,
    ) -> None:
        self.history.append(
            {
                "id": id,
                "method": method,
                "old_point": old_point,
                "new_point": new_point,
                "old_id": old_id,
                "new_id": new_id,
            }
        )
        if self.image_points:
            self.save_points_to_file()
        elif self.is_dots_file_exist():
            self.delete_dots_file()

    def __validate_dot(self, id: str, point: tuple[float, float]) -> None:
        if not id:
            raise InvalidDotId("Не указан идентификатор точки.")
        if len(point) != 2:
            raise InvalidDotFormat(
                "Точка должна быть списком с двумя значениями координат."
            )
        if point[0] < 0 or point[1] < 0:
            raise InvalidDotCoordinates(
                "Координаты точки не могут быть отрицательными."
            )

    def __validate_id(self, id: str) -> None:
        if not id or not id.strip():
            raise InvalidDotId("Идентификатор точки не может быть пустым.")

    def add_point(self, id: str, point: tuple[float, float]) -> None:
        self.__validate_dot(id, point)
        if id in self.image_points.keys():
            raise DotWithTheSameIdAlreadyExists(
                f"Точка с указанным идентификатором {id} уже существует."
            )
        self.image_points[id] = point
        self.__update_history(id, "add", None, point)

    def edit_point(self, id: str, point: tuple[float, float]) -> None:
        self.__validate_dot(id, point)
        if id not in self.image_points.keys():
            raise DotWithCurrentIdNotFound(
                f"Точка с указанным идентификатором {id} не найдена."
            )
        previous_point = self.image_points[id]
        self.image_points[id] = point
        self.__update_history(id, "edit", previous_point, point)

    def edit_point_id(self, old_id: str, new_id: str) -> None:
        self.__validate_id(old_id)
        self.__validate_id(new_id)

        if old_id not in self.image_points.keys():
            raise DotWithCurrentIdNotFound(
                f"Точка с указанным идентификатором {old_id} не найдена."
            )

        if new_id in self.image_points.keys():
            raise DotWithTheSameIdAlreadyExists(
                f"Точка с указанным идентификатором {new_id} уже существует."
            )

        self.image_points[new_id] = self.image_points.pop(old_id)
        self.__update_history(old_id, "rename", old_id=old_id, new_id=new_id)

    def remove_point(self, id: str) -> None:
        if id not in self.image_points.keys():
            raise DotWithCurrentIdNotFound(
                f"Точка с указанным идентификатором {id} не найдена."
            )
        removed_point = self.image_points[id]
        self.image_points.pop(id)
        self.__update_history(id, "remove", removed_point, None)

    def undo(self) -> None:
        if not self.history:
            raise DotsHistoryIsEmpty("В истории нет операций.")
        operation = self.history.pop()
        if operation["method"] == "add":
            self.image_points.pop(operation["id"], None)
        elif operation["method"] == "edit":
            if operation["old_point"] is not None:
                self.image_points[operation["id"]] = operation["old_point"]
        elif operation["method"] == "remove":
            if operation["old_point"] is not None:
                self.image_points[operation["id"]] = operation["old_point"]
        elif operation["method"] == "rename":
            if operation["old_id"] and operation["new_id"]:
                point = self.image_points.pop(operation["new_id"], None)
                if point:
                    self.image_points[operation["old_id"]] = point
        else:
            raise InvalidHistoryOperationType(
                f"Недопустимый тип операции {operation['method']} в истории."
            )

    def clear_history(self) -> None:
        self.history.clear()

    def clear(self) -> None:
        self.image_points.clear()
        self.clear_history()

    def get_history(self) -> list[HistoryEntry]:
        return self.history

    def get_points_dict(self) -> dict[str, tuple[float, float]]:
        return self.image_points

    def get_points_list(self) -> list[tuple[float, float]]:
        return list(self.image_points.values())

    def save_points_to_file(self) -> None:
        if self.image_points:
            filename = f"{os.path.basename(self.image_path).split(".")[0]}.json"
            filepath = os.path.join(os.path.dirname(self.image_path), filename)
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(self.image_points, file)

    def is_dots_file_exist(self) -> bool:
        filename = f"{os.path.basename(self.image_path).split('.')[0]}.json"
        filepath = os.path.join(os.path.dirname(self.image_path), filename)
        return os.path.exists(filepath)

    def load_points_from_file(self) -> None:
        filename = f"{os.path.basename(self.image_path).split('.')[0]}.json"
        filepath = os.path.join(os.path.dirname(self.image_path), filename)
        if not os.path.exists(filepath):
            return
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.image_points = {k: tuple(v) for k, v in data.items()}

    def delete_dots_file(self) -> None:
        filename = f"{os.path.basename(self.image_path).split('.')[0]}.json"
        filepath = os.path.join(os.path.dirname(self.image_path), filename)
        if os.path.exists(filepath):
            os.remove(filepath)


class DotsHistoryIsEmpty(Exception):
    pass


class RoomImageDotsEditorCreatingError(Exception):
    pass


class DotWithTheSameIdAlreadyExists(Exception):
    pass


class DotWithCurrentIdNotFound(Exception):
    pass


class SomeImagesHaveNoDots(Exception):
    pass


class InvalidDotId(Exception):
    pass


class InvalidDotFormat(Exception):
    pass


class InvalidDotCoordinates(Exception):
    pass


class RoomImagesManagerSelfCheckError(Exception):
    pass


class RoomImageDotsEditorSelfCheckError(Exception):
    pass


class NoImagesInDirectoryError(Exception):
    pass


class InvalidHistoryOperationType(Exception):
    pass


class DotsRealCoordinatesLoadingFromFileError(Exception):
    pass
