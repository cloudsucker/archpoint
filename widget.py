import os
import sys

from ui.ui_form import Ui_Widget
from handlers.calibration_handler import CalibrationHandler
from handlers.hloc_handler import HLOC_Handler
from handlers.project import Project
from PySide6.QtWidgets import (
    QFileDialog,
    QApplication,
    QWidget,
    QMessageBox,
    QPushButton,
)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # HANDLERS
        self.calibration_handler = CalibrationHandler()
        self.project = Project()
        self.hloc_handler = HLOC_Handler()

        # GUI VARIABLES
        self.theme = 0

        self.ui.stackedWidget_workSpace.setCurrentWidget(self.ui.page_calibrationChoice)

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
        self.ui.pushButton_calibration_start.clicked.connect(
            self.on_calibration_start_clicked
        )
        self.ui.pushButton_calibration_skip.clicked.connect(
            self.on_calibration_skip_clicked
        )
        self.connect_navigation_button(
            self.ui.pushButton_calibrationStartFromPreparing,
            self.ui.page_calibrationSteps_4,
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
        pass  # TODO: ADD SETTINGS PAGE AND PAGE SWTITCHING PROCESSING

    def on_theme_toggle_clicked(self):
        pass  # TODO: ADD THEME SWITCHING LOGIC

    def on_calibration_start_clicked(self):
        self.ui.stackedWidget_workSpace.setCurrentWidget(
            self.ui.page_calibrationSteps_1_3
        )
        # TODO: ADD CALIBRATION LOGGING LOGIC
        # TODO: ADD
        # self.calibration_handler.calibrate()

    def on_calibration_from_file_clicked(self):
        calibration_file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", "JSON files (*.json)"
        )

        if (
            calibration_file_path
            and os.path.exists(calibration_file_path)
            and calibration_file_path.endswith(".json")
        ):
            self.calibration_handler.load_calibration_data(calibration_file_path)
            self.carefully_go_to_processing()

    def on_calibration_skip_clicked(self):
        self.carefully_go_to_processing()

    def on_choose_project_clicked(self):
        project_path = QFileDialog.getExistingDirectory(
            self, "Выберите директорию проекта"
        )
        if project_path and os.path.isdir(project_path):
            self.project.open_project(project_path)
            self.carefully_go_to_processing()

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
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
