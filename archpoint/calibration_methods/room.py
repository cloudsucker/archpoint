from __future__ import annotations

import os
import cv2
import numpy as np
from typing import TypedDict

from archpoint.calibration_methods import CalibrationMethodAbstract


class HistoryEntry(TypedDict):
    """Словарь содержащий информацию о конкретной операции с точкой.

    Attributes:
        id (str): Уникальный идентификатор точки.
        method (str): Тип операции "add", "edit", "remove".
        old_point (tuple[float, float] | None): Старые координаты точки на изображении.
        new_point (tuple[float, float] | None): Новые координаты точки на изображении.
    """

    id: str
    method: str
    old_point: tuple[float, float] | None
    new_point: tuple[float, float] | None


class RoomCalibrationMethod(CalibrationMethodAbstract):
    def __init__(self):
        self.images_handler = RoomImagesHandler()

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
        return all(image.is_completed() for image in self.images_handler.images)


class RoomImagesHandler:
    def __init__(self):
        self.images: list[RoomImageDotsEditor] = []
        self.current_image_index = 0

    def initialize_manager(self, image_paths: list[str]) -> None:
        for image_path in image_paths:
            self.images.append(RoomImageDotsEditor(image_path))

    def __self_check(self) -> None:
        if len(self.images) == 0:
            raise RoomImagesManagerSelfCheckError(
                "Менеджер изображений не инициализирован."
            )

    def __is_index_valid(self, index: int) -> bool:
        self.__self_check()
        return index >= 0 and index < len(self.images)

    def get_previous_image(self) -> RoomImageDotsEditor:
        if self.__is_index_valid(self.current_image_index - 1):
            self.current_image_index -= 1
            return self.images[self.current_image_index]

    def get_next_image(self) -> RoomImageDotsEditor:
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

    def is_completed(self) -> bool:
        self.__self_check()
        return all(image.is_completed() for image in self.images)

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
        self.image_points: dict[str, tuple[float, float]] = {}

        # TODO: У нас разве не трёхмерные точки должны быть в points_true_coords ???
        # TODO: ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇
        self.points_true_coords: dict[str, tuple[float, float]] = {}  # ID: [x, y]
        self.history: list[HistoryEntry] = []

    def is_completed(self) -> bool:
        self.__self_check()
        # TODO: Прописать полную реализацию проверки завершенности
        return len(self.image_points) >= 4

    def __self_check(self) -> None:
        if len(self.image_points) != len(self.points_true_coords):
            raise RoomImageDotsEditorSelfCheckError(
                f"Количество точек в image_points ({len(self.image_points)}) и points_true_coords ({len(self.points_true_coords)}) не совпадает."
            )

    def __update_history(
        self,
        id: str,
        method: str,
        old_point: tuple[float, float],
        new_point: tuple[float, float],
    ) -> None:
        self.history.append(
            {"id": id, "method": method, "old_point": old_point, "new_point": new_point}
        )

    def add_point(self, id: str, point: tuple[float, float]) -> None:
        if id in self.image_points.keys():
            raise DotWithTheSameIdAlreadyExists(
                f"Точка с указанным идентификатором {id} уже существует."
            )

        if len(point) != 2:
            raise InvalidDotFormat(
                "Точка должна быть списком с двумя значениями координат."
            )

        self.__update_history(id, "add", None, point)
        self.image_points[id] = point

    def edit_point(self, id: str, point: list[int, int]) -> None:
        if id not in self.image_points.keys():
            raise DotWithCurrentIdNotFound(
                f"Точка с указанным идентификатором {id} не найдена."
            )

        if len(point) != 2:
            raise InvalidDotFormat(
                "Точка должна быть списком с двумя значениями координат."
            )

        self.__update_history(id, "edit", self.image_points[id], point)
        self.image_points[id] = point

    def remove_point(self, id: str) -> None:
        if id not in self.image_points.keys():
            raise DotWithCurrentIdNotFound(
                f"Точка с указанным идентификатором {id} не найдена."
            )
        self.__update_history(id, "remove", self.image_points[id], None)
        self.image_points.pop(id)

    def undo(self) -> None:
        if not self.history:
            raise DotsHistoryIsEmpty("В истории нет операций.")
        operation = self.history.pop()
        if operation["method"] == "add":
            self.image_points.pop(operation["id"])
        elif operation["method"] == "edit":
            self.image_points[operation["id"]] = operation["old_point"]
        elif operation["method"] == "remove":
            self.image_points[operation["id"]] = operation["new_point"]
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

    def get_points_true_coords_dict(self) -> dict[str, tuple[float, float]]:
        return self.points_true_coords

    def get_points_true_coords_list(self) -> list[tuple[float, float]]:
        return list(self.points_true_coords.values())

    def set_points_true_coords(self, points: dict[str, tuple[float, float]]) -> None:
        self.points_true_coords = points


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


class InvalidDotFormat(Exception):
    pass


class RoomImagesManagerSelfCheckError(Exception):
    pass


class RoomImageDotsEditorSelfCheckError(Exception):
    pass


class InvalidHistoryOperationType(Exception):
    pass
