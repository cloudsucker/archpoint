import os
import cv2
import numpy as np

from archpoint.calibration.auto import ChessboardCalibrationMethod
from archpoint.calibration.manual import RoomCalibrationMethod


class CalibrationHandler:
    def __init__(self):
        self.calibration_data = {}
        self.method: ChessboardCalibrationMethod | RoomCalibrationMethod | None = None

        self.calibration_methods = {
            "chessboard": ChessboardCalibrationMethod,
            "room": RoomCalibrationMethod,
        }

        self.image_extensions = (".jpg", ".jpeg", ".png")

    def is_completed(self) -> bool:
        """
        Метод для проверки завершенности калибровки.
        Возвращает True, если калибровка завершена и содержит данные, иначе False.
        """
        if (
            self.method is not None
            and self.calibration_data
            and self.calibration_data.get("stereo_mode", None) is not None
        ):
            # TODO: ADD MORE DATA CHECKING
            return True
        return False

    def clear(self) -> None:
        """
        Метод для корректной очистки данных калибровки.
        Используется для сброса данных калибровки в начальное состояние.
        """
        self.method = None

    def get_calibration_data_as_string(self) -> str:
        calibration_data_str = ""
        for key, value in self.calibration_data.items():
            if isinstance(value, np.ndarray):
                calibration_data_str += (
                    f"{key}:\n{np.array2string(value, separator=', ')}\n\n"
                )
            else:
                calibration_data_str += f"{key}: {value}\n\n"
        return calibration_data_str

    def load_calibration_data(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError("Файл калибровки не найден.")
        if not filepath.endswith(".npz"):
            raise ValueError("Имя файла калибровки должно заканчиваться на '.npz'.")
        self.calibration_data = dict(np.load(filepath))

        print(str(self.calibration_data["calibration_method"].item()))
        print(str(self.calibration_data["stereo_mode"].item()))

        # SETTING ATTRIBUTES
        # TODO: REFACTOR METHODS NAMING
        if (
            str(self.calibration_data["calibration_method"].item())
            == "ChessboardCalibrationMethod"
        ):
            self.set_calibration_method("chessboard")
        elif (
            str(self.calibration_data["calibration_method"].item())
            == "RoomCalibrationMethod"
        ):
            self.set_calibration_method("room")

    def save_calibration_data(self, filepath: str) -> None:
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))

        if not filepath.endswith(".npz"):
            raise ValueError("Имя файла калибровки должно заканчиваться на '.npz'.")

        np.savez(filepath, **self.calibration_data)

        data = dict(np.load(filepath))

        for key in ("L_Imgpoints", "R_Imgpoints"):
            if key in data:
                shape = data[key].shape
                if len(shape) == 4:
                    new_shape = (shape[0], shape[1], shape[3])
                    data[key] = np.resize(data.pop(key), new_shape)

        np.savez(filepath, **data)

    def __get_image_paths_sorted(self, images_dir: str) -> list:
        image_names = sorted(os.listdir(images_dir), key=len)
        image_names = [
            name
            for name in image_names
            if name.lower().endswith(
                tuple(ext.lower() for ext in self.image_extensions)
            )
        ]

        if not image_names:
            raise ValueError("В директории нет допустимых изображений.")

        return [os.path.join(images_dir, name) for name in image_names]

    def set_calibration_method(self, calibration_method: str) -> None:
        """
        Метод для установки метода калибровки.

        Parameters:
            calibration_method (str): Название метода калибровки ('room' или 'chessboard').
        """
        if calibration_method not in self.calibration_methods:
            raise CalibrationMethodDoesNotExist(
                f"Недопустимый метод калибровки: {calibration_method}"
            )
        self.method = self.calibration_methods[calibration_method]()

    def get_calibration_method_name(self) -> str:
        return list(self.calibration_methods.keys())[
            list(self.calibration_methods.values()).index(self.method.__class__)
        ]

    def initialize_room_images_handler(
        self, images_path: str, second_camera_images_path: str | None = None
    ):
        if not isinstance(self.method, RoomCalibrationMethod):
            raise ValueError("Метод калибровки не поддерживает создание точек.")

        if second_camera_images_path:
            first_images = self.__get_image_paths_sorted(images_path)
            second_images = self.__get_image_paths_sorted(second_camera_images_path)
            self.method.initialize(first_images, second_images)
            return
        image_paths = self.__get_image_paths_sorted(images_path)
        self.method.initialize(image_paths)

    def calibrate(self, images_path: str) -> None:
        self.__init_calibration_data(stereo_mode=False)
        image_paths = self.__get_image_paths_sorted(images_path)
        self.calibration_data.update(self.method.calibrate(image_paths))

    def calibrate_stereo(self, left_images_path: str, right_images_path: str) -> None:
        self.__init_calibration_data(stereo_mode=True)
        left_image_paths = self.__get_image_paths_sorted(left_images_path)
        right_image_paths = self.__get_image_paths_sorted(right_images_path)
        self.calibration_data.update(
            self.method.calibrate_stereo(left_image_paths, right_image_paths)
        )

    def __init_calibration_data(self, stereo_mode: bool) -> None:
        self.calibration_data = {
            "stereo_mode": stereo_mode,
            "calibration_method": str(self.method),
        }

    def __fix_image_distortion(self, image_path: str) -> None:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Изображение не найдено: {image_path}")

        if not self.calibration_data:
            raise ValueError("Нет данных калибровки.")

        stereo_mode = self.calibration_data.get("stereo_mode", None)
        if stereo_mode is None:
            raise ValueError("Поле 'stereo_mode' не найдено в данных калибровки.")

        if stereo_mode:
            dist_coeffs = self.calibration_data.get("L_distortion_coeffs", None)
            intrinsic = self.calibration_data.get("L_camera_matrix", None)
            new_camera_matrix = self.calibration_data.get("L_new_camera_matrix", None)
        else:
            dist_coeffs = self.calibration_data.get("distortion_coeffs", None)
            intrinsic = self.calibration_data.get("camera_matrix", None)
            new_camera_matrix = self.calibration_data.get("new_camera_matrix", None)

        if not dist_coeffs:
            raise CalibrationParameterNotFound(
                "Коэффициенты искажений камеры не найдены."
            )
        if not intrinsic:
            raise CalibrationParameterNotFound(
                "Матрица внутренних параметров не найдена."
            )
        if not new_camera_matrix:
            raise CalibrationParameterNotFound(
                "Новая матрица внутренних параметров искажений не найдена."
            )

        image = cv2.imread(image_path, 0)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result = cv2.undistort(
            image,
            intrinsic,
            dist_coeffs,
            None,
            new_camera_matrix,
        )

        return result

    def __fix_images_pair_rectification(
        self, left_image_path: str, right_image_path: str
    ) -> tuple[np.ndarray, np.ndarray]:
        left_image = cv2.imread(left_image_path, 0)
        right_image = cv2.imread(right_image_path, 0)

        if left_image is None or right_image is None:
            raise FileNotFoundError(
                f"Ошибка загрузки изображений: {left_image_path}, {right_image_path}"
            )

        left_image = cv2.cvtColor(left_image, cv2.COLOR_BGR2RGB)
        right_image = cv2.cvtColor(right_image, cv2.COLOR_BGR2RGB)

        left_K = self.calibration_data.get("L_camera_matrix", None)
        right_K = self.calibration_data.get("R_camera_matrix", None)

        if left_K is None or right_K is None:
            raise CalibrationParameterNotFound(
                "Матрица внутренних параметров камеры не найдена."
            )

        left_D = self.calibration_data.get("L_distortion_coeffs", None)
        right_D = self.calibration_data.get("R_distortion_coeffs", None)

        if left_D is None or right_D is None:
            raise CalibrationParameterNotFound(
                "Коэффициенты искажений камеры не найдены."
            )

        image_size = (left_image.shape[1], left_image.shape[0])

        Rk = self.calibration_data.get("transformation_matrix")[:3, :3]
        Tk = self.calibration_data.get("transformation_matrix")[:3, 3:]

        if Rk is None or Tk is None:
            raise CalibrationParameterNotFound(
                "Матрица трансформации не найдена в данных калибровки."
            )

        rect = cv2.stereoRectify(
            left_K, left_D, right_K, right_D, image_size, Rk, Tk, alpha=0
        )
        map1 = cv2.initUndistortRectifyMap(
            left_K, left_D, rect[0], rect[2], image_size, cv2.CV_32FC1
        )
        map2 = cv2.initUndistortRectifyMap(
            right_K, right_D, rect[1], rect[3], image_size, cv2.CV_32FC1
        )

        left_image_rect = cv2.remap(left_image, map1[0], map1[1], cv2.INTER_AREA)
        right_image_rect = cv2.remap(right_image, map2[0], map2[1], cv2.INTER_AREA)

        if left_image_rect is None or right_image_rect is None:
            raise RuntimeError("Ошибка ремаппинга изображений.")

        return left_image_rect, right_image_rect

    def fix_images(self, images_path: str, results_path: str) -> None:
        image_paths = self.__get_image_paths_sorted(images_path)

        if not os.path.exists(images_path):
            raise FileNotFoundError("Папка с изображениями не найдена.")

        os.makedirs(results_path, exist_ok=True)

        for image_path in image_paths:
            fixed_image = self.__fix_image_distortion(image_path)

            image_name = os.path.basename(image_path)
            full_path = os.path.join(results_path, image_name)

            cv2.imwrite(full_path, fixed_image)

    def fix_images_stereo(
        self,
        first_images_path: str,
        second_images_path: str,
        first_results_path: str,
        second_results_path: str,
    ) -> None:
        if not os.path.exists(first_images_path):
            raise FileNotFoundError("Папка с левыми изображениями не найдена.")

        if not os.path.exists(second_images_path):
            raise FileNotFoundError("Папка с правыми изображениями не найдена.")

        left_image_paths = self.__get_image_paths_sorted(first_images_path)
        right_image_paths = self.__get_image_paths_sorted(second_images_path)

        os.makedirs(first_results_path, exist_ok=True)
        os.makedirs(second_results_path, exist_ok=True)

        for left_image_path, right_image_path in zip(
            left_image_paths, right_image_paths
        ):
            left_fixed_image, right_fixed_image = self.__fix_images_pair_rectification(
                left_image_path, right_image_path
            )

            first_image_name = os.path.basename(left_image_path)
            second_image_name = os.path.basename(right_image_path)

            first_full_path = os.path.join(first_results_path, first_image_name)
            second_full_path = os.path.join(second_results_path, second_image_name)

            cv2.imwrite(first_full_path, left_fixed_image)
            cv2.imwrite(second_full_path, right_fixed_image)


class CalibrationParameterNotFound(Exception):
    pass


class CalibrationMethodDoesNotExist(Exception):
    pass
