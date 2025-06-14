import os
import json
from typing import TypedDict

from archpoint.calibration.manual.exceptions import (
    RoomImageDotsEditorCreatingError,
    InvalidDotId,
    InvalidDotCoordinates,
    InvalidDotFormat,
    InvalidHistoryOperationType,
    DotWithTheSameIdAlreadyExists,
    DotWithCurrentIdNotFound,
    DotsHistoryIsEmpty,
)


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


class RoomImageAnnotation:
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
                if point := self.image_points.pop(operation["new_id"], None):
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
