from archpoint.handlers import ProjectHandler, HLOC_Handler, CalibrationHandler
from archpoint.handlers.calibration_handler import (
    ChessboardCalibrationMethod,
    CalibrationRoomCalibrationMethod,
)


class Archpoint:
    def __init__(
        self,
        project_handler: ProjectHandler,
        hloc_handler: HLOC_Handler,
        calibration_handler: CalibrationHandler,
    ):
        self.project_handler = project_handler
        self.hloc_handler = hloc_handler
        self.calibration_handler = calibration_handler

        self.calibration_methods = {
            "chessboard": ChessboardCalibrationMethod,
            "room": CalibrationRoomCalibrationMethod,
        }

    # PROJECT:
    def create_project(self, name: str, path: str) -> None:
        self.project_handler.create_project(name, path)

    def open_project(self, path: str) -> None:
        self.project_handler.open_project(path)

    # HLOC HANDLER:
    def process_images(self, images_path: str, outputs_path: str) -> None:
        self.hloc_handler.process_images(images_path, outputs_path)

    # CALIBRATION HANDLER:
    def set_calibration_method(self, method: str) -> None:
        if method not in self.calibration_methods:
            raise ValueError("Недопустимый метод калибровки.")
        calibration_method = self.calibration_methods[method]
        self.calibration_handler.set_calibration_method(calibration_method)

    def load_calibration_data(self, filepath: str) -> None:
        self.calibration_handler.load_calibration_data(filepath)

    def save_calibration_data(self, filepath: str) -> None:
        self.calibration_handler.save_calibration_data(filepath)

    def calibrate(self, images_path: str) -> None:
        self.calibration_handler.calibrate(images_path)

    def calibrate_stereo(self, left_images_path: str, right_images_path: str) -> None:
        self.calibration_handler.calibrate_stereo(left_images_path, right_images_path)

    def get_calibration_data_as_string(self) -> None:
        return self.calibration_handler.get_calibration_data_as_string()
