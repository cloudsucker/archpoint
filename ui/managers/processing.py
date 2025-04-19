import os

from PySide6.QtWidgets import QMainWindow, QFileDialog

from ui.forms.ui_form import Ui_Widget
from ui.managers.abstract import AbstractGUIManager
from archpoint.handlers import HLOC_Handler


class ProcessingManager(AbstractGUIManager):
    def __init__(self, ui: Ui_Widget, main_window: QMainWindow, handler: HLOC_Handler):
        self.ui = ui
        self.main_window = main_window
        self.handler = handler
        self.__connect_buttons()

    def __connect_buttons(self):
        self.connect_button(
            # SET IMAGES DIRECTORY
            self.ui.pushButton_imagesDirectoryChoose,
            self.__on_images_directory_choose_clicked,
        )
        self.connect_button(
            # SET SECOND IMAGES DIRECTORY (STEREO MODE)
            self.ui.pushButton_setSecondCameraProcessingImagesDirectory,
            self.__on_set_second_camera_processing_images_directory_clicked,
        )

    def __on_images_directory_choose_clicked(self):
        images_directory = QFileDialog.getExistingDirectory(
            self.main_window, "Выберите директорию с изображениями"
        )
        if images_directory and os.path.isdir(images_directory):
            self.ui.lineEdit_imagesDirectoryField.setText(images_directory)

    def __on_set_second_camera_processing_images_directory_clicked(self):
        images_directory = QFileDialog.getExistingDirectory(
            self.main_window, "Выберите директорию с изображениями второй камеры"
        )
        if images_directory and os.path.isdir(images_directory):
            self.ui.lineEdit_secondCameraProcessingImagesDirectory.setText(
                images_directory
            )
