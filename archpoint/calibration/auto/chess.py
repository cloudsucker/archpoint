import os
import cv2
import numpy as np

from archpoint.calibration import CalibrationMethodAbstract
from archpoint.calibration.auto.exceptions import ChessboardSizeIsIncorrect


class ChessboardCalibrationMethod(CalibrationMethodAbstract):
    """
    Класс для проведения автоматической калибровки с помощью шахматного рисунка.

    Attributes:
        square_size (int): размер квадрата шахматного рисунка (в миллиметрах).
        board_size (tuple): кол-во внутренних углов (узлов) шахматного рисунка.
        __global_parameters (list): список глобальных (не требующих перезаписи для каждой камеры в режиме стерео) параметров калибровки.

    Примечание:
        Внутренние углы (узлы) шахматного рисунка могут быть найдены по формуле (N - 1) * (M - 1), где N и M - размеры шахматной доски.
    """

    def __init__(self):
        self.square_size = 30
        self.board_size = (11, 7)
        self.__global_parameters = ["square_size", "board_size"]

    def __eq__(self, other):
        return isinstance(other, str) and other == "chessboard"

    def set_chessboard_sizes(
        self, square_size: int | None = None, board_size: tuple | None = None
    ) -> None:
        """
        Метод для установки размера шахматной доски.

        Parameters:
            square_size (int): размер квадрата шахматного рисунка (в миллиметрах)
            board_size (tuple | None): кол-во внутренних углов (узлов) шахматного рисунка.
        """
        if square_size is not None:
            self.square_size = square_size
        if board_size is not None:
            self.board_size = board_size

    def is_chessboard_size_correct(self, test_image_filepath: str) -> None:
        """
        Метод для проверки указанного размера шахматной доски на тестовом изображении.

        Parameters:
            test_image_filepath (str): путь к тестовому изображению.

        Raises:
            ChessboardSizeIsIncorrect: если размер шахматной доски указан неверно.
        """
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
        """
        Метод для получения параметров камеры в моно-режиме.

        Parameters:
            image_paths (list): список путей к изображениям.

        Returns:
            dict: словарь с параметрами калибровки.
        """

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

        final_objpoints = [initial_objpoints for _ in range(len(image_paths))]
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
        """
        Метод для получения параметров камеры в стерео-режиме.

        Parameters:
            left_image_paths (list): список путей к изображениям с левой камеры.
            right_image_paths (list): список путей к изображениям с правой камеры.

        Returns:
            dict: словарь с параметрами калибровки.
        """
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
            "square_size": self.square_size,
            "board_size": self.board_size,
            "transformation_matrix": T,
            "essential_matrix": E,
            "fundamental_matrix": F,
            "mean_reprojection_error": ret,
        }

        # ADDING LEFT CAMERA PARAMETERS WITH PREFIX 'L_'
        for Lkey in left_camera_parameters.keys():
            # IGNORING GLOBAL PARAMETERS
            if Lkey in self.__global_parameters:
                continue
            name = "L_" + str(Lkey)
            dual_camera_parameters[name] = left_camera_parameters[Lkey]

        # ADDING RIGHT CAMERA PARAMETERS WITH PREFIX 'R_'
        for Rkey in right_camera_parameters.keys():
            # IGNORING GLOBAL PARAMETERS
            if Lkey in self.__global_parameters:
                continue
            name = "R_" + str(Rkey)
            dual_camera_parameters[name] = right_camera_parameters[Rkey]

        return dual_camera_parameters

    def calculate_errors(
        self, camera_parameters: dict, imgpoints: list, objpoints: np.ndarray
    ):
        """
        Метод для расчета ошибок калибровки.

        Parameters:
            camera_parameters (dict): словарь с параметрами калибровки.
            imgpoints (list): список точек на изображении.
            objpoints (np.ndarray): массив настоящих координат точек.

        Returns:
            dict: словарь с ошибками калибровки.
        """
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
        """
        Метод для получения автоматически определённых точек на изображении
        и массива настоящих координат точек.

        Parameters:
            image_paths (list): список путей к изображениям.

        Returns:
            tuple: кортеж из списка точек на изображении и массива настоящих координат точек.
        """
        self.is_chessboard_size_correct(image_paths[0])
        imgpoints = self.__generate_image_points(image_paths)
        objpoints = self.__detect_board_corners()
        return imgpoints, objpoints

    def __detect_board_corners(self) -> np.ndarray:
        """
        Метод для автоматического определения настоящих координат точек.

        Returns:
            np.ndarray: массив настоящих координат точек.
        """
        objpoints = np.zeros((self.board_size[0] * self.board_size[1], 3), np.float32)
        objpoints[:, :2] = np.mgrid[
            0 : self.board_size[0], 0 : self.board_size[1]
        ].T.reshape(-1, 2)
        objpoints *= self.square_size
        return objpoints

    def __generate_image_points(self, image_paths: list) -> list:
        """
        Метод для автоматического определения точек на изображении.

        Parameters:
            image_paths (list): список путей к изображениям.

        Returns:
            list: список точек на изображении.
        """
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
