import os
import numpy as np

from typing import Callable

from archpoint.calibration.manual.room_image_annotation import RoomImageAnnotation
from archpoint.calibration.manual.exceptions import (
    NoImagesInDirectoryError,
    RoomImagesManagerSelfCheckError,
    DotWithCurrentIdNotFound,
    DotsRealCoordinatesLoadingFromFileError,
)


class RoomImageCollection:
    """Класс для работы с набором изображений для калибровки методом комнаты.

    Attributes:
        images (list[RoomImageAnnotation]): Список изображений для калибровки.
        points (dict[str, dict[str, tuple[float, float]]]): Словарь точек для каждого изображения.
        points_true_coords (dict[str, tuple[float, float, float]]): Словарь реальных (настоящих) точек для каждого изображения.
        unique_ids (set[str]): Уникальные идентификаторы точек.
        current_image_index (int): Индекс текущего изображения.
        is_initialized (bool): Флаг инициализации.
        stereo_mode (bool): Флаг стерео-режима.
        real_coords_file_extensions (tuple[str]): Допустимые расширения файлов с реальными координатами точек.
    """

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
        """
        Метод для инициализации менеджера изображений.

        Parameters:
            image_paths (list[str]): Список путей к изображениям.
            second_image_paths (list[str] | None): Список путей к вторым изображениям (для стерео-режима).
        """
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
        """Метод для самодиагностики менеджера изображений."""
        if len(self.images) == 0:
            raise RoomImagesManagerSelfCheckError(
                "Менеджер изображений не инициализирован."
            )

    def __self_sync(self) -> None:
        """Метод для синхронизации менеджера изображений."""
        self.__collect_all_images_points()
        self.__collect_all_unique_points_ids()

    def __collect_all_images_points(self) -> None:
        """Метод для сбора всех точек изображений."""
        for image in self.images:
            if image.image_path not in self.points:
                self.points[image.image_path] = {}
            self.points[image.image_path].update(image.image_points)

    def __collect_all_unique_points_ids(self) -> None:
        """Метод для сбора всех уникальных идентификаторов точек."""
        self.unique_ids = set()
        for image in self.images:
            self.unique_ids.update(image.image_points.keys())

    def __validate_point_real_coords(
        self, real_coords: tuple[float, float, float]
    ) -> None:
        """Метод для валидации реальных координат точек.

        Parameters:
            real_coords (tuple[float, float, float]): Реальные координаты точки.
        """
        if not real_coords:
            raise ValueError("Точка не имеет координат.")

        if not isinstance(real_coords, tuple) or len(real_coords) != 3:
            raise ValueError("Неккоректный формат координат.")

    def get_previous_image(self) -> RoomImageAnnotation | None:
        """
        Метод для получения предыдущего изображения.

        Returns:
            RoomImageAnnotation | None: Предыдущее изображение.
        """
        if self.__is_index_valid(self.current_image_index - 1):
            self.current_image_index -= 1
            return self.images[self.current_image_index]

    def get_current_image(self) -> RoomImageAnnotation:
        """
        Метод для получения текущего изображения.

        Returns:
            RoomImageAnnotation: Текущее изображение.
        """
        self.__self_sync()
        return self.images[self.current_image_index]

    def get_next_image(self) -> RoomImageAnnotation | None:
        """
        Метод для получения следующего изображения.

        Returns:
            RoomImageAnnotation | None: Следующее изображение.
        """
        if self.__is_index_valid(self.current_image_index + 1):
            self.current_image_index += 1
            return self.images[self.current_image_index]

    def get_image_by_image_path(self, image_path: str) -> RoomImageAnnotation | None:
        """
        Метод для получения изображения по пути к изображению.

        Parameters:
            image_path (str): Путь к изображению.

        Returns:
            RoomImageAnnotation | None: Изображение.
        """
        for image in self.images:
            if image.image_path == image_path:
                return image

    def __is_index_valid(self, index: int) -> bool:
        """
        Метод для проверки валидности индекса.

        Parameters:
            index (int): Индекс.

        Returns:
            bool: Валидность индекса.
        """
        self.__self_check()
        return index >= 0 and index < len(self.images)

    def get_image_by_index(self, index: int) -> RoomImageAnnotation | None:
        """
        Метод для получения изображения по индексу.

        Parameters:
            index (int): Индекс.

        Returns:
            RoomImageAnnotation | None: Изображение.
        """
        if self.__is_index_valid(index):
            return self.images[index]

    def are_all_image_dots_set(self) -> bool:
        """
        Метод для проверки, что все точки изображений установлены.

        Returns:
            bool: Валидность индекса.
        """
        self.__self_check()
        self.__self_sync()
        return all(image.are_all_image_dots_set() for image in self.images)

    def set_dot_real_coordinates(
        self, point_id: str, coords: tuple[float, float, float]
    ) -> None:
        """
        Метод для установки реальных координат точки.

        Parameters:
            point_id (str): Идентификатор точки.
            coords (tuple[float, float, float]): Реальные координаты точки.
        """
        self.__self_check()
        self.__self_sync()
        self.__validate_point_real_coords(coords)

        if point_id not in self.unique_ids:
            raise DotWithCurrentIdNotFound(f"Точка с id {point_id} не существует.")

        self.points_true_coords[point_id] = coords

    def get_dot_real_coordinates(self, point_id: str) -> tuple[float, float, float]:
        """
        Метод для получения реальных координат точки.

        Parameters:
            point_id (str): Идентификатор точки.

        Returns:
            tuple[float, float, float]: Реальные координаты точки.
        """
        self.__self_check()
        self.__self_sync()
        return self.points_true_coords.get(point_id)

    def are_all_real_coordinates_completed(self) -> bool:
        """
        Метод для проверки, что все реальные координаты точек установлены.

        Returns:
            bool: Валидность индекса.
        """
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
        """
        Метод для загрузки реальных координат точек из файла.

        Parameters:
            file_path (str): Путь к файлу внутренних координат точек.
        """
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
        """
        Метод для загрузки реальных координат точек из файла.

        Parameters:
            file_path (str): Путь к файлу внутренних координат точек.
        """
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

    def __detect_parser(self, lines: list[str]) -> Callable[[str], list[str] | None]:
        """
        Метод для определения структуры файла.

        Parameters:
            lines (list[str]): Список строк.

        Returns:
            Callable[[str], list[str] | None]: Функция для парсинга строки.
        """
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
        """
        Метод для парсинга строки.

        Parameters:
            line (str): Строка для парсинга.
            sep (str): Разделитель.

        Returns:
            list[str]: Список элементов.
        """
        parts = line.strip().split(sep)
        if len(parts) == 4:
            return parts
        raise ValueError("Неверное количество элементов.")

    def __try_parse_line_auto(self, line: str) -> list[str]:
        """
        Метод для автоматического парсинга строки.

        Parameters:
            line (str): Строка для парсинга.

        Returns:
            list[str]: Список элементов.
        """
        parts = line.strip().split()
        if len(parts) == 4:
            return parts
        raise ValueError("Неверное количество элементов.")

    def get_img_and_obj_points(self, image_paths: list[str]) -> tuple[list, np.ndarray]:
        """
        Метод для получения точек на изображениях и массива настоящих координат точек.

        Parameters:
            image_paths (list[str]): Список путей к изображениям.

        Returns:
            tuple[list, np.ndarray]: Кортеж из списка точек на изображениях и массива настоящих координат точек.
        """
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
        """Метод для полного сброса объекта класса."""
        self.images.clear()
        self.points.clear()
        self.points_true_coords.clear()
        self.unique_ids.clear()
        self.current_image_index = 0
        self.stereo_mode = False
        self.is_initialized = False
