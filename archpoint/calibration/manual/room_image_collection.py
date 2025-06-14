import os
import numpy as np

from archpoint.calibration.manual.room_image_annotation import RoomImageAnnotation
from archpoint.calibration.manual.exceptions import (
    NoImagesInDirectoryError,
    RoomImagesManagerSelfCheckError,
    DotWithCurrentIdNotFound,
    DotsRealCoordinatesLoadingFromFileError,
)


class RoomImageCollection:
    def __init__(self):
        self.images: list[RoomImageAnnotation] = []
        self.points: dict[str, dict[str, tuple[float, float]]] = {}
        self.points_true_coords: dict[str, tuple[float, float, float]] = {}
        self.unique_ids: set[str] = set()
        self.current_image_index = 0
        self.is_initialized = False
        self.stereo_mode = False
        self.real_coords_file_extensions = (".txt", ".csv")

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
            self.images.append(RoomImageAnnotation(image_path))

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

    def get_previous_image(self) -> RoomImageAnnotation | None:
        if self.__is_index_valid(self.current_image_index - 1):
            self.current_image_index -= 1
            return self.images[self.current_image_index]

    def get_current_image(self) -> RoomImageAnnotation:
        self.__self_sync()
        return self.images[self.current_image_index]

    def get_next_image(self) -> RoomImageAnnotation | None:
        if self.__is_index_valid(self.current_image_index + 1):
            self.current_image_index += 1
            return self.images[self.current_image_index]

    def get_image_by_image_path(self, image_path: str) -> RoomImageAnnotation | None:
        for image in self.images:
            if image.image_path == image_path:
                return image

    def __is_index_valid(self, index: int) -> bool:
        self.__self_check()
        return index >= 0 and index < len(self.images)

    def get_image_by_index(self, index: int) -> RoomImageAnnotation | None:
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
        if self.points_true_coords.keys() != self.unique_ids:
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
            if point_id not in self.unique_ids:
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
