import cv2
import numpy as np

from archpoint.calibration import CalibrationMethodAbstract
from archpoint.calibration.manual.room_image_collection import RoomImageCollection
from archpoint.calibration.manual.exceptions import SomeImagesHaveNoDots


class RoomCalibrationMethod(CalibrationMethodAbstract):
    def __init__(self):
        self.images_handler = RoomImageCollection()

    def __eq__(self, value):
        return isinstance(value, str) and value == "room"

    def initialize(
        self, image_paths: list[str], second_image_paths: list[str] | None = None
    ) -> None:
        self.images_handler.initialize(image_paths, second_image_paths)

    def calibrate(self, image_paths: list) -> dict:
        if not image_paths:
            raise ValueError("Недостаточно изображений для калибровки.")
        if not self.is_completed():
            raise SomeImagesHaveNoDots("Не все изображения были размечены.")

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

        image_height, image_width = image.shape[:2]
        img_size = (image_width, image_height)

        final_objpoints = [initial_objpoints[0]] * len(image_paths)

        initial_camera_matrix = cv2.initCameraMatrix2D(
            objectPoints=final_objpoints,
            imagePoints=initial_imgpoints,
            imageSize=img_size,
            aspectRatio=1.0,
        )

        flags = cv2.CALIB_USE_INTRINSIC_GUESS

        (
            retval,
            camera_matrix,
            distortion_coeffs,
            rotation_vectors,
            translation_vectors,
        ) = cv2.calibrateCamera(
            objectPoints=final_objpoints,
            imagePoints=initial_imgpoints,
            imageSize=img_size,
            cameraMatrix=initial_camera_matrix,
            distCoeffs=None,
            flags=flags,
        )
        if not retval:
            raise RuntimeError("Калибровка камеры не удалась.")

        rotation_matrices = []
        transformation_matrices = []
        for rvec, tvec in zip(rotation_vectors, translation_vectors):
            R, _ = cv2.Rodrigues(rvec)
            rotation_matrices.append(R)
            RT = np.vstack((np.hstack((R, tvec)), [0, 0, 0, 1]))
            transformation_matrices.append(RT)

        new_matrix, roi = cv2.getOptimalNewCameraMatrix(
            camera_matrix, distortion_coeffs, img_size, 1, img_size
        )
        if new_matrix is None or roi is None:
            raise RuntimeError("Ошибка получения оптимальной новой матрицы камеры.")

        if np.sum(roi) == 0:
            roi = (0, 0, image_width - 1, image_height - 1)

        return {
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

    def calibrate_stereo(
        self, left_image_paths: list[str], right_image_paths: list[str]
    ) -> dict:
        if not self.is_completed():
            raise SomeImagesHaveNoDots("Не все изображения были размечены.")
        if len(left_image_paths) != len(right_image_paths):
            raise ValueError("Количество изображений слева и справа должно совпадать.")
        if len(left_image_paths) < 1:
            raise ValueError("Недостаточно изображений для стереокалибровки.")

        left_imgpoints, left_objpoints = self.images_handler.get_img_and_obj_points(
            left_image_paths
        )
        right_imgpoints, right_objpoints = self.images_handler.get_img_and_obj_points(
            right_image_paths
        )

        if len(left_imgpoints) == 0 or len(right_imgpoints) == 0:
            raise ValueError("Не удалось извлечь точки для калибровки.")

        left_image = cv2.imread(left_image_paths[0])
        right_image = cv2.imread(right_image_paths[0])
        if left_image is None or right_image is None:
            raise ValueError("Не удалось загрузить одно из изображений.")

        img_size_left = left_image.shape[1], left_image.shape[0]
        img_size_right = right_image.shape[1], right_image.shape[0]

        if img_size_left != img_size_right:
            raise ValueError(
                "Изображения левого и правого каналов должны иметь одинаковый размер."
            )

        flags = cv2.CALIB_USE_INTRINSIC_GUESS

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-6)

        # Калибровка каждой камеры отдельно
        mtx_left_init = cv2.initCameraMatrix2D(
            objectPoints=left_objpoints,
            imagePoints=left_imgpoints,
            imageSize=img_size_left,
            aspectRatio=1.0,
        )

        ret_left, mtx_left, dist_left, rvecs_left, tvecs_left = cv2.calibrateCamera(
            left_objpoints,
            left_imgpoints,
            img_size_left,
            cameraMatrix=mtx_left_init,
            distCoeffs=None,
            flags=cv2.CALIB_USE_INTRINSIC_GUESS,
        )

        mtx_right_init = cv2.initCameraMatrix2D(
            objectPoints=right_objpoints,
            imagePoints=right_imgpoints,
            imageSize=img_size_right,
            aspectRatio=1.0,
        )

        ret_right, mtx_right, dist_right, rvecs_right, tvecs_right = (
            cv2.calibrateCamera(
                right_objpoints,
                right_imgpoints,
                img_size_right,
                cameraMatrix=mtx_right_init,
                distCoeffs=None,
                flags=cv2.CALIB_USE_INTRINSIC_GUESS,
            )
        )

        if not (ret_left and ret_right):
            raise RuntimeError("Не удалось выполнить калибровку отдельных камер.")

        # Стереокалибровка
        ret_stereo, mtx_left, dist_left, mtx_right, dist_right, R, T, E, F = (
            cv2.stereoCalibrate(
                left_objpoints,
                left_imgpoints,
                right_imgpoints,
                mtx_left,
                dist_left,
                mtx_right,
                dist_right,
                img_size_left,
                criteria=criteria,
                flags=cv2.CALIB_USE_INTRINSIC_GUESS,
            )
        )

        if not ret_stereo:
            raise RuntimeError("Стереокалибровка не удалась.")

        # Получение карт смещения (rectification maps)
        R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(
            mtx_left,
            dist_left,
            mtx_right,
            dist_right,
            img_size_left,
            R,
            T,
            flags=0,
            alpha=0,
        )

        stereo_params = {
            "left_camera_matrix": mtx_left,
            "left_distortion_coeffs": dist_left,
            "right_camera_matrix": mtx_right,
            "right_distortion_coeffs": dist_right,
            "rotation_between_cameras": R,
            "translation_between_cameras": T,
            "essential_matrix": E,
            "fundamental_matrix": F,
            "rectification_transform_left": R1,
            "rectification_transform_right": R2,
            "projection_matrix_left": P1,
            "projection_matrix_right": P2,
            "disparity_to_depth_map": Q,
            "roi_left": roi1,
            "roi_right": roi2,
        }

        return stereo_params

    def __get_img_and_obj_points(
        self, image_paths: list[str]
    ) -> tuple[list, np.ndarray]:
        imgpoints = []
        objpoints = []
        imgpoints, objpoints = self.images_handler.get_img_and_obj_points(image_paths)
        return imgpoints, objpoints

    def is_completed(self) -> bool:
        return (
            self.images_handler.are_all_image_dots_set()
            and self.images_handler.are_all_real_coordinates_completed()
        )
