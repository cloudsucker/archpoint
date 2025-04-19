from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsPixmapItem,
)

from archpoint.calibration_methods.room import RoomImagesHandler, RoomImageDotsEditor

from ui.forms.ui_form import Ui_Widget
from ui.managers.abstract import AbstractGUIManager


class DotsCreatorManager(AbstractGUIManager):
    def __init__(self, ui: Ui_Widget, main_window: QMainWindow):
        self.ui = ui
        self.main_window = main_window
        self.images_handler: RoomImagesHandler | None = None
        self.current_image: RoomImageDotsEditor | None = None

        self.view: QGraphicsView = self.ui.graphicsView_imageDotsCreator_ImagePreview
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.__connect_buttons()

    def preprocess_dots_creator_page(self, images_handler: RoomImagesHandler) -> None:
        self.images_handler = images_handler
        self.current_image = self.images_handler.get_current_image()
        self.update()

    def update(self):
        self.__render_current_image()
        self.__show_current_image_name()

    def is_completed(self) -> bool:
        return self.images_handler.is_completed()

    def __render_current_image(self):
        self.scene.clear()
        pixmap = QPixmap(self.current_image.image_path)
        self.scene.addItem(QGraphicsPixmapItem(pixmap))
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def __show_current_image_name(self):
        self.ui.label_imageDotsCreator_ImageName.setText(self.current_image.image_name)

    def __connect_buttons(self):
        # NEXT IMAGE
        self.ui.pushButton_imageDotsCreator_getNextImage.clicked.connect(
            self.__on_get_next_image_clicked
        )
        # PREVIOUS IMAGE
        self.ui.pushButton_imageDotsCreator_getPreviousImage.clicked.connect(
            self.__on_get_previous_image_clicked
        )

    def __on_get_next_image_clicked(self):
        next_image = self.images_handler.get_next_image()
        if next_image:
            self.current_image = next_image
            self.update()

    def __on_get_previous_image_clicked(self):
        previous_image = self.images_handler.get_previous_image()
        if previous_image:
            self.current_image = previous_image
            self.update()
