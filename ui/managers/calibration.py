import os

from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from ui.forms.ui_form import Ui_Widget
from ui.managers.abstract import AbstractGUIManager
from archpoint.handlers import CalibrationHandler


class CalibrationManager(AbstractGUIManager):
    def __init__(
        self, ui: Ui_Widget, main_window: QMainWindow, handler: CalibrationHandler
    ):
        self.ui = ui
        self.main_window = main_window
        self.handler = handler

        self.__connect_buttons()

    def update_calibration_done_page(self):
        if self.handler.is_completed():
            self.ui.textBrowser_calibrationResultsData.setText(
                self.handler.get_calibration_data_as_string()
            )
        else:
            self.ui.textBrowser_calibrationResultsData.clear()

    def __connect_buttons(self):
        self.connect_button(
            # SET IMAGES DIRECTORY
            self.ui.pushButton_setCalibrationImagesDirectory,
            self.__on_set_calibration_images_directory_clicked,
        )
        self.connect_button(
            # SET SECOND IMAGES DIRECTORY (STEREO MODE)
            self.ui.pushButton_setCalibrationImagesDirectorySecondCamera,
            self.__on_set_calibration_images_directory_second_camera_clicked,
        )

        self.connect_button(
            # RETURN -> TO CALIBRATION INITIAL OPTIONS CHOICE
            self.ui.pushButton_returnToCalibrationChoice,
            self.ui.page_calibrationInitialChoice,
        )

        self.connect_button(
            # FROM (CHESSBOARD METHOD) TIPS -> TO MAIN PAGE
            self.ui.pushButton_calibrationChessboardSteps_1_3_GoToCalibration,
            self.ui.page_calibrationSteps_4_MainPage,
        )
        self.connect_button(
            # FROM (CHESSBOARD METHOD) -> RETURN TO METHOD SELECTION
            self.ui.pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection,
            self.ui.page_calibrationSteps_0_MethodSelection,
        )

        self.connect_button(
            # FROM (ROOM METHOD) TIPS -> TO MAIN PAGE
            self.ui.pushButton_calibrationRoomSteps_1_3_GoToCalibration,
            self.ui.page_calibrationSteps_4_MainPage,
        )
        self.connect_button(
            # FROM (ROOM METHOD) -> RETURN TO METHOD SELECTION
            self.ui.pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection,
            self.ui.page_calibrationSteps_0_MethodSelection,
        )

        self.connect_button(
            # FROM CALIBRATION_MAIN_PAGE -> TO (ABSTRACT METHOD TIPS)
            self.ui.pushButton_calibrationSteps_4_returnToTipsButton,
            self.__on_calibration_steps_4_return_to_tips_button_clicked,
        )

        self.connect_button(
            # SAVE CALIBRATION RESULTS
            self.ui.pushButton_saveCalibrationResults,
            self.__on_save_calibration_results_clicked,
        )

        self.connect_button(
            # METHOD SELECTION (ROOM METHOD CHOOSED)
            self.ui.pushButton_calibrationSteps_0_MethodManualSelectButton,
            self.__on_calibration_steps_0_method_manual_select_button_clicked,
        )
        self.connect_button(
            # METHOD SELECTION (CHESSBOARD METHOD CHOOSED)
            self.ui.pushButton_calibrationSteps_0_MethodAutoSelectButton,
            self.__on_calibration_steps_0_method_auto_select_button_clicked,
        )

    def __on_set_calibration_images_directory_clicked(self):
        calibration_images_directory = QFileDialog.getExistingDirectory(
            self.main_window, "Выберите директорию с изображениями"
        )
        self.ui.lineEdit_calibrationImagesDirectory.setText(
            calibration_images_directory
        )

    def __on_set_calibration_images_directory_second_camera_clicked(self):
        calibration_images_directory_second_camera = QFileDialog.getExistingDirectory(
            self.main_window, "Выберите директорию с изображениями второй камеры"
        )
        self.ui.lineEdit_calibrationImagesDirectorySecondCamera.setText(
            calibration_images_directory_second_camera
        )

    def __on_save_calibration_results_clicked(self):
        calibration_results_file_path, _ = QFileDialog.getSaveFileName(
            self.main_window,
            "Сохранить результаты калибровки",
            "",
            ".npz files (*.npz)",
        )
        if (
            calibration_results_file_path
            and os.path.splitext(calibration_results_file_path)[1] == ".npz"
        ):
            try:
                self.handler.save_calibration_data(calibration_results_file_path)
                QMessageBox.information(
                    self.main_window,
                    "Файл сохранён",
                    "Результаты калибровки успешно сохранены.",
                )
            except Exception as e:
                QMessageBox.critical(
                    self.main_window,
                    "Ошибка",
                    f"Произошла ошибка при сохранении данных: {e}",
                )

    def __on_calibration_steps_0_method_manual_select_button_clicked(self):
        self.handler.set_calibration_method("room")
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationSteps_1_3_PreparingRoomTips
        )

    def __on_calibration_steps_0_method_auto_select_button_clicked(self):
        self.handler.set_calibration_method("chessboard")
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationSteps_1_3_PreparingChessboardTips
        )

    def __on_calibration_steps_4_return_to_tips_button_clicked(self):
        if self.handler.get_calibration_method_name() == "room":
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_calibrationSteps_1_3_PreparingRoomTips
            )
        elif self.handler.get_calibration_method_name() == "chessboard":
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_calibrationSteps_1_3_PreparingChessboardTips
            )
