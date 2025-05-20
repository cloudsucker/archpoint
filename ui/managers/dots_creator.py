from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QPointF
from PySide6.QtWidgets import QLayout, QTableWidgetItem
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem

from archpoint.calibration_methods.room import RoomImagesHandler, RoomImageDotsEditor

from ui.custom_widgets.custom_view import CustomGraphicsView
from ui.managers.abstract import AbstractWindow, AbstractGUIManager


class DotsCreatorManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow):
        self.window: AbstractWindow = window
        self.images_handler: RoomImagesHandler | None = None
        self.current_image: RoomImageDotsEditor | None = None

        self.__current_image_pixmap: QPixmap | None = None
        self.__initialize_dots_table()
        self.__replace_graphic_view_on_custom()
        self.__connect_buttons()

    def preprocess_dots_creator_page(self, images_handler: RoomImagesHandler) -> None:
        self.images_handler = images_handler
        self.current_image = self.images_handler.get_current_image()
        self.update()

    def __replace_graphic_view_on_custom(self) -> None:
        original_view = self.window.ui.graphicsView_imageDotsCreator_ImagePreview
        parent_layout: QLayout = original_view.parentWidget().layout()

        self.view = CustomGraphicsView()
        self.view.setObjectName(original_view.objectName())

        index = parent_layout.indexOf(original_view)
        parent_layout.removeWidget(original_view)
        original_view.deleteLater()
        parent_layout.insertWidget(index, self.view)

        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.view.point_clicked.connect(self.__on_point_clicked)

    def update(self) -> None:
        self.__render_current_image()
        self.__show_current_image_name()
        self.__update_dots_table()

    def is_completed(self) -> bool:
        return self.images_handler.is_completed()

    def __render_current_image(self):
        self.scene.clear()
        self.__current_image_pixmap = QPixmap(self.current_image.image_path)
        self.scene.addItem(QGraphicsPixmapItem(self.__current_image_pixmap))
        self.scene.setSceneRect(self.__current_image_pixmap.rect())

        # Отрисовка точек
        for dot_id, (x, y) in self.current_image.image_points.items():
            self.scene.addEllipse(x - 3, y - 3, 6, 6, brush=Qt.red)
            text = self.scene.addText(dot_id)
            text.setPos(x + 5, y - 10)

    def __show_current_image_name(self):
        self.window.ui.label_imageDotsCreator_ImageName.setText(
            self.current_image.image_name
        )

    def __initialize_dots_table(self):
        self.window.ui.tableWidget_imageDotsCreator_DotsData.setRowCount(0)
        self.window.ui.tableWidget_imageDotsCreator_DotsData.setColumnCount(3)
        self.window.ui.tableWidget_imageDotsCreator_DotsData.setHorizontalHeaderLabels(
            ["ID", "X", "Y"]
        )

    def __update_dots_table(self):
        points = self.current_image.image_points
        self.window.ui.tableWidget_imageDotsCreator_DotsData.setRowCount(len(points))
        self.window.ui.tableWidget_imageDotsCreator_DotsData.setColumnCount(3)
        self.window.ui.tableWidget_imageDotsCreator_DotsData.setHorizontalHeaderLabels(
            ["ID", "X", "Y"]
        )

        for row, (dot_name, dot_data) in enumerate(points.items()):
            self.window.ui.tableWidget_imageDotsCreator_DotsData.setItem(
                row, 0, QTableWidgetItem(dot_name)
            )
            self.window.ui.tableWidget_imageDotsCreator_DotsData.setItem(
                row, 1, QTableWidgetItem(str(dot_data[0]))
            )
            self.window.ui.tableWidget_imageDotsCreator_DotsData.setItem(
                row, 2, QTableWidgetItem(str(dot_data[1]))
            )

        self.window.ui.tableWidget_imageDotsCreator_DotsData.resizeColumnsToContents()
        self.window.ui.tableWidget_imageDotsCreator_DotsData.resizeRowsToContents()

    def __connect_buttons(self):
        self.connect_button(
            # NEXT IMAGE
            self.window.ui.pushButton_imageDotsCreator_getNextImage,
            self.__on_get_next_image_clicked,
        )
        self.connect_button(
            # PREVIOUS IMAGE
            self.window.ui.pushButton_imageDotsCreator_getPreviousImage,
            self.__on_get_previous_image_clicked,
        )

    def __is_dot_valid(self, x: float, y: float) -> bool:
        return (
            0 <= x <= self.__current_image_pixmap.width()
            and 0 <= y <= self.__current_image_pixmap.height()
        )

    def __on_get_next_image_clicked(self):
        if next_image := self.images_handler.get_next_image():
            self.current_image = next_image
            self.update()

    def __on_get_previous_image_clicked(self):
        if previous_image := self.images_handler.get_previous_image():
            self.current_image = previous_image
            self.update()

    def __on_point_clicked(self, pos: QPointF):
        if self.current_image is None:
            return

        dot_id = str(len(self.current_image.image_points) + 1)
        dot_x = float(pos.x())
        dot_y = float(pos.y())

        if self.__is_dot_valid(dot_x, dot_y):
            self.current_image.add_point(dot_id, (dot_x, dot_y))
            self.update()
