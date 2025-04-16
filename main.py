import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QApplication,
    QWidget,
    QMessageBox,
    QPushButton,
    QGraphicsScene,
    QTableWidgetItem,
    QGraphicsPixmapItem,
)

from PySide6.QtGui import QIcon, QPixmap

# TODO: ADD THE TRAY ICON OR DELETE THIS
# from PySide6.QtWidgets import QSystemTrayIcon

from ui.ui_form import Ui_Widget
from archpoint.handlers import ProjectHandler, HLOC_Handler, CalibrationHandler
from archpoint.calibration_methods.room import RoomImageDotsEditor


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        central_widget = QWidget()
        self.ui.setupUi(central_widget)
        self.setCentralWidget(central_widget)

        # HANDLERS
        self.calibration_handler = CalibrationHandler()
        self.project = ProjectHandler()
        self.hloc_handler = HLOC_Handler()

        # GUI SETTINGS
        self.theme = "light"
        # self.apply_styles()
        self.adjustSize()
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationInitialChoice
        )

        self.setWindowTitle("Archpoint")
        self.app_logo_icon = QIcon("static/logo_v2_black.png")
        self.app_logo_pixmap = QPixmap("static/logo_v2_black.png")

        # TODO: ADD THE TRAY ICON OR DELETE THIS
        # self.tray_icon = QSystemTrayIcon(self)
        # self.tray_icon.setIcon(self.app_logo_icon)
        # self.tray_icon.setVisible(True)

        self.setWindowIcon(self.app_logo_icon)
        self.preprocess_app_images()

        # ============================= BUTTON CONNECTIONS =============================

        # LEFT MENU PAGES:
        self.ui.pushButton_pageCalibration.clicked.connect(
            self.carefully_go_to_calibration
        )
        self.ui.pushButton_pageProcess.clicked.connect(self.on_page_process_clicked)
        # LEFT MENU SETTINGS:
        self.ui.pushButton_settings.clicked.connect(self.on_settings_clicked)
        # LEFT MENU THEME:
        self.ui.pushButton_themeToggle.clicked.connect(self.on_theme_toggle_clicked)

        # CALIBRATION INITIAL OPTIONS:
        self.ui.pushButton_page_calibrationFromFileOptionButton.clicked.connect(
            self.on_calibration_from_file_option_button_clicked
        )
        self.ui.pushButton_page_calibrationSkipOptionButton.clicked.connect(
            self.on_calibration_skip_option_button_clicked
        )
        self.connect_navigation_button(
            self.ui.pushButton_page_calibrationStartOptionButton,
            self.ui.page_calibrationSteps_0_MethodSelection,
        )

        # CALIBRATION DIRECTORIES:
        self.ui.pushButton_setCalibrationImagesDirectory.clicked.connect(
            self.on_set_calibration_images_directory_clicked
        )
        self.ui.pushButton_setCalibrationImagesDirectorySecondCamera.clicked.connect(
            self.on_set_calibration_images_directory_second_camera_clicked
        )

        # CALIBRATION PAGES RETURN AND NEXT BUTTONS:
        self.connect_navigation_button(
            self.ui.pushButton_returnToCalibrationChoice,
            self.ui.page_calibrationInitialChoice,
        )
        self.connect_navigation_button(
            self.ui.pushButton_calibrationChessboardSteps_1_3_GoToCalibration,
            self.ui.page_calibrationSteps_4_MainPage,
        )
        self.ui.pushButton_calibrationProcessStart.clicked.connect(
            self.on_calibration_process_start_clicked
        )
        self.connect_navigation_button(
            self.ui.pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection,
            self.ui.page_calibrationSteps_0_MethodSelection,
        )
        self.connect_navigation_button(
            self.ui.pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection,
            self.ui.page_calibrationSteps_0_MethodSelection,
        )
        self.connect_navigation_button(
            self.ui.pushButton_calibrationRoomSteps_1_3_GoToCalibration,
            self.ui.page_calibrationSteps_4_MainPage,
        )
        self.ui.pushButton_calibrationSteps_4_returnToTipsButton.clicked.connect(
            self.on_calibration_steps_4_return_to_tips_button_clicked
        )
        self.ui.pushButton_cancelCalibration.clicked.connect(
            self.on_cancel_calibration_clicked
        )
        self.ui.pushButton_saveCalibrationResults.clicked.connect(
            self.on_save_calibration_results_clicked
        )
        self.ui.pushButton_calibrationSteps_0_MethodManualSelectButton.clicked.connect(
            self.on_calibration_steps_0_method_manual_select_button_clicked
        )
        self.connect_navigation_button(
            self.ui.pushButton_calibrationSteps_0_MethodAutoSelectButton,
            self.ui.page_calibrationSteps_1_3_PreparingChessboardTips,
        )

        # PROJECT BUTTONS:
        self.connect_navigation_button(
            self.ui.pushButton_newProject, self.ui.page_processingNewProjectCreating
        )
        self.ui.pushButton_chooseProject.clicked.connect(self.on_choose_project_clicked)
        self.ui.pushButton_newProjectCreatingPathChoose.clicked.connect(
            self.on_new_project_creating_path_choose_clicked
        )
        self.ui.pushButton_newProjectCreatingSubmit.clicked.connect(
            self.on_new_project_creating_submit_clicked
        )
        self.connect_navigation_button(
            self.ui.pushButton_newProjectCreatingCancel,
            self.ui.page_processingChoiceProject,
        )

        # PROCESSING BUTTONS:
        self.ui.pushButton_imagesDirectoryChoose.clicked.connect(
            self.on_images_directory_choose_clicked
        )
        self.ui.pushButton_setSecondCameraProcessingImagesDirectory.clicked.connect(
            self.on_set_second_camera_processing_images_directory_clicked
        )
        self.ui.pushButton_processingStart.clicked.connect(
            self.on_processing_start_clicked
        )

    # =================================== UTILS FUNCTIONS ===================================

    def preprocess_app_images(self):
        self.ui.label_appLogo.setPixmap(self.app_logo_pixmap.scaledToHeight(155))
        self.ui.label_page_calibrationFromFileOptionIcon.setPixmap(
            QPixmap("static/file/file-black.png").scaledToHeight(70)
        )

    def connect_navigation_button(self, button: QPushButton, target_widget: QWidget):
        """Метод для связки навигационных кнопок и целевых виджетов."""
        if button and target_widget:
            button.clicked.connect(
                lambda: self.ui.stackedWidget_workSpace.setCurrentWidget(target_widget)
            )

    # ============================ CAREFULLY REDIRECTING FUNCTIONS ============================

    def carefully_go_to_processing(self):
        """Безопасный переход к стадии обработки (в зависимости от наличия
        проекта переходит к его выбору или прямиком к процессу обработки)."""
        if self.project.is_project_initialized:
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_processingProcess
            )
            if self.calibration_handler.is_completed():
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

    def carefully_go_to_calibration(self):
        self.update_calibration_done_page()
        if self.calibration_handler.is_completed():
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_calibrationSteps_5_done
            )
            return
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationInitialChoice
        )

    def update_calibration_done_page(self):
        if self.calibration_handler.is_completed():
            self.ui.textBrowser_calibrationResultsData.setText(
                self.calibration_handler.get_calibration_data_as_string()
            )
        else:
            self.ui.textBrowser_calibrationResultsData.clear()

    def carefully_go_to_dots_creator(
        self, images_path: str, second_camera_images_path: str | None = None
    ):
        if second_camera_images_path:
            self.calibration_handler.initialize_dots_creator(
                images_path, second_camera_images_path
            )
        else:
            self.calibration_handler.initialize_dots_creator(images_path)

        self.update_dots_creator()
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationSteps_5_ImageDotsCreating
        )

    def update_dots_creator(self):
        self.room_method_images: dict[str, RoomImageDotsEditor] = (
            self.calibration_handler.calibration_method.images
        )

        for image_path, image_dots in self.room_method_images.items():
            if image_dots.is_completed():
                continue

            self.room_method_current_image_path = image_path

            image_name = os.path.basename(image_path)
            self.ui.label_imageDotsCreator_ImageName.setText(image_name)

            pixmap = QPixmap(image_path)
            scene = QGraphicsScene()
            scene.clear()

            item = QGraphicsPixmapItem(pixmap)
            scene.addItem(item)

            self.ui.graphicsView_imageDotsCreator_ImagePreview.setScene(scene)
            self.ui.graphicsView_imageDotsCreator_ImagePreview.setAlignment(
                Qt.AlignCenter
            )
            self.ui.graphicsView_imageDotsCreator_ImagePreview.fitInView(
                item.boundingRect(), Qt.KeepAspectRatio
            )

            return

    # ==================================== BUTTON HANDLERS ====================================

    # LEFT MENU BUTTONS:
    def on_page_process_clicked(self):
        self.carefully_go_to_processing()

    def on_settings_clicked(self):
        self.ui.stackedWidget_workSpace.setCurrentWidget(self.ui.page_settings)

    def on_theme_toggle_clicked(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.apply_styles()

    # CALIBRATION:
    def on_calibration_from_file_option_button_clicked(self):
        calibration_file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", ".npz files (*.npz)"
        )

        if calibration_file_path and os.path.exists(calibration_file_path):
            if calibration_file_path.endswith(".npz"):
                try:
                    self.calibration_handler.load_calibration_data(
                        calibration_file_path
                    )
                    if self.calibration_handler.is_completed():

                        # TODO: ADD CALIBRATION DATA DISPLAYING ON MAIN PAGE
                        # TO MAKE USER BE SURE ABOUT IT'S LOADING

                        self.carefully_go_to_calibration()
                    else:
                        QMessageBox.critical(
                            self,
                            "Ошибка",
                            "Ошибка загрузки данных из файла калибровки.",
                        )
                except Exception as e:
                    QMessageBox.critical(
                        self, "Ошибка", f"Произошла ошибка при загрузке данных: {e}"
                    )
            else:
                QMessageBox.warning(
                    self,
                    "Неверный формат",
                    "Пожалуйста, выберите файл с расширением .npz.",
                )

    def on_set_calibration_images_directory_clicked(self):
        calibration_images_directory = QFileDialog.getExistingDirectory(
            self, "Выберите директорию с изображениями"
        )
        self.ui.lineEdit_calibrationImagesDirectory.setText(
            calibration_images_directory
        )

    def on_set_calibration_images_directory_second_camera_clicked(self):
        calibration_images_directory_second_camera = QFileDialog.getExistingDirectory(
            self, "Выберите директорию с изображениями второй камеры"
        )
        self.ui.lineEdit_calibrationImagesDirectorySecondCamera.setText(
            calibration_images_directory_second_camera
        )

    def on_calibration_process_start_clicked(self):
        images_directory = self.ui.lineEdit_calibrationImagesDirectory.text()

        if not images_directory:
            QMessageBox.critical(
                self,
                "Ошибка",
                "Пожалуйста, укажите директорию с изображениями.",
            )
            return

        if not os.path.exists(images_directory):
            QMessageBox.critical(
                self,
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
                    self,
                    "Ошибка",
                    "Пожалуйста, укажите директорию с изображениями второй камеры.",
                )
                return

            if not os.path.exists(images_directory_second_camera):
                QMessageBox.critical(
                    self,
                    "Ошибка",
                    "Пожалуйста, укажите корректную директорию с изображениями второй камеры.",
                )
                return

            if self.calibration_handler.get_calibration_method_name() == "room":
                self.carefully_go_to_dots_creator(
                    images_directory, images_directory_second_camera
                )
                return
            elif self.calibration_handler.get_calibration_method_name() == "chessboard":
                self.calibration_handler.calibrate_stereo(
                    images_directory, images_directory_second_camera
                )
        else:
            if self.calibration_handler.get_calibration_method_name() == "room":
                self.carefully_go_to_dots_creator(images_directory)
                return
            elif self.calibration_handler.get_calibration_method_name() == "chessboard":
                self.calibration_handler.calibrate(images_directory)

        # TODO: ADD CALIBRATION LOGGING LOGIC
        # TODO: ADD PROCESSING IMAGES DISPLAYING

        self.carefully_go_to_calibration()

    def on_save_calibration_results_clicked(self):
        calibration_results_file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить результаты калибровки", "", ".npz files (*.npz)"
        )
        if (
            calibration_results_file_path
            and os.path.splitext(calibration_results_file_path)[1] == ".npz"
        ):
            try:
                self.calibration_handler.save_calibration_data(
                    calibration_results_file_path
                )
                QMessageBox.information(
                    self,
                    "Файл сохранён",
                    "Результаты калибровки успешно сохранены.",
                )
            except Exception as e:
                QMessageBox.critical(
                    self, "Ошибка", f"Произошла ошибка при сохранении данных: {e}"
                )

    def on_calibration_skip_option_button_clicked(self):
        self.carefully_go_to_processing()

    def on_cancel_calibration_clicked(self):
        self.calibration_handler.clear()
        self.carefully_go_to_calibration()

    def on_calibration_steps_0_method_manual_select_button_clicked(self):
        self.calibration_handler.set_calibration_method("room")
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationSteps_1_3_PreparingRoomTips
        )

    def on_calibration_steps_0_method_auto_select_button_clicked(self):
        self.calibration_handler.set_calibration_method("chessboard")
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationSteps_1_3_PreparingChessboardTips
        )

    def on_calibration_steps_4_return_to_tips_button_clicked(self):
        if self.calibration_handler.get_calibration_method_name() == "room":
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_calibrationSteps_1_3_PreparingRoomTips
            )
        elif self.calibration_handler.get_calibration_method_name() == "chessboard":
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_calibrationSteps_1_3_PreparingChessboardTips
            )

    # PROJECT:
    def on_choose_project_clicked(self):
        project_path = QFileDialog.getExistingDirectory(
            self, "Выберите директорию проекта"
        )
        if project_path and os.path.isdir(project_path):
            try:
                self.project.open_project(project_path)
                self.carefully_go_to_processing()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка открытия проекта: {e}")

    def on_new_project_creating_path_choose_clicked(self):
        project_path = QFileDialog.getExistingDirectory(self, "Выберите папку проекта")
        if project_path and os.path.isdir(project_path):
            self.ui.lineEdit_newProjectCreatingPathField.setText(project_path)

    def on_new_project_creating_submit_clicked(self):
        project_name = self.ui.lineEdit_newProjectCreatingNameField.text()
        project_path = self.ui.lineEdit_newProjectCreatingPathField.text()

        if not project_name or not project_path:
            QMessageBox.critical(
                self, "Ошибка", "Пожалуйста, укажите имя проекта и путь."
            )
            return
        try:
            self.project.create_project(project_name, project_path)
            self.carefully_go_to_processing()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка создания проекта: {e}")

    # HLOC PROCESSING:
    def on_images_directory_choose_clicked(self):
        images_directory = QFileDialog.getExistingDirectory(
            self, "Выберите директорию с изображениями"
        )
        if images_directory and os.path.isdir(images_directory):
            self.ui.lineEdit_imagesDirectoryField.setText(images_directory)

    def on_set_second_camera_processing_images_directory_clicked(self):
        images_directory = QFileDialog.getExistingDirectory(
            self, "Выберите директорию с изображениями второй камеры"
        )
        if images_directory and os.path.isdir(images_directory):
            self.ui.lineEdit_secondCameraProcessingImagesDirectory.setText(
                images_directory
            )

    def on_processing_start_clicked(self):
        images_directory = self.ui.lineEdit_imagesDirectoryField.text()
        if not images_directory or not os.path.isdir(images_directory):
            QMessageBox.critical(
                self, "Ошибка", "Пожалуйста, укажите директорию с изображениями."
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
                        self,
                        "Ошибка",
                        "Пожалуйста, укажите директорию с изображениями второй камеры.",
                    )
                    return
                self.calibration_handler.fix_images_stereo(
                    images_directory,
                    images_directory_second_camera,
                    self.project.path + "/processed_images",
                    self.project.path + "/processed_images",
                )
            else:
                self.calibration_handler.fix_images(
                    images_directory, self.project.path + "/processed_images"
                )

        # TODO: UNCOMMENT THIS CODE AFTER TESTING
        # self.hloc_handler.process_images(
        #     self.project.path + "/processed_images", self.project.path
        # )

    # THEMES & STYLES:
    def apply_styles(self):
        path = f"static/styles/{self.theme}.css"
        with open(path, "r") as f:
            self.window().setStyleSheet(f.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# LITTLE BEAUTIES TODO:
#   - Добавить кнопку "Отменить" для проекта (обработки).
#   - При пропуске калибровки установить состояние отказа от калибровки, редиректить на страницу отказа.
#   - Добавить отображение названия проекта после его открытия или создания на странице обработки.
#   - Перерисововать логотип.
#   - Добавить все иконки для кнопок.
#   - Переделать визуальное оформление страниц.
