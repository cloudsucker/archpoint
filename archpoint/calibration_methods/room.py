import cv2
import numpy as np

from archpoint.calibration_methods import CalibrationMethodAbstract


class CalibrationRoomCalibrationMethod(CalibrationMethodAbstract):
    def __init__(self):
        # Словарь путей к изображениям и их точек
        self.images: dict[str, ImageCalibrationDots] = {}

    def __is_all_images_dotted(self) -> bool:
        for key in self.images.keys():
            if not self.images[key].is_completed():
                return False
        return True

    def initialize_dot_creator(self, image_paths: list) -> None:
        for image_path in image_paths:
            self.images[image_path] = ImageCalibrationDots()

    def calibrate(self, image_paths: list) -> dict:
        if not self.__is_all_images_dotted():
            raise SomeImagesHaveNoDots("Не все изображения были размечены.")
        if len(image_paths) < 1:
            raise ValueError("Недостаточно изображений для калибровки.")

        camera_parameters = {}

        for image in self.images:
            initial_imgpoints, initial_objpoints = self.__get_img_and_obj_points(image)

        if len(initial_imgpoints) == 0 or len(initial_objpoints) == 0:
            raise ValueError("Не удалось извлечь точки для калибровки.")

        image = cv2.imread(image_paths[0])
        if image is None:
            raise ValueError(
                f"Ошибка калибровки: Не удалось загрузить изображение: {image_paths[0]}"
            )

        # TODO: Дописать логику калибровки для одной камеры.
        pass

    def calibrate_stereo(self, left_image_paths: list, right_image_paths: list) -> dict:
        if not self.__is_all_images_dotted():
            raise SomeImagesHaveNoDots("Не все изображения были размечены.")
        if len(left_image_paths) < 1 or len(right_image_paths) < 1:
            raise ValueError("Недостаточно изображений для калибровки.")

        # TODO: Реализовать логику калибровки для режима двух камер.
        pass

    def __get_img_and_obj_points(self, image: str) -> tuple[list, np.ndarray]:
        imgpoints = []
        objpoints = []

        for image_path in self.images.keys():
            imgpoints.append(self.images[image_path].get_points_list())
            objpoints.append(self.images[image_path].get_points_true_coords_list())

        return imgpoints, np.array(objpoints)


class ImageCalibrationDots:
    def __init__(self):
        # Расставленные пользователем точки и их координаты на изображении
        self.image_points: dict[str, list[float, float]] = {}

        # Словарь сопоствления уникальных идентификаторов пользовательских точек
        # и их внутренних координат в системе калибровки
        self.points_true_coords: dict[str, list[float, float]] = {}

        # История операций (список словарей {id, method, old_point, new_point]}).
        self.history: list[dict[str, str, list[float, float], list[float, float]]] = []

    def is_completed(self) -> bool:

        # TODO: Прописать полную реализацию проверки завершенности

        if len(self.image_points) < 4:
            return False
        return True

    def __update_history(
        self,
        id: str,
        method: str,
        old_point: list[float, float],
        new_point: list[float, float],
    ) -> None:
        self.history.append(
            {"id": id, "method": method, "old_point": old_point, "new_point": new_point}
        )

    def add_point(self, id: str, point: list[float, float]) -> None:
        if len(point) != 2:
            raise InvalidDotsFormat(
                "Точка должна быть списком с двумя значениями координат."
            )

        if id in self.image_points.keys():
            raise DotWithTheSameIdAlreadyExists(
                f"Точка с указанным идентификатором {id} уже существует."
            )

        self.__update_history(id, "add", None, point)
        self.image_points[id] = point

    def edit_point(self, id: str, point: list[int, int]) -> None:
        if id not in self.image_points.keys():
            raise DotWithCurentIdNotFound(
                f"Точка с указанным идентификатором {id} не найдена."
            )

        if len(point) != 2:
            raise InvalidDotsFormat(
                "Точка должна быть списком с двумя значениями координат."
            )

        self.__update_history(id, "edit", self.image_points[id], point)
        self.image_points[id] = point

    def remove_point(self, id: str) -> None:
        if id not in self.image_points.keys():
            raise DotWithCurentIdNotFound(
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

    def clear_history(self) -> None:
        self.history = []

    def get_history(
        self,
    ) -> list[dict[str, str, list[float, float], list[float, float]]]:
        return self.history

    def get_points_dict(self) -> dict[str, list[float, float]]:
        return self.image_points

    def get_points_list(self) -> list[list[float, float]]:
        return list(self.image_points.values())

    def get_points_true_coords_dict(self) -> dict[str, list[float, float]]:
        return self.points_true_coords

    def get_points_true_coords_list(self) -> list[list[float, float]]:
        return list(self.points_true_coords.values())

    def set_points_true_coords(self, points: dict[str, list[float, float]]) -> None:
        self.points_true_coords = points


# DOTS OPERATIONS HISTORY EXCEPTIONS
class DotsHistoryIsEmpty(Exception):
    pass


# DOTS EXCEPTIONS
class DotWithTheSameIdAlreadyExists(Exception):
    pass


class DotWithCurentIdNotFound(Exception):
    pass


class SomeImagesHaveNoDots(Exception):
    pass


class InvalidDotsFormat(Exception):
    pass
