import os
import cv2
import numpy as np

from abc import ABC, abstractmethod


class CalibrationHandler:
    def __init__(self):
        self.calibration_data = {}
        self.calibration_method: CalibrationMethod = ChessboardCalibrationMethod()

    def is_completed(self) -> bool:
        """
        Метод для проверки завершенности калибровки.
        Возвращает True, если калибровка завершена и содержит данные, иначе False.
        """
        if self.calibration_data and self.calibration_data.get("stereo_mode", None):
            # TODO: ADD MORE DATA CHECKING
            return True
        return False

    def clear(self) -> None:
        """
        Метод для корректной очистки данных калибровки.
        Используется для сброса данных калибровки в начальное состояние.
        """
        self.calibration_data = {}

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
        return [os.path.join(images_dir, name) for name in image_names]

    def set_calibration_method(self, calibration_method: "CalibrationMethod") -> None:
        self.calibration_method = calibration_method

    def calibrate(self, images_path: str) -> None:
        image_paths = self.__get_image_paths_sorted(images_path)
        self.calibration_data = self.calibration_method.calibrate(image_paths)

    def calibrate_stereo(self, left_images_path: str, right_images_path: str) -> None:
        left_image_paths = self.__get_image_paths_sorted(left_images_path)
        right_image_paths = self.__get_image_paths_sorted(right_images_path)
        self.calibration_data = self.calibration_method.calibrate_stereo(
            left_image_paths, right_image_paths
        )

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


class CalibrationMethod(ABC):
    @abstractmethod
    def calibrate(self, image_paths: list) -> dict:
        pass

    @abstractmethod
    def calibrate_stereo(self, left_image_paths: list, right_image_paths: list) -> dict:
        pass


