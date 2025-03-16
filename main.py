import os
import sys

from PySide6.QtWidgets import (
    QFileDialog,
    QApplication,
    QWidget,
    QMessageBox,
    QPushButton,
)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QSystemTrayIcon

from PySide6.QtWidgets import QMainWindow
from ui.ui_form import Ui_Widget
from handlers.project import Project
from handlers.hloc_handler import HLOC_Handler
from handlers.calibration_handler import CalibrationHandler


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        central_widget = QWidget()
        self.ui.setupUi(central_widget)
        self.setCentralWidget(central_widget)

        # HANDLERS
        self.calibration_handler = CalibrationHandler()
        self.project = Project()
        self.hloc_handler = HLOC_Handler()

        # GUI SETTINGS
        self.theme = 0
        self.adjustSize()
        self.ui.stackedWidget_workSpace.setCurrentWidget(self.ui.page_calibrationChoice)

        self.setWindowTitle("Archpoint")
        self.app_logo_icon = QIcon("static/logo_black.png")
        self.app_logo_pixmap = QPixmap("static/logo_black.png")

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.app_logo_icon)
        self.tray_icon.setVisible(True)

        self.setWindowIcon(self.app_logo_icon)
        self.preprocess_app_images()

        # BUTTON CONNECTIONS
        self.connect_navigation_button(
            self.ui.pushButton_pageCalibration, self.ui.page_calibrationChoice
        )
        self.ui.pushButton_pageProcess.clicked.connect(self.on_page_process_clicked)
        self.ui.pushButton_settings.clicked.connect(self.on_settings_clicked)
        self.ui.pushButton_themeToggle.clicked.connect(self.on_theme_toggle_clicked)
        self.ui.pushButton_calibration_from_file.clicked.connect(
            self.on_calibration_from_file_clicked
        )
        self.ui.pushButton_calibration_skip.clicked.connect(
            self.on_calibration_skip_clicked
        )
        self.ui.pushButton_setCalibrationImagesDirectory.clicked.connect(
            self.on_set_calibration_images_directory_clicked
        )
        self.connect_navigation_button(
            self.ui.pushButton_calibrationStartFromPreparing,
            self.ui.page_calibrationSteps_4,
        )
        self.connect_navigation_button(
            self.ui.pushButton_calibration_start,
            self.ui.page_calibrationSteps_1_3,
        )
        self.ui.pushButton_calibrationProcessStart.clicked.connect(
            self.on_calibration_process_start_clicked
        )
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
        self.ui.pushButton_imagesDirectoryChoose.clicked.connect(
            self.on_images_directory_choose_clicked
        )
        self.ui.pushButton_processingStart.clicked.connect(
            self.on_processing_start_clicked
        )

    def preprocess_app_images(self):
        self.ui.label_appLogo.setPixmap(self.app_logo_pixmap.scaledToHeight(155))
        self.ui.label_calibration_from_file_icon.setPixmap(
            QPixmap(r"static\file\file-black.png").scaledToHeight(70)
        )
        # app.setStyleSheet(
        #     """
        #     QGroupBox {
        #         border-top: none;
        #     }
        # """
        # )

    def connect_navigation_button(self, button: QPushButton, target_widget: QWidget):
        """Метод для связки навигационных кнопок и целевых виджетов."""
        if button and target_widget:
            button.clicked.connect(
                lambda: self.ui.stackedWidget_workSpace.setCurrentWidget(target_widget)
            )

    def carefully_go_to_processing(self):
        """Безопасный переход к стадии обработки (в зависимости от наличия
        проекта переходит к его выбору или прямиком к процессу обработки)."""
        if self.project.is_project_initialized:
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_processingProcess
            )
            return
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_processingChoiceProject
        )

    # = = = = = = = = = = = = = = = = = = BUTTON HANDLERS = = = = = = = = = = = = =

    def on_page_process_clicked(self):
        self.carefully_go_to_processing()

    def on_settings_clicked(self):
        # TODO: ADD SETTINGS PAGE
        # TODO: ADD PAGE SWTITCHING LOGIC HERE
        pass

    def on_theme_toggle_clicked(self):
        # TODO: ADD THEME SWITCHING LOGIC
        pass

    def on_calibration_from_file_clicked(self):
        calibration_file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", ".npz files (*.npz)"
        )

        if calibration_file_path and os.path.exists(calibration_file_path):
            if calibration_file_path.endswith(".npz"):
                try:
                    self.calibration_handler.load_calibration_data(
                        calibration_file_path
                    )
                    if self.calibration_handler.calibration_data:

                        # TODO: ADD CALIBRATION DATA DISPLAYING ON MAIN PAGE
                        # TO MAKE USER BE SURE ABOUT IT'S LOADING

                        self.carefully_go_to_processing()
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

    def on_calibration_process_start_clicked(self):
        images_directory = self.ui.lineEdit_calibrationImagesDirectory.text()

        if os.path.exists(images_directory):
            self.calibration_handler.calibrate(images_directory)
            # TODO: ADD CALIBRATION LOGGING LOGIC
            # TODO: ADD PROCESSING IMAGES DISPLAYING
            self.ui.stackedWidget_workSpace.setCurrentWidget(
                self.ui.page_calibrationSteps_5_done
            )

            self.ui.textBrowser_calibrationResultsData.setText(
                self.calibration_handler.get_calibration_data_as_string()
            )
        else:
            QMessageBox.critical(
                self, "Ошибка", "Пожалуйста, укажите директорию с изображениями."
            )

    def on_calibration_skip_clicked(self):
        self.carefully_go_to_processing()

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

    def on_images_directory_choose_clicked(self):
        images_directory = QFileDialog.getExistingDirectory(
            self, "Выберите директорию с изображениями"
        )
        if images_directory and os.path.isdir(images_directory):
            self.ui.lineEdit_imagesDirectoryField.setText(images_directory)

    def on_processing_start_clicked(self):
        images_directory = self.ui.lineEdit_imagesDirectoryField.text()
        if not images_directory or not os.path.isdir(images_directory):
            QMessageBox.critical(
                self, "Ошибка", "Пожалуйста, укажите директорию с изображениями."
            )
            return

        self.hloc_handler.process_images(images_directory, self.project.path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
