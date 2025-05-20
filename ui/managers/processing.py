import os

from PySide6.QtWidgets import QFileDialog

from ui.managers import AbstractWindow, AbstractGUIManager
from archpoint.handlers import HLOC_Handler


class ProcessingManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow, handler: HLOC_Handler):
        self.window = window
        self.handler = handler
        self.__connect_buttons()

    def __connect_buttons(self):
        self.connect_button(
            # SET IMAGES DIRECTORY
            self.window.ui.pushButton_imagesDirectoryChoose,
            self.__on_images_directory_choose_clicked,
        )
        self.connect_button(
            # SET SECOND IMAGES DIRECTORY (STEREO MODE)
            self.window.ui.pushButton_setSecondCameraProcessingImagesDirectory,
            self.__on_set_second_camera_processing_images_directory_clicked,
        )

    def __on_images_directory_choose_clicked(self):
        images_directory = QFileDialog.getExistingDirectory(
            self.window, "Выберите директорию с изображениями"
        )
        if images_directory and os.path.isdir(images_directory):
            self.window.ui.lineEdit_imagesDirectoryField.setText(images_directory)

    def __on_set_second_camera_processing_images_directory_clicked(self):
        images_directory = QFileDialog.getExistingDirectory(
            self.window, "Выберите директорию с изображениями второй камеры"
        )
        if images_directory and os.path.isdir(images_directory):
            self.window.ui.lineEdit_secondCameraProcessingImagesDirectory.setText(
                images_directory
            )