class ChessboardCalibrationMethod(CalibrationMethod):
    def __init__(self):
        self.square_size = 30  # размер квадрата шахматного рисунка (в миллиметрах)
        self.board_size = (11, 7)  # размер доски (кол-во пересечений углов квадратов)

    def set_chessboard_sizes(self, square_size: int, board_size: tuple) -> None:
        self.square_size = square_size
        self.board_size = board_size

    def is_chessboard_size_correct(self, test_image_filepath: str) -> None:
        if not os.path.exists(test_image_filepath):
            raise FileNotFoundError(
                "Ошибка проверки размера шахматной доски: Файл не найден."
            )

        example_image = cv2.imread(test_image_filepath)
        example_image = cv2.cvtColor(example_image, cv2.COLOR_BGR2GRAY)

        self.ret, _ = cv2.findChessboardCorners(example_image, self.board_size)
        if not self.ret:
            raise ChessboardSizeIsIncorrect("Размер шахматной доски указан неверно.")

    def calibrate(self, image_paths: list) -> dict:
        if image_paths is None or len(image_paths) < 1:
            raise ValueError("Недостаточно изображений для калибровки.")

        camera_parameters = {}
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

        gray = cv2.cvtColor(cv2.imread(image_paths[0]), cv2.COLOR_BGR2GRAY).shape[::-1]
        image_height, image_width = image.shape[:2]
        flags = 0

        final_objpoints = []
        for i in range(20):
            final_objpoints.append(initial_objpoints)
        (
            retval,
            camera_matrix,
            distortion_coeffs,
            rotation_vectors,
            translation_vectors,
        ) = cv2.calibrateCamera(
            final_objpoints, initial_imgpoints, gray, None, None, flags=flags
        )
        if not retval:
            raise RuntimeError("Калибровка камеры не удалась.")

        rotation_matrices = []
        transformation_matrices = []
        for k, r in enumerate(rotation_vectors):
            rotation_matrices.append(cv2.Rodrigues(r)[0])
            transformation_matrices.append(
                np.vstack(
                    (
                        np.hstack((rotation_matrices[k], translation_vectors[k])),
                        np.array([0, 0, 0, 1]),
                    )
                )
            )

        new_matrix, roi = cv2.getOptimalNewCameraMatrix(
            camera_matrix,
            distortion_coeffs,
            (image_width, image_height),
            1,
            (image_width, image_height),
        )
        if new_matrix is None or roi is None:
            raise RuntimeError("Ошибка получения оптимальной новой матрицы камеры.")

        if np.sum(roi) == 0:
            roi = (0, 0, image_width - 1, image_height - 1)

        camera_parameters = {
            "stereo_mode": True,
            "calibration_method": self.__class__.__name__,
            "square_size": self.square_size,
            "board_size": self.board_size,
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

        return camera_parameters

    def calibrate_stereo(self, left_image_paths: list, right_image_paths: list) -> dict:
        if not left_image_paths or not right_image_paths:
            raise ValueError(
                "Ошибка калибровки стереокамеры: Пути к изображениям не могут быть пустыми."
            )

        dual_camera_parameters = {}

        left_imgpoints, left_objpoints = self.__get_img_and_obj_points(left_image_paths)
        right_imgpoints, right_objpoints = self.__get_img_and_obj_points(
            right_image_paths
        )

        try:
            left_camera_parameters = self.calibrate(left_image_paths)
            right_camera_parameters = self.calibrate(right_image_paths)
        except Exception as e:
            raise RuntimeError(f"Ошибка при калибровке одной из камер: {e}")

        k1 = left_camera_parameters["camera_matrix"]
        d1 = left_camera_parameters["distortion_coeffs"]
        k2 = right_camera_parameters["camera_matrix"]
        d2 = right_camera_parameters["distortion_coeffs"]

        gray = cv2.imread(left_image_paths[0], 0)
        g = gray.shape[::-1]

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-5)
        flags = 0
        flags |= cv2.CALIB_FIX_INTRINSIC

        objp = []
        for i in range(20):
            objp.append(left_objpoints)

        (ret, K1, D1, K2, D2, R, t, E, F) = cv2.stereoCalibrate(
            objp,
            left_imgpoints,
            right_imgpoints,
            k1,
            d1,
            k2,
            d2,
            g,
            criteria=criteria,
            flags=flags,
        )
        if not ret:
            raise RuntimeError("Не удалось провести стереокалибровку.")

        # Составление трансформационной матрицы
        T = np.vstack((np.hstack((R, t)), np.array([0, 0, 0, 1])))

        dual_camera_parameters = {
            "stereo_mode": True,
            "calibration_method": self.__class__.__name__,
            "square_size": self.square_size,
            "board_size": self.board_size,
            "transformation_matrix": T,
            "essential_matrix": E,
            "fundamental_matrix": F,
            "mean_reprojection_error": ret,
        }

        # Добавление параметров левой камеры с префиксом "L_"
        for Lkey in left_camera_parameters.keys():
            if (
                Lkey == "stereo_mode"
                or Lkey == "calibration_method"
                or Lkey == "square_size"
                or Lkey == "board_size"
            ):
                continue  # Эти ключи записаны выше единожды для словаря
            name = "L_" + str(Lkey)
            dual_camera_parameters[name] = left_camera_parameters[Lkey]

        # Добавление параметров правой камеры с префиксом "R_"
        for Rkey in right_camera_parameters.keys():
            if (
                Lkey == "stereo_mode"
                or Lkey == "calibration_method"
                or Lkey == "square_size"
                or Lkey == "board_size"
            ):
                continue  # Эти ключи записаны выше единожды для словаря
            name = "R_" + str(Rkey)
            dual_camera_parameters[name] = right_camera_parameters[Rkey]

        return dual_camera_parameters

    def calculate_errors(
        self, camera_parameters: dict, imgpoints: list, objpoints: np.ndarray
    ):
        imgp = np.array(imgpoints)
        imgp = imgp.reshape((imgp.shape[0], imgp.shape[1], imgp.shape[3]))
        objp = np.array(objpoints)
        K = np.array(camera_parameters["camera_matrix"])
        D = np.array(camera_parameters["distortion_coeffs"])
        R = np.array(camera_parameters["rotation_vectors"])
        T = np.array(camera_parameters["translation_vectors"])
        N = imgp.shape[0]

        imgpNew = []
        for i in range(N):
            temp, _ = cv2.projectPoints(objp, R[i], T[i], K, D)
            imgpNew.append(temp.reshape((temp.shape[0], temp.shape[2])))
        imgpNew = np.array(imgpNew)

        err = []
        for i in range(N):
            err.append(imgp[i] - imgpNew[i])
        err = np.array(err)

        def RMSE(err):
            return np.sqrt(np.mean(np.sum(err**2, axis=1)))

        errall = np.copy(err[0])
        rmsePerView = [RMSE(err[0])]
        for i in range(1, N):
            errall = np.vstack((errall, err[i]))
            rmsePerView.append(RMSE(err[i]))

        rmseAll = RMSE(errall)
        return rmsePerView, rmseAll

    def __get_img_and_obj_points(self, image_paths: list) -> tuple[list, np.ndarray]:
        self.is_chessboard_size_correct(image_paths[0])
        imgpoints = self.__generate_image_points(image_paths)
        objpoints = self.__detect_board_corners()
        return imgpoints, objpoints

    def __detect_board_corners(self) -> np.ndarray:
        objpoints = np.zeros((self.board_size[0] * self.board_size[1], 3), np.float32)
        objpoints[:, :2] = np.mgrid[
            0 : self.board_size[0], 0 : self.board_size[1]
        ].T.reshape(-1, 2)
        objpoints *= self.square_size
        return objpoints

    def __generate_image_points(self, image_paths: list) -> list:
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        imgpoints = []

        for path in image_paths:
            image = cv2.imread(path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            found, corners = cv2.findChessboardCorners(image, self.board_size)

            if found:
                refined = cv2.cornerSubPix(gray, corners, (4, 4), (-1, -1), criteria)
                imgpoints.append(refined)

        return imgpoints


class CalibrationRoomCalibrationMethod(CalibrationMethod):
    def __init__(self):
        self.points: list[list[int, int]] = []

    def calibrate(self, image_paths: list) -> dict:
        # TODO: Реализовать логику калибровки
        pass

    def calibrate_stereo(self, left_image_paths: list, right_image_paths: list) -> dict:
        # TODO: Реализовать логику калибровки для режима двух камер.
        pass

    def add_point(self, point: list[int, int]) -> None:
        if len(point) != 2:
            raise ValueError("Точка должна быть списком с двумя значениями координат.")
        self.points.append(point)

    def remove_last_point(self) -> list[list[int, int]]:
        if len(self.points) < 1:
            raise ValueError("Удаление точки невозможно. Нет точек.")
        self.points.pop()
        return self.points

    def remove_point(self, point_index: int) -> list[list[int, int]]:
        if point_index < 0 or point_index >= len(self.points):
            raise ValueError(
                f"Индекс точки должен быть в диапазоне от 0 до {len(self.points) - 1}."
            )
        if len(self.points < 1):
            raise ValueError("Удаление точки невозможно. Нет точек.")
        self.points.pop(point_index)
        return self.points


class ChessboardSizeIsIncorrect(Exception):
    pass


class CalibrationParameterNotFound(Exception):
    pass
