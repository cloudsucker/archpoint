from __future__ import annotations

import os
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

    def initialize(self, image_paths: list[str]) -> None:
        self.images_handler.initialize(image_paths)

    def calibrate(self, image_paths: list) -> dict:
        if not image_paths:
            raise ValueError("Недостаточно изображений для калибровки.")
        if not self.is_completed():
            raise SomeImagesHaveNoDots("Не все изображения были размечены.")

        # camera_parameters = {}

        # initial_imgpoints, initial_objpoints = self.__get_img_and_obj_points(image)

        # if len(initial_imgpoints) == 0 or len(initial_objpoints) == 0:
        #     raise ValueError("Не удалось извлечь точки для калибровки.")

        # image = cv2.imread(image_paths[0])
        # if image is None:
        #     raise ValueError(
        #         f"Ошибка калибровки: Не удалось загрузить изображение: {image_paths[0]}"
        #     )

        # TODO: Дописать логику калибровки для одной камеры.
        pass

    def calibrate_stereo(self, left_image_paths: list, right_image_paths: list) -> dict:
        if not self.is_completed():
            raise SomeImagesHaveNoDots("Не все изображения были размечены.")
        if len(left_image_paths) < 1 or len(right_image_paths) < 1:
            raise ValueError("Недостаточно изображений для калибровки.")

        # TODO: Реализовать логику калибровки для режима двух камер.
        pass

    def __get_img_and_obj_points(self) -> tuple[list, np.ndarray]:
        imgpoints = []
        objpoints = []

        for image in self.images_handler.images:
            imgpoints.append(image.get_points_list())
            objpoints.append(image.get_points_true_coords_list())

        return imgpoints, np.array(objpoints)

    def is_completed(self) -> bool:
        return all(
            image.are_all_image_dots_set() for image in self.images_handler.images
        )


class RoomImagesHandler:
    def __init__(self):
        self.images: list[RoomImageDotsEditor] = []
        self.current_image_index = 0
        self.is_initialized = False

    def initialize(self, image_paths: list[str]) -> None:
        if not image_paths:
            raise NoImagesInDirectoryError(
                "Нет изобрважений для инициализации метода калибровки."
            )
        for image_path in image_paths:
            self.images.append(RoomImageDotsEditor(image_path))
        self.is_initialized = True

    def __self_check(self) -> None:
        if len(self.images) == 0:
            raise RoomImagesManagerSelfCheckError(
                "Менеджер изображений не инициализирован."
            )

    def __is_index_valid(self, index: int) -> bool:
        self.__self_check()
        return index >= 0 and index < len(self.images)

    def get_previous_image(self) -> RoomImageDotsEditor | None:
        if self.__is_index_valid(self.current_image_index - 1):
            self.current_image_index -= 1
            return self.images[self.current_image_index]

    def get_current_image(self) -> RoomImageDotsEditor:
        return self.images[self.current_image_index]

    def get_next_image(self) -> RoomImageDotsEditor | None:
        if self.__is_index_valid(self.current_image_index + 1):
            self.current_image_index += 1
            return self.images[self.current_image_index]

    def get_image_by_image_path(self, image_path: str) -> RoomImageDotsEditor | None:
        for image in self.images:
            if image.image_path == image_path:
                return image

    def get_image_by_index(self, index: int) -> RoomImageDotsEditor | None:
        if self.__is_index_valid(index):
            return self.images[index]

    def are_all_image_dots_set(self) -> bool:
        self.__self_check()
        return all(image.are_all_image_dots_set() for image in self.images)

    def are_all_real_coordinates_completed(self) -> bool:
        self.__self_check()
        return all(image.are_real_coordinates_completed() for image in self.images)

    def clear(self) -> None:
        self.images.clear()
        self.current_image_index = 0


class RoomImageDotsEditor:
    def __init__(self, image_path: str):
        if not os.path.exists(image_path):
            raise RoomImageDotsEditorCreatingError(
                f"Изображение по указанному пути {image_path} не существует."
            )
        self.image_path = image_path
        self.image_name = os.path.basename(image_path).split(".")[0]
        if self.is_dots_file_exist():
            self.load_points_from_file()
        else:
            self.image_points: dict[str, tuple[float, float]] = {}
        self.points_true_coords: dict[str, tuple[float, float, float]] = {}
        self.history: list[HistoryEntry] = []

    def are_all_image_dots_set(self) -> bool:
        return len(self.image_points) >= 4

    def are_real_coordinates_completed(self) -> bool:
        if len(self.image_points) != len(self.points_true_coords):
            return False
        return self.are_all_image_dots_set()

    def __self_check(self) -> None:
        if len(self.image_points) != len(self.points_true_coords):
            raise RoomImageDotsEditorSelfCheckError(
                f"Количество точек в image_points ({len(self.image_points)}) и points_true_coords ({len(self.points_true_coords)}) не совпадает."
            )

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
        self.points_true_coords.clear()
        self.clear_history()

    def get_history(self) -> list[HistoryEntry]:
        return self.history

    def get_points_dict(self) -> dict[str, tuple[float, float]]:
        return self.image_points

    def get_points_list(self) -> list[tuple[float, float]]:
        return list(self.image_points.values())

    def get_points_true_coords_dict(self) -> dict[str, tuple[float, float, float]]:
        return self.points_true_coords

    def get_points_true_coords_list(self) -> list[tuple[float, float, float]]:
        return list(self.points_true_coords.values())

    def set_points_true_coords(
        self, points: dict[str, tuple[float, float, float]]
    ) -> None:
        self.points_true_coords = points

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
