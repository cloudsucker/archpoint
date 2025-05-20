import os
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from ui.forms.ui_form import Ui_Widget
from ui.managers import (
    AbstractGUIManager,
    CalibrationManager,
    DotsCreatorManager,
    ImagesManager,
    ProcessingManager,
    ProjectManager,
    SettingsManager,
    StylesManager,
)


class AppRouter(AbstractGUIManager):
    """Главный класс графического интерфейса приложения.
    Отвечает за общую навигацию в приложении и связку менеджеров приложения."""

    def __init__(
        self,
        ui: Ui_Widget,
        window: QMainWindow,
        calibration_manager: CalibrationManager,
        dots_creator_manager: DotsCreatorManager,
        images_manager: ImagesManager,
        processing_manager: ProcessingManager,
        project_manager: ProjectManager,
        settings_manager: SettingsManager,
        styles_manager: StylesManager,
    ):
        self.ui = ui
        self.window = window
        self.calibration_manager = calibration_manager
        self.dots_creator_manager = dots_creator_manager
        self.images_manager = images_manager
        self.processing_manager = processing_manager
        self.project_manager = project_manager
        self.settings_manager = settings_manager
        self.styles_manager = styles_manager

        # УСТАНОВКА НАЧАЛЬНОГО ВИДЖЕТА
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationInitialChoice
        )

        self.__connect_buttons()

    def go_to_calibration(self) -> None:
        """Метод для корректного перехода к этапу калибровки.
        Проверяет состояние калибровки и переходит к соответствующему виджету."""
        self.calibration_manager.update_calibration_done_page()
        if self.calibration_manager.handler.is_completed():
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_calibrationSteps_5_done
            )
            return
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationInitialChoice
        )

    def go_to_processing(self) -> None:
        if self.project_manager.handler.is_project_initialized:
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_processingProcess
            )
            if self.calibration_manager.handler.is_completed():
                self.ui.checkBox_preprocessingImages.setChecked(True)
                self.ui.checkBox_preprocessingImages.setHidden(False)
            else:
                self.ui.checkBox_preprocessingImages.setChecked(False)
                self.ui.checkBox_preprocessingImages.setHidden(True)
            return
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_processingChoiceProject
        )
        self.ui.pushButton_pageProcess.setChecked(True)

    def go_to_settings(self) -> None:
        self.ui.stackedWidget_workSpace.setCurrentWidget(self.ui.page_settings)

    def go_to_dots_creator(
        self, images_path: str, second_camera_images_path: str | None = None
    ) -> None:
        if second_camera_images_path:
            self.calibration_manager.handler.initialize_room_images_handler(
                images_path, second_camera_images_path
            )
        else:
            self.calibration_manager.handler.initialize_room_images_handler(images_path)

        self.dots_creator_manager.preprocess_dots_creator_page(
            self.calibration_manager.handler.calibration_method.images_handler
        )
        if not self.dots_creator_manager.is_completed():
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_calibrationSteps_5_ImageDotsCreating
            )
        # else:
        #    TODO: ЗАПУСКАТЬ КАЛИБРОВКУ ЕСЛИ РАЗМЕТКА ИЗОБРАЖЕНИЙ ЗАВЕРШЕНА
        #    pass

    def __connect_buttons(self) -> None:
        # LEFT MENU BUTTONS
        self.ui.pushButton_pageCalibration.clicked.connect(self.go_to_calibration)
        self.ui.pushButton_pageProcess.clicked.connect(self.go_to_processing)
        self.ui.pushButton_settings.clicked.connect(self.go_to_settings)
        self.ui.pushButton_themeToggle.clicked.connect(self.__on_theme_toggle_clicked)

        # CALIBRATION INITIAL OPTIONS
        self.ui.pushButton_page_calibrationFromFileOptionButton.clicked.connect(
            # FROM FILE
            self.__on_calibration_from_file_option_button_clicked
        )
        self.connect_button(
            # START
            self.ui.pushButton_page_calibrationStartOptionButton,
            self.ui.page_calibrationSteps_0_MethodSelection,
        )
        self.ui.pushButton_page_calibrationSkipOptionButton.clicked.connect(
            # SKIP
            self.go_to_processing
        )

        # CALIBRATION START (STARTS PROCESSING)
        self.ui.pushButton_calibrationProcessStart.clicked.connect(
            self.__on_calibration_process_start_clicked
        )
        # CALIBRATION CANCEL (ABORTING)
        self.ui.pushButton_cancelCalibration.clicked.connect(
            self.__on_cancel_calibration_clicked
        )

        # PROJECT INITIAL OPTIONS PAGE (CHOOSING DIRECTORY) -> PROCESSING MAIN PAGE
        self.ui.pushButton_chooseProject.clicked.connect(
            self.__on_choose_project_clicked
        )
        # PROJECT CREATING PAGE (SUBMITING FORM) -> PROCESSING MAIN PAGE
        self.ui.pushButton_newProjectCreatingSubmit.clicked.connect(
            self.__on_new_project_creating_submit_clicked
        )

        # PROCESSING START -> PROCESSING STARTING
        self.ui.pushButton_processingStart.clicked.connect(
            self.__on_processing_start_clicked
        )

    def __on_theme_toggle_clicked(self) -> None:
        self.styles_manager.switch_theme()

    def __on_calibration_from_file_option_button_clicked(self) -> None:
        calibration_file_path, _ = QFileDialog.getOpenFileName(
            self.window, "Выберите файл", "", ".npz files (*.npz)"
        )

        if calibration_file_path and os.path.exists(calibration_file_path):
            if calibration_file_path.endswith(".npz"):
                try:
                    self.calibration_manager.handler.load_calibration_data(
                        calibration_file_path
                    )
                    if self.calibration_manager.handler.is_completed():

                        # TODO: ADD CALIBRATION DATA DISPLAYING ON MAIN PAGE
                        # TO MAKE USER BE SURE ABOUT IT'S LOADING

                        self.go_to_calibration()
                    else:
                        QMessageBox.critical(
                            self.window,
                            "Ошибка",
                            "Ошибка загрузки данных из файла калибровки.",
                        )
                except Exception as e:
                    QMessageBox.critical(
                        self.window,
                        "Ошибка",
                        f"Произошла ошибка при загрузке данных: {e}",
                    )
            else:
                QMessageBox.warning(
                    self.window,
                    "Неверный формат",
                    "Пожалуйста, выберите файл с расширением .npz.",
                )

    def __on_calibration_process_start_clicked(self) -> None:
        images_directory = self.ui.lineEdit_calibrationImagesDirectory.text()

        if not images_directory:
            QMessageBox.critical(
                self.window,
                "Ошибка",
                "Пожалуйста, укажите директорию с изображениями.",
            )
            return

        if not os.path.exists(images_directory):
            QMessageBox.critical(
                self.window,
                "Ошибка",
                "Пожалуйста, укажите корректную директорию с изображениями.",
            )
            return

        if self.ui.groupBox_calibrationImagesDirectoryFieldSecondCamera.isChecked():
            images_directory_second_camera = (
                self.ui.lineEdit_calibrationImagesDirectorySecondCamera.text()
            )

            if not images_directory_second_camera:
                QMessageBox.critical(
                    self.window,
                    "Ошибка",
                    "Пожалуйста, укажите директорию с изображениями второй камеры.",
                )
                return

            if not os.path.exists(images_directory_second_camera):
                QMessageBox.critical(
                    self.window,
                    "Ошибка",
                    "Пожалуйста, укажите корректную директорию с изображениями второй камеры.",
                )
                return

            if self.calibration_manager.handler.get_calibration_method_name() == "room":
                self.go_to_dots_creator(
                    images_directory, images_directory_second_camera
                )
                return
            elif (
                self.calibration_manager.handler.get_calibration_method_name()
                == "chessboard"
            ):
                self.calibration_manager.handler.calibrate_stereo(
                    images_directory, images_directory_second_camera
                )
        elif self.calibration_manager.handler.get_calibration_method_name() == "room":
            self.go_to_dots_creator(images_directory)
            return
        elif (
            self.calibration_manager.handler.get_calibration_method_name()
            == "chessboard"
        ):
            self.calibration_manager.handler.calibrate(images_directory)

        # TODO: ADD CALIBRATION LOGGING LOGIC
        # TODO: ADD PROCESSING IMAGES DISPLAYING

        self.go_to_calibration()

    def __on_cancel_calibration_clicked(self) -> None:
        self.calibration_manager.handler.clear()
        self.go_to_calibration()

    def __on_choose_project_clicked(self) -> None:
        project_path = QFileDialog.getExistingDirectory(
            self.window, "Выберите директорию проекта"
        )
        if project_path and os.path.isdir(project_path):
            try:
                self.project_manager.handler.open_project(project_path)
                self.go_to_processing()
            except Exception as e:
                QMessageBox.critical(
                    self.window, "Ошибка", f"Ошибка открытия проекта: {e}"
                )

    def __on_new_project_creating_submit_clicked(self) -> None:
        project_name = self.ui.lineEdit_newProjectCreatingNameField.text()
        project_path = self.ui.lineEdit_newProjectCreatingPathField.text()

        if not project_name or not project_path:
            QMessageBox.critical(
                self.window, "Ошибка", "Пожалуйста, укажите имя проекта и путь."
            )
            return
        try:
            self.project_manager.handler.create_project(project_name, project_path)
            self.go_to_processing()
        except Exception as e:
            QMessageBox.critical(self.window, "Ошибка", f"Ошибка создания проекта: {e}")

    def __on_processing_start_clicked(self) -> None:
        images_directory = self.ui.lineEdit_imagesDirectoryField.text()
        if not images_directory or not os.path.isdir(images_directory):
            QMessageBox.critical(
                self.window,
                "Ошибка",
                "Пожалуйста, укажите директорию с изображениями.",
            )
            return

        if (
            not self.ui.checkBox_preprocessingImages.isHidden()
            and self.ui.checkBox_preprocessingImages.isChecked()
        ):
            if self.ui.groupBox_secondCameraProcessingField.isEnabled():
                images_directory_second_camera = (
                    self.ui.lineEdit_secondCameraProcessingImagesDirectory.text()
                )
                if not os.path.isdir(images_directory_second_camera):
                    QMessageBox.critical(
                        self.window,
                        "Ошибка",
                        "Пожалуйста, укажите директорию с изображениями второй камеры.",
                    )
                    return
                self.calibration_manager.handler.fix_images_stereo(
                    images_directory,
                    images_directory_second_camera,
                    self.project_manager.handler.path + "/processed_images",
                    self.project_manager.handler.path + "/processed_images",
                )
            else:
                self.calibration_manager.handler.fix_images(
                    images_directory,
                    self.project_manager.handler.path + "/processed_images",
                )

        # TODO: UNCOMMENT THIS CODE AFTER TESTING
        # self.hloc_handler.process_images(
        #     self.project.path + "/processed_images", self.project.path
        # )
