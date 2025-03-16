import os
import cv2
import numpy as np

from abc import ABC, abstractmethod


class CalibrationHandler:
    def __init__(self):
        self.images_path = ""
        self.calibration_file_path = ""
        self.calibration_data = {}
        self.calibration_method: CalibrationMethod = ChessboardCalibrationMethod()

        self.__calibration_filename_json = "parameters.json"
        self.__calibration_filename_npz = "parameters.npz"

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
        if not os.path.exists(filepath) or not filepath.endswith(".npz"):
            raise FileNotFoundError("Файл калибровки не найден.")

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

    def calibrate(self, images_path: str) -> None:
        image_paths = self.__get_image_paths_sorted(images_path)
        self.calibration_data = self.calibration_method.calibrate(image_paths)

    def calibrate_stereo(self, left_images_path: str, right_images_path: str) -> None:
        left_image_paths = self.__get_image_paths_sorted(left_images_path)
        right_image_paths = self.__get_image_paths_sorted(right_images_path)
        self.calibration_data = self.calibration_method.calibrate_stereo(
            left_image_paths, right_image_paths
        )


class CalibrationMethod(ABC):
    @abstractmethod
    def calibrate(self, image_paths: list) -> dict:
        pass

    @abstractmethod
    def calibrate_stereo(self, left_image_paths: list, right_image_paths: list) -> None:
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

    def calibrate(self, image_paths: list) -> dict:
        camera_parameters = {}
        imgpoints, objpoints = self.__get_img_and_obj_points(image_paths)

        gray = cv2.cvtColor(cv2.imread(image_paths[0]), cv2.COLOR_BGR2GRAY)
        gray = gray.shape[::-1]

        flags = 0

        obj_points = []
        for i in range(20):
            obj_points.append(objpoints)
        (ret, mtx, dist, rvecs, tvecs) = cv2.calibrateCamera(
            obj_points, imgpoints, gray, None, None, flags=flags
        )

        Rmtx = []
        Tmtx = []
        k = 0
        for r in rvecs:
            Rmtx.append(cv2.Rodrigues(r)[0])
            Tmtx.append(
                np.vstack((np.hstack((Rmtx[k], tvecs[k])), np.array([0, 0, 0, 1])))
            )
            k += 1

        img = cv2.imread(image_paths[0], 0)
        h, w = img.shape[:2]
        newmtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

        if np.sum(roi) == 0:
            roi = (0, 0, w - 1, h - 1)

        camera_parameters = {
            "calibration_method": self.__class__.__name__,
            "square_size": self.square_size,
            "board_size": self.board_size,
            "object_points": objpoints,
            "camera_matrix": mtx,
            "distortion_coeffs": dist,
            "roi": roi,
            "new_camera_matrix": newmtx,
            "rotation_vectors": rvecs,
            "rotation_matrices": Rmtx,
            "extrinsic_parameters": Tmtx,
            "translation_vectors": tvecs,
        }

        return camera_parameters

    def calibrate_stereo(self, left_image_paths: list, right_image_paths: list):
        dual_camera_parameters = {}

        left_imgpoints, left_objpoints = self.__get_img_and_obj_points(left_image_paths)
        right_imgpoints, right_objpoints = self.__get_img_and_obj_points(
            right_image_paths
        )

        left_camera_parameters = self.calibrate(left_image_paths)
        right_camera_parameters = self.calibrate(right_image_paths)

        k1 = left_camera_parameters["Intrinsic"]
        d1 = left_camera_parameters["Distortion"]

        k2 = right_camera_parameters["Intrinsic"]
        d2 = right_camera_parameters["Distortion"]

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

        T = np.vstack((np.hstack((R, t)), np.array([0, 0, 0, 1])))

        dual_camera_parameters = {
            "transformation_matrix": T,
            "essential_matrix": E,
            "fundamental_matrix": F,
            "mean_reprojection_error": ret,
        }

        for Lkey in left_camera_parameters.keys():
            name = "L_" + str(Lkey)
            dual_camera_parameters[name] = left_camera_parameters[Lkey]

        for Rkey in right_camera_parameters.keys():
            name = "R_" + str(Rkey)
            dual_camera_parameters[name] = right_camera_parameters[Rkey]

        return dual_camera_parameters

    def calculate_errors(
        self, camera_parameters: dict, imgpoints: list, objpoints: np.ndarray
    ):
        imgp = np.array(imgpoints)
        imgp = imgp.reshape((imgp.shape[0], imgp.shape[1], imgp.shape[3]))
        objp = np.array(objpoints)
        K = np.array(camera_parameters["Intrinsic"])
        D = np.array(camera_parameters["Distortion"])
        R = np.array(camera_parameters["RotVektor"])
        T = np.array(camera_parameters["TransVektor"])
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


class ChessboardSizeIsIncorrect(Exception):
    pass
