from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QPointF, Signal
from PySide6.QtWidgets import (
    QLayout,
    QTableWidgetItem,
    QGraphicsScene,
    QTableWidget,
    QLineEdit,
    QInputDialog,
)
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtGui import QDoubleValidator, QTransform

from archpoint.calibration_methods.room import (
    RoomImagesHandler,
    RoomImageDotsEditor,
    InvalidDotId,
    DotWithTheSameIdAlreadyExists,
)

from ui.custom_widgets.custom_view import CustomGraphicsView
from ui.managers import AbstractWindow, AbstractGUIManager


class CustomGraphicsScene(QGraphicsScene):
    undo_action = Signal()
    redo_action = Signal()


class DotsCreatorManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow):
        super().__init__(window)
        self.window: AbstractWindow = window
        self.images_handler: RoomImagesHandler | None = None
        self.current_image: RoomImageDotsEditor | None = None
        self.__current_image_pixmap: QPixmap | None = None
        self.__initialize_dots_table()
        self.__replace_graphic_view_on_custom()
        self.__connect_buttons()
        self.redo_stack = []
        self._drag_start_pos = None

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

        self.scene = CustomGraphicsScene()
        self.view.setScene(self.scene)

        self.view.point_clicked.connect(self.__on_point_clicked)
        self.view.point_selected.connect(self.__on_point_selected)
        self.view.point_moved.connect(self.__on_point_moved)
        self.view.point_moved_finished.connect(self.__on_point_moved_finished)
        self.view.point_removed.connect(self.__on_point_removed)
        self.view.point_id_changed.connect(self.__on_point_id_changed)
        self.scene.undo_action.connect(self.__on_undo)
        self.scene.redo_action.connect(self.__on_redo)
        self.window.ui.tableWidget_imageDotsCreator_DotsData.cellClicked.connect(
            self.__on_table_cell_clicked
        )
        self.window.ui.tableWidget_imageDotsCreator_DotsData.itemChanged.connect(
            self.__on_table_item_changed
        )

    def update(self) -> None:
        self.__render_current_image()
        self.__show_current_image_name()
        self.__update_dots_table()

    def is_completed(self) -> bool:
        return self.images_handler.is_completed()

    def __render_current_image(self):
        # Store current view transformation to preserve zoom and position
        current_transform = self.view.transform()
        current_scroll_x = self.view.horizontalScrollBar().value()
        current_scroll_y = self.view.verticalScrollBar().value()

        self.scene.clear()
        self.view._point_items.clear()
        self.view._text_items.clear()
        self.__current_image_pixmap = QPixmap(self.current_image.image_path)
        pixmap_item = QGraphicsPixmapItem(self.__current_image_pixmap)
        self.scene.addItem(pixmap_item)

        # Restore the view transformation
        self.view.setTransform(current_transform)
        self.view.horizontalScrollBar().setValue(current_scroll_x)
        self.view.verticalScrollBar().setValue(current_scroll_y)
        self.view._current_zoom = current_transform.m11()
        self.view.update_point_sizes()

        for dot_id, (x, y) in self.current_image.image_points.items():
            if x is not None and y is not None:
                self.view.add_point_item(dot_id, x, y)

    def __show_current_image_name(self):
        self.window.ui.label_imageDotsCreator_ImageName.setText(
            self.current_image.image_name
        )

    def __initialize_dots_table(self):
        table = self.window.ui.tableWidget_imageDotsCreator_DotsData
        table.setRowCount(0)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["ID", "X", "Y"])
        table.setSelectionMode(QTableWidget.SingleSelection)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setEditTriggers(QTableWidget.DoubleClicked)
        table.setFocusPolicy(Qt.StrongFocus)
        table.keyPressEvent = self.__on_table_key_press

    def __update_dots_table(self):
        points = self.current_image.image_points
        table = self.window.ui.tableWidget_imageDotsCreator_DotsData
        table.blockSignals(True)
        table.setRowCount(0)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["ID", "X", "Y"])

        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)

        row = 0
        for dot_name, dot_data in points.items():
            if (
                dot_data is None
                or not isinstance(dot_data, tuple)
                or len(dot_data) != 2
            ):
                continue

            table.insertRow(row)
            id_item = QTableWidgetItem(str(dot_name))
            id_item.setData(Qt.UserRole, str(dot_name))
            id_item.setFlags(id_item.flags() | Qt.ItemIsEditable)
            table.setItem(row, 0, id_item)
            x_item = QTableWidgetItem(f"{dot_data[0]:.2f}")
            x_item.setFlags(x_item.flags() | Qt.ItemIsEditable)
            table.setItem(row, 1, x_item)
            y_item = QTableWidgetItem(f"{dot_data[1]:.2f}")
            y_item.setFlags(y_item.flags() | Qt.ItemIsEditable)
            table.setItem(row, 2, y_item)
            row += 1

        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.blockSignals(False)

    def __connect_buttons(self):
        self.connect_button(
            self.window.ui.pushButton_imageDotsCreator_getNextImage,
            self.__on_get_next_image_clicked,
        )
        self.connect_button(
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
            self.redo_stack.clear()
            self.view.deselect_point()
            self.update()

    def __on_get_previous_image_clicked(self):
        if previous_image := self.images_handler.get_previous_image():
            self.current_image = previous_image
            self.redo_stack.clear()
            self.view.deselect_point()
            self.update()

    def __generate_unique_id(self) -> str:
        existing_ids = set(self.current_image.image_points.keys())
        i = 1

        while str(i) in existing_ids:
            i += 1

        return str(i)

    def __on_point_clicked(self, pos: QPointF):
        if self.current_image is None or self.view._selected_point_id:
            return

        dot_id = self.__generate_unique_id()
        dot_x = float(pos.x())
        dot_y = float(pos.y())

        if self.__is_dot_valid(dot_x, dot_y):
            self.current_image.add_point(dot_id, (dot_x, dot_y))
            self.redo_stack.clear()
            self.view.add_point_item(dot_id, dot_x, dot_y)
            self.update()

    def __on_point_selected(self, point_id: str):
        self.view.select_point(point_id)
        table = self.window.ui.tableWidget_imageDotsCreator_DotsData

        for row in range(table.rowCount()):
            if table.item(row, 0).text() == point_id:
                table.selectRow(row)
                break

    def __on_point_moved(self, point_id: str, pos: QPointF):
        if self.current_image and self.__is_dot_valid(pos.x(), pos.y()):
            if self._drag_start_pos is None:
                self._drag_start_pos = self.current_image.image_points.get(point_id)

            self.current_image.image_points[point_id] = (pos.x(), pos.y())
            self.view.update_point_position(point_id, pos.x(), pos.y())
            self.__update_dots_table()

    def __on_point_moved_finished(self, point_id: str, pos: QPointF):
        if self.current_image and self.__is_dot_valid(pos.x(), pos.y()):
            if self._drag_start_pos is not None:
                self.current_image.edit_point(point_id, (pos.x(), pos.y()))
                self._drag_start_pos = None
            self.__update_dots_table()

    def __on_point_removed(self, point_id: str):
        if self.current_image:
            self.current_image.remove_point(point_id)
            self.view.remove_point_item(point_id)
            self.redo_stack.clear()
            self.update()

    def __on_point_id_changed(self, old_id: str, new_id: str):
        new_id, ok = QInputDialog.getText(
            self.window,
            "Изменить ID точки",
            f"Введите новый ID для точки {old_id}:",
            QLineEdit.Normal,
            old_id,
        )
        if ok and new_id and new_id.strip() and new_id != old_id:
            try:
                self.current_image.edit_point_id(old_id, new_id.strip())
                self.view.remove_point_item(old_id)
                self.view.add_point_item(
                    new_id, *self.current_image.image_points[new_id]
                )
                self.update()

            except (InvalidDotId, DotWithTheSameIdAlreadyExists):
                pass

    def __on_table_item_changed(self, item: QTableWidgetItem):
        if self.current_image is None:
            return

        table = self.window.ui.tableWidget_imageDotsCreator_DotsData
        row = item.row()
        column = item.column()
        old_id = item.data(Qt.UserRole) or table.item(row, 0).text().strip()

        if not old_id:
            return

        table.blockSignals(True)
        try:
            # ID CHANGING
            if column == 0:
                new_id = item.text().strip()

                if new_id and new_id != old_id:
                    try:
                        self.current_image.edit_point_id(old_id, new_id)
                        self.view.remove_point_item(old_id)
                        self.view.add_point_item(
                            new_id, *self.current_image.image_points[new_id]
                        )
                        table.item(row, 0).setData(Qt.UserRole, new_id)
                    except (InvalidDotId, DotWithTheSameIdAlreadyExists) as e:
                        item.setText(old_id)
                else:
                    item.setText(old_id)

            # COORDINATES CHANGING
            else:
                try:
                    x = float(table.item(row, 1).text())
                    y = float(table.item(row, 2).text())

                    if self.__is_dot_valid(x, y):
                        self.current_image.edit_point(old_id, (x, y))
                        self.view.update_point_position(old_id, x, y)

                    else:
                        old_point = self.current_image.image_points.get(old_id, (0, 0))
                        table.item(row, 1).setText(f"{old_point[0]:.2f}")
                        table.item(row, 2).setText(f"{old_point[1]:.2f}")

                except ValueError:
                    old_point = self.current_image.image_points.get(old_id, (0, 0))
                    table.item(row, 1).setText(f"{old_point[0]:.2f}")
                    table.item(row, 2).setText(f"{old_point[1]:.2f}")

        finally:
            table.blockSignals(False)

    def __on_table_cell_clicked(self, row: int, column: int):
        table = self.window.ui.tableWidget_imageDotsCreator_DotsData
        point_id = table.item(row, 0).text()
        self.view.select_point(point_id)

    def __on_table_key_press(self, event):
        table = self.window.ui.tableWidget_imageDotsCreator_DotsData
        if event.key() == Qt.Key_Delete:
            selected_rows = table.selectedRows()
            if selected_rows:
                row = selected_rows[0]
                point_id = table.item(row, 0).text()
                self.__on_point_removed(point_id)
        else:
            QTableWidget.keyPressEvent(table, event)

    def __on_undo(self):
        if self.current_image:
            try:
                last_operation = (
                    self.current_image.history[-1]
                    if self.current_image.history
                    else None
                )
                self.current_image.undo()

                if last_operation:
                    self.redo_stack.append(last_operation)

                self.view.deselect_point()
                self.update()

            except Exception:
                pass

    def __on_redo(self):
        if self.current_image and self.redo_stack:
            operation = self.redo_stack.pop()

            if operation:
                if operation["method"] == "add":
                    if operation["id"] in self.current_image.image_points:
                        self.current_image.remove_point(operation["id"])
                    self.current_image.add_point(
                        operation["id"], operation["new_point"]
                    )

                elif operation["method"] == "edit":
                    self.current_image.edit_point(
                        operation["id"], operation["new_point"]
                    )

                elif operation["method"] == "remove":
                    self.current_image.remove_point(operation["id"])

                elif operation["method"] == "rename":
                    if operation["old_id"] and operation["new_id"]:
                        self.current_image.edit_point_id(
                            operation["new_id"], operation["old_id"]
                        )

                self.view.deselect_point()
                self.update()
