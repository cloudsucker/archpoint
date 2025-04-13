from archpoint.handlers import ProjectHandler, HLOC_Handler, CalibrationHandler
from archpoint.calibration_methods import ChessboardCalibrationMethod
from archpoint.calibration_methods import CalibrationRoomCalibrationMethod


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

        self.images_directory = "processed_images"

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

    def fix_images(self, images_path: str) -> None:
        if not self.project_handler.is_project_initialized:
            raise ProjectNotInitializedError("Проект не инициализирован.")

        results_path = self.project_handler.path + "/" + self.images_directory
        self.calibration_handler.fix_images(images_path, results_path)

    def fix_stereo_images(self, left_images_path: str, right_images_path: str) -> None:
        if not self.project_handler.is_project_initialized:
            raise ProjectNotInitializedError("Проект не инициализирован.")

        self.calibration_handler.fix_images_stereo(left_images_path, right_images_path)


class ArchpointError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class ProjectNotInitializedError(ArchpointError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message
