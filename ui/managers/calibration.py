import os

from PySide6.QtWidgets import QFileDialog, QMessageBox

from ui.managers import AbstractWindow, AbstractGUIManager
from archpoint.handlers import CalibrationHandler


class CalibrationManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow, handler: CalibrationHandler):
        self.window = window
        self.handler = handler

        self.__connect_buttons()

    def update_calibration_done_page(self) -> None:
        if self.handler.is_completed():
            self.window.ui.textBrowser_calibrationResultsData.setText(
                self.handler.get_calibration_data_as_string()
            )
        else:
            self.window.ui.textBrowser_calibrationResultsData.clear()

    def __connect_buttons(self) -> None:
        self.connect_button(
            # SET IMAGES DIRECTORY
            self.window.ui.pushButton_setCalibrationImagesDirectory,
            self.__on_set_calibration_images_directory_clicked,
        )
        self.connect_button(
            # SET SECOND IMAGES DIRECTORY (STEREO MODE)
            self.window.ui.pushButton_setCalibrationImagesDirectorySecondCamera,
            self.__on_set_calibration_images_directory_second_camera_clicked,
        )

        self.connect_button(
            # RETURN -> TO CALIBRATION INITIAL OPTIONS CHOICE
            self.window.ui.pushButton_returnToCalibrationChoice,
            self.window.ui.page_calibrationInitialChoice,
        )

        self.connect_button(
            # FROM (CHESSBOARD METHOD) TIPS -> TO MAIN PAGE
            self.window.ui.pushButton_calibrationChessboardSteps_1_3_GoToCalibration,
            self.window.ui.page_calibrationSteps_4_MainPage,
        )
        self.connect_button(
            # FROM (CHESSBOARD METHOD) -> RETURN TO METHOD SELECTION
            self.window.ui.pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection,
            self.window.ui.page_calibrationSteps_0_MethodSelection,
        )

        self.connect_button(
            # FROM (ROOM METHOD) TIPS -> TO MAIN PAGE
            self.window.ui.pushButton_calibrationRoomSteps_1_3_GoToCalibration,
            self.window.ui.page_calibrationSteps_4_MainPage,
        )
        self.connect_button(
            # FROM (ROOM METHOD) -> RETURN TO METHOD SELECTION
            self.window.ui.pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection,
            self.window.ui.page_calibrationSteps_0_MethodSelection,
        )

        self.connect_button(
            # FROM CALIBRATION_MAIN_PAGE -> TO (ABSTRACT METHOD TIPS)
            self.window.ui.pushButton_calibrationSteps_4_returnToTipsButton,
            self.__on_calibration_steps_4_return_to_tips_button_clicked,
        )

        self.connect_button(
            # SAVE CALIBRATION RESULTS
            self.window.ui.pushButton_saveCalibrationResults,
            self.__on_save_calibration_results_clicked,
        )

        self.connect_button(
            # METHOD SELECTION (ROOM METHOD CHOOSED)
            self.window.ui.pushButton_calibrationSteps_0_MethodManualSelectButton,
            self.__on_calibration_steps_0_method_manual_select_button_clicked,
        )
        self.connect_button(
            # METHOD SELECTION (CHESSBOARD METHOD CHOOSED)
            self.window.ui.pushButton_calibrationSteps_0_MethodAutoSelectButton,
            self.__on_calibration_steps_0_method_auto_select_button_clicked,
        )

    def __on_set_calibration_images_directory_clicked(self) -> None:
        calibration_images_directory = QFileDialog.getExistingDirectory(
            self.window, "Выберите директорию с изображениями"
        )
        self.window.ui.lineEdit_calibrationImagesDirectory.setText(
            calibration_images_directory
        )

    def __on_set_calibration_images_directory_second_camera_clicked(self) -> None:
        calibration_images_directory_second_camera = QFileDialog.getExistingDirectory(
            self.window, "Выберите директорию с изображениями второй камеры"
        )
        self.window.ui.lineEdit_calibrationImagesDirectorySecondCamera.setText(
            calibration_images_directory_second_camera
        )

    def __on_save_calibration_results_clicked(self) -> None:
        calibration_results_file_path, _ = QFileDialog.getSaveFileName(
            self.window,
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
                    self.window,
                    "Файл сохранён",
                    "Результаты калибровки успешно сохранены.",
                )
            except Exception as e:
                QMessageBox.critical(
                    self.window,
                    "Ошибка",
                    f"Произошла ошибка при сохранении данных: {e}",
                )

    def __on_calibration_steps_0_method_manual_select_button_clicked(self) -> None:
        self.handler.set_calibration_method("room")

        # HIDING CHESSBOARD SIZE SETTINGS AND TIPS:
        self.window.ui.groupBox_chessboardSize_Setting.hide()
        self.window.ui.label_chessboardSize_Setting_Tips.hide()

        self.window.ui.stackedWidget_workSpace.setCurrentWidget(
            self.window.ui.page_calibrationSteps_1_3_PreparingRoomTips
        )

    def __on_calibration_steps_0_method_auto_select_button_clicked(self) -> None:
        self.handler.set_calibration_method("chessboard")

        # SHOWING CHESSBOARD SIZE SETTINGS AND TIPS:
        self.window.ui.groupBox_chessboardSize_Setting.show()
        self.window.ui.label_chessboardSize_Setting_Tips.show()

        self.window.ui.stackedWidget_workSpace.setCurrentWidget(
            self.window.ui.page_calibrationSteps_1_3_PreparingChessboardTips
        )

    def __on_calibration_steps_4_return_to_tips_button_clicked(self) -> None:
        if self.handler.get_calibration_method_name() == "room":
            self.window.ui.stackedWidget_workSpace.setCurrentWidget(
                self.window.ui.page_calibrationSteps_1_3_PreparingRoomTips
            )
        elif self.handler.get_calibration_method_name() == "chessboard":
            self.window.ui.stackedWidget_workSpace.setCurrentWidget(
                self.window.ui.page_calibrationSteps_1_3_PreparingChessboardTips
            )
