import os
import cv2
import json
import numpy as np

from abc import ABC, abstractmethod


class CalibrationHandler:
    def __init__(self):
        self.images_path = ""
        self.calibration_file_path = ""
        self.calibration_data = {}
        self.calibration_method: CalibrationMethod = ChessboardCalibrationMethod

        self.__calibration_filename = "calibration.json"

    def load_calibration_data(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError("Файл калибровки не найден.")

        with open(filepath, "r", encoding="utf-8") as f:
            self.calibration_data = json.load(f)

    def save_calibration_data(self, filepath: str) -> None:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.calibration_data, f, indent=4, ensure_ascii=False)

    def calibrate(self):
        self.calibration_data = self.calibration_method.calibrate()


class CalibrationMethod(ABC):
    @abstractmethod
    def calibrate(self, images_path: str):
        pass


class ChessboardCalibrationMethod(CalibrationMethod):
    def __init__(self):
        self.square_size = 30  # размер квадрата шахматного рисунка (в миллиметрах)
        self.board_size = (11, 7)  # размер доски (кол-во пересечений углов квадратов)

        # TODO: add dual camera mode support
        # self.dual_camera_mode = False

    def set_chessboard_sizes(self, square_size: int, board_size: tuple) -> None:
        self.square_size = square_size
        self.board_size = board_size

    def is_chessboard_size_correct(self, test_image_filepath: str) -> None:
        example_image = cv2.imread(test_image_filepath)
        example_image = cv2.cvtColor(example_image, cv2.COLOR_BGR2GRAY)

        self.ret, _ = cv2.findChessboardCorners(example_image, self.board_size)
        if not self.ret:
            raise ChessboardSizeIsIncorrect("Размер шахматной доски указан неверно.")

    def calibrate(self, images_path: str):
        self.__get_images_sorted(images_path)
        imgpoints = self.__generate_image_points(self.images)
        objpoints = self.__detect_board_corners()

    def __generate_image_points(self, image_paths: str):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        imgpoints = []

        for image_path in image_paths:
            img = cv2.imread(image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners1 = cv2.findChessboardCorners(img, self.board_size)
            if ret:
                corners2 = cv2.cornerSubPix(gray, corners1, (4, 4), (-1, -1), criteria)
                imgpoints.append(corners2)
        return imgpoints

    def __detect_board_corners(self):
        objpoints = np.zeros((self.board_size[0] * self.board_size[1], 3), np.float32)
        objpoints[:, :2] = np.mgrid[
            0 : self.board_size[0], 0 : self.board_size[1]
        ].T.reshape(-1, 2)
        objpoints *= self.square_size
        return objpoints


class ChessboardSizeIsIncorrect(Exception):
    pass
