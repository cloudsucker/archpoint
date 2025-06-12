import os

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QPointF, Signal
from PySide6.QtWidgets import (
    QFileDialog,
    QLayout,
    QTableWidgetItem,
    QGraphicsScene,
    QTableWidget,
    QLineEdit,
    QInputDialog,
    QHeaderView,
    QMessageBox,
)
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtGui import QDoubleValidator

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
        self.dots_table = self.window.ui.tableWidget_imageDotsCreator_DotsData
        self.real_coords_table = self.window.ui.tableWidget_imageDotsAndRealCoordinates
        self.redo_stack = []
        self._drag_start_pos = None

        self.__initialize_dots_creator_table()
        self.__initialize_real_coords_table()
        self.__replace_graphic_view_on_custom()
        self.__connect_buttons()

    def preprocess_dots_creator_page(self, images_handler: RoomImagesHandler) -> None:
        """Подготовка страницы разметки калибровочных изображений."""
        self.images_handler = images_handler
        self.current_image = self.images_handler.get_current_image()
        self.update()

    def __replace_graphic_view_on_custom(self) -> None:
        """Замена графического представления на кастомное."""
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
        self.dots_table.cellClicked.connect(self.__on_dots_table_cell_clicked)
        self.dots_table.itemChanged.connect(self.__on_dots_table_item_changed)
        self.real_coords_table.cellClicked.connect(
            self.__on_real_coords_table_cell_clicked
        )
        self.real_coords_table.itemChanged.connect(
            self.__on_real_coords_table_item_changed
        )

    def update(self) -> None:
        """Глобальное обновление интерфейса работы с точками."""
        self.__render_current_image()
        self.__show_current_image_name()
        self.__update_dots_creator_table()
        self.__update_real_coords_table()
        self.window.ui.pushButton_goToSettingRealCoordinates.setEnabled(
            self.are_all_images_dots_set()
        )

        if self.are_real_coordinates_completed():
            self.window.ui.pushButton_startCalibrationProcessFromSettingRealCoordinates.setEnabled(
                True
            )
        else:
            self.window.ui.pushButton_startCalibrationProcessFromSettingRealCoordinates.setEnabled(
                False
            )

    def are_all_images_dots_set(self) -> bool:
        """Проверка, все ли точки на изображениях установлены."""
        return self.images_handler.are_all_image_dots_set()

    def are_real_coordinates_completed(self) -> bool:
        """Проверка, все ли реальные координаты заполнены."""
        return self.images_handler.are_all_real_coordinates_completed()

    def __render_current_image(self):
        """Рендеринг текущего изображения."""
        current_transform = self.view.transform()
        current_scroll_x = self.view.horizontalScrollBar().value()
        current_scroll_y = self.view.verticalScrollBar().value()

        self.scene.clear()
        self.view._point_items.clear()
        self.view._text_items.clear()
        self.__current_image_pixmap = QPixmap(self.current_image.image_path)
        pixmap_item = QGraphicsPixmapItem(self.__current_image_pixmap)
        self.scene.addItem(pixmap_item)

        self.view.setTransform(current_transform)
        self.view.horizontalScrollBar().setValue(current_scroll_x)
        self.view.verticalScrollBar().setValue(current_scroll_y)
        self.view._current_zoom = current_transform.m11()
        self.view.update_point_sizes()

        for dot_id, (x, y) in self.current_image.image_points.items():
            if x is not None and y is not None:
                self.view.add_point_item(dot_id, x, y)

    def __show_current_image_name(self):
        """Отображение имени текущего изображения."""
        self.window.ui.label_imageDotsCreator_ImageName.setText(
            self.current_image.image_name
        )

    def __initialize_dots_creator_table(self):
        """Инициализация таблицы точек."""
        self.dots_table.setRowCount(0)
        self.dots_table.setColumnCount(3)
        self.dots_table.setHorizontalHeaderLabels(["ID", "X", "Y"])
        self.dots_table.setSelectionMode(QTableWidget.SingleSelection)
        self.dots_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.dots_table.setEditTriggers(QTableWidget.DoubleClicked)
        self.dots_table.setFocusPolicy(Qt.StrongFocus)
        self.dots_table.keyPressEvent = self.__on_dots_table_key_press
        self.dots_table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.dots_table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.dots_table.setFixedWidth(280)
        self.dots_table.verticalHeader().setFixedWidth(30)
        self.dots_table.setColumnWidth(0, 70)
        self.dots_table.setColumnWidth(1, 90)
        self.dots_table.setColumnWidth(2, 90)

    def __initialize_real_coords_table(self):
        """Инициализация таблицы реальных координат."""
        self.real_coords_table.setRowCount(0)
        self.real_coords_table.setColumnCount(4)
        self.real_coords_table.setHorizontalHeaderLabels(
            ["ID", "REAL X", "REAL Y", "REAL Z"]
        )
        self.real_coords_table.setSelectionMode(QTableWidget.SingleSelection)
        self.real_coords_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.real_coords_table.setEditTriggers(
            QTableWidget.DoubleClicked | QTableWidget.AnyKeyPressed
        )
        self.real_coords_table.setFocusPolicy(Qt.StrongFocus)
        self.real_coords_table.keyPressEvent = self.__on_real_coords_table_key_press
        self.real_coords_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Fixed
        )
        self.real_coords_table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.real_coords_table.setFixedWidth(800)
        self.real_coords_table.setColumnWidth(0, 200)
        self.real_coords_table.setColumnWidth(1, 200)
        self.real_coords_table.setColumnWidth(2, 200)
        self.real_coords_table.setColumnWidth(3, 200)
        self.real_coords_table.setSortingEnabled(True)

    def __update_dots_creator_table(self):
        """Обновление таблицы точек."""
        points = self.current_image.image_points
        self.dots_table.blockSignals(True)
        self.dots_table.setRowCount(0)
        self.dots_table.setColumnCount(3)
        self.dots_table.setHorizontalHeaderLabels(["ID", "X", "Y"])

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

            self.dots_table.insertRow(row)
            id_item = QTableWidgetItem(str(dot_name))
            id_item.setData(Qt.UserRole, str(dot_name))
            id_item.setFlags(id_item.flags() | Qt.ItemIsEditable)
            self.dots_table.setItem(row, 0, id_item)
            x_item = QTableWidgetItem(f"{dot_data[0]:.3f}")
            x_item.setFlags(x_item.flags() | Qt.ItemIsEditable)
            self.dots_table.setItem(row, 1, x_item)
            y_item = QTableWidgetItem(f"{dot_data[1]:.3f}")
            y_item.setFlags(y_item.flags() | Qt.ItemIsEditable)
            self.dots_table.setItem(row, 2, y_item)
            row += 1

        self.dots_table.blockSignals(False)

    def __update_real_coords_table(self):
        """Обновление таблицы реальных координат."""
        if not self.images_handler:
            return

        self.real_coords_table.blockSignals(True)
        self.real_coords_table.setRowCount(0)
        self.real_coords_table.setColumnCount(4)
        self.real_coords_table.setHorizontalHeaderLabels(
            ["ID", "REAL X", "REAL Y", "REAL Z"]
        )

        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)

        unique_ids = sorted(self.images_handler.unique_ids, key=self.__safe_int)
        self.real_coords_table.setRowCount(len(unique_ids))

        for row, id_value in enumerate(unique_ids):
            id_item = QTableWidgetItem(str(id_value))
            id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)
            self.real_coords_table.setItem(row, 0, id_item)

            coords = self.images_handler.get_dot_real_coordinates(id_value) or (
                0.0,
                0.0,
                0.0,
            )
            x_item = QTableWidgetItem(f"{coords[0]:.3f}" if coords[0] else "")
            y_item = QTableWidgetItem(f"{coords[1]:.3f}" if coords[1] else "")
            z_item = QTableWidgetItem(f"{coords[2]:.3f}" if coords[2] else "")
            x_item.setFlags(x_item.flags() | Qt.ItemIsEditable)
            y_item.setFlags(y_item.flags() | Qt.ItemIsEditable)
            z_item.setFlags(z_item.flags() | Qt.ItemIsEditable)
            self.real_coords_table.setItem(row, 1, x_item)
            self.real_coords_table.setItem(row, 2, y_item)
            self.real_coords_table.setItem(row, 3, z_item)

        self.real_coords_table.blockSignals(False)

    def __connect_buttons(self):
        """Подключение кнопок."""
        self.connect_button(
            self.window.ui.pushButton_imageDotsCreator_getNextImage,
            self.__on_get_next_image_clicked,
        )
        self.connect_button(
            self.window.ui.pushButton_imageDotsCreator_getPreviousImage,
            self.__on_get_previous_image_clicked,
        )
        self.connect_button(
            self.window.ui.pushButton_goToSettingRealCoordinates,
            self.__on_go_to_setting_real_coordinates_clicked,
        )
        self.connect_button(
            self.window.ui.pushButton_returnToDotsCreator,
            self.__on_return_to_dots_creator_clicked,
        )
        self.connect_button(
            self.window.ui.pushButton_loadRealCoordinatesFromFile,
            self.__on_load_real_coords_from_file_clicked,
        )

    def __is_dot_valid(self, x: float, y: float) -> bool:
        """Проверка валидности координат точки."""
        return (
            0 <= x <= self.__current_image_pixmap.width()
            and 0 <= y <= self.__current_image_pixmap.height()
        )

    def __safe_int(self, x):
        """Безопасное преобразование в int."""
        try:
            return int(x)
        except ValueError:
            return float("inf")

    def __on_get_next_image_clicked(self):
        """Обработка перехода к следующему изображению."""
        if next_image := self.images_handler.get_next_image():
            self.current_image = next_image
            self.redo_stack.clear()
            self.view.deselect_point()
            self.update()

    def __on_get_previous_image_clicked(self):
        """Обработка перехода к предыдущему изображению."""
        if previous_image := self.images_handler.get_previous_image():
            self.current_image = previous_image
            self.redo_stack.clear()
            self.view.deselect_point()
            self.update()

    def __on_go_to_setting_real_coordinates_clicked(self):
        """Обработка перехода к настройке реальных координат."""
        if not self.are_all_images_dots_set():
            QMessageBox.critical(
                self.window,
                "Ошибка",
                "Завершите разметку изображений для перехода к следующему этапу.",
            )
            return
        self.window.ui.stackedWidget_workSpace.setCurrentWidget(
            self.window.ui.page_calibrationSteps_5_ImageDotsCreating_SetCoords
        )
        self.__update_real_coords_table()

    def __on_return_to_dots_creator_clicked(self):
        """Обработка возврата к разметке точек."""
        self.window.ui.stackedWidget_workSpace.setCurrentWidget(
            self.window.ui.page_calibrationSteps_5_ImageDotsCreating
        )

    def __generate_unique_id(self) -> str:
        """Генерация уникального ID."""
        existing_ids = set(self.current_image.image_points.keys())
        i = 1
        while str(i) in existing_ids:
            i += 1
        return str(i)

    def __on_point_clicked(self, pos: QPointF):
        """Обработка клика по точке."""
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
        """Обработка выбора точки."""
        self.view.select_point(point_id)
        for row in range(self.dots_table.rowCount()):
            if self.dots_table.item(row, 0).text() == point_id:
                self.dots_table.selectRow(row)
                break

    def __on_point_moved(self, point_id: str, pos: QPointF):
        """Обработка перемещения точки."""
        if self.current_image and self.__is_dot_valid(pos.x(), pos.y()):
            if self._drag_start_pos is None:
                self._drag_start_pos = self.current_image.image_points.get(point_id)
            self.current_image.image_points[point_id] = (pos.x(), pos.y())
            self.view.update_point_position(point_id, pos.x(), pos.y())
            self.__update_dots_creator_table()

    def __on_point_moved_finished(self, point_id: str, pos: QPointF):
        """Обработка завершения перемещения точки."""
        if self.current_image and self.__is_dot_valid(pos.x(), pos.y()):
            if self._drag_start_pos is not None:
                self.current_image.edit_point(point_id, (pos.x(), pos.y()))
                self._drag_start_pos = None
            self.__update_dots_creator_table()

    def __on_point_removed(self, point_id: str):
        """Обработка удаления точки."""
        if self.current_image:
            self.current_image.remove_point(point_id)
            self.view.remove_point_item(point_id)
            self.redo_stack.clear()
            self.update()

    def __on_point_id_changed(self, old_id: str, new_id: str):
        """Обработка изменения ID точки."""
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

    def __on_dots_table_item_changed(self, item: QTableWidgetItem):
        """Обработка изменения ячейки таблицы точек."""
        if self.current_image is None:
            return

        row = item.row()
        column = item.column()
        old_id = item.data(Qt.UserRole) or self.dots_table.item(row, 0).text().strip()

        if not old_id:
            return

        self.dots_table.blockSignals(True)
        try:
            if column == 0:  # ID change
                new_id = item.text().strip()
                if new_id and new_id != old_id:
                    try:
                        self.current_image.edit_point_id(old_id, new_id)
                        self.view.remove_point_item(old_id)
                        self.view.add_point_item(
                            new_id, *self.current_image.image_points[new_id]
                        )
                        self.dots_table.item(row, 0).setData(Qt.UserRole, new_id)
                    except (InvalidDotId, DotWithTheSameIdAlreadyExists):
                        item.setText(old_id)
                else:
                    item.setText(old_id)
            else:  # Coordinates change
                try:
                    x = float(self.dots_table.item(row, 1).text())
                    y = float(self.dots_table.item(row, 2).text())
                    if self.__is_dot_valid(x, y):
                        self.current_image.edit_point(old_id, (x, y))
                        self.view.update_point_position(old_id, x, y)
                    else:
                        old_point = self.current_image.image_points.get(old_id, (0, 0))
                        self.dots_table.item(row, 1).setText(f"{old_point[0]:.3f}")
                        self.dots_table.item(row, 2).setText(f"{old_point[1]:.3f}")
                except ValueError:
                    old_point = self.current_image.image_points.get(old_id, (0, 0))
                    self.dots_table.item(row, 1).setText(f"{old_point[0]:.3f}")
                    self.dots_table.item(row, 2).setText(f"{old_point[1]:.3f}")
        finally:
            self.dots_table.blockSignals(False)

    def __on_dots_table_cell_clicked(self, row: int, column: int):
        """Обработка клика по ячейке таблицы точек."""
        point_id = self.dots_table.item(row, 0).text()
        self.view.select_point(point_id)

    def __on_dots_table_key_press(self, event):
        """Обработка нажатия клавиши в таблице точек."""
        if event.key() == Qt.Key_Delete:
            if selected_indexes := self.dots_table.selectedIndexes():
                row = selected_indexes[0].row()
                point_id = self.dots_table.item(row, 0).text()
                self.__on_point_removed(point_id)
        else:
            QTableWidget.keyPressEvent(self.dots_table, event)

    def __on_real_coords_table_item_changed(self, item: QTableWidgetItem):
        """Обработка изменения ячейки таблицы реальных координат."""
        row = item.row()
        column = item.column()
        id_value = self.real_coords_table.item(row, 0).text()

        if column == 0:  # ID is not editable
            return

        self.real_coords_table.blockSignals(True)
        try:
            x_text = self.real_coords_table.item(row, 1).text() or "0.0"
            y_text = self.real_coords_table.item(row, 2).text() or "0.0"
            z_text = self.real_coords_table.item(row, 3).text() or "0.0"

            try:
                x = float(x_text) if x_text.strip() else 0.0
                y = float(y_text) if y_text.strip() else 0.0
                z = float(z_text) if z_text.strip() else 0.0
                self.images_handler.set_dot_real_coordinates(id_value, (x, y, z))
            except ValueError:
                coords = self.images_handler.get_dot_real_coordinates(id_value) or (
                    0.0,
                    0.0,
                    0.0,
                )
                self.real_coords_table.item(row, 1).setText(
                    f"{coords[0]:.3f}" if coords[0] else ""
                )
                self.real_coords_table.item(row, 2).setText(
                    f"{coords[1]:.3f}" if coords[1] else ""
                )
                self.real_coords_table.item(row, 3).setText(
                    f"{coords[2]:.3f}" if coords[2] else ""
                )
        finally:
            self.real_coords_table.blockSignals(False)

    def __on_real_coords_table_cell_clicked(self, row: int, column: int):
        """Обработка клика по ячейке таблицы реальных координат."""
        # Выделение строки при клике
        self.real_coords_table.selectRow(row)

    def __on_load_real_coords_from_file_clicked(self):
        """Обработка нажатия на кнопку загрузки реальных координат из файла."""
        real_coords_file_path, _ = QFileDialog.getOpenFileName(
            self.window,
            "Выберите файл внутренних координат точек",
            "",
            "Текстовые файлы (*.txt *.TXT *.csv *.CSV)",
        )

        if not real_coords_file_path:
            return

        if not os.path.exists(real_coords_file_path):
            QMessageBox.critical(
                self.window,
                "Ошибка",
                f"Файл '{real_coords_file_path}' не существует.",
            )
            return

        self.images_handler.load_dots_real_coords_from_file(real_coords_file_path)
        self.update()

    def __on_real_coords_table_key_press(self, event):
        """Обработка нажатия клавиши в таблице реальных координат."""
        if event.key() == Qt.Key_Delete:
            selected_indexes = self.real_coords_table.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                id_value = self.real_coords_table.item(row, 0).text()
                self.images_handler.set_dot_real_coordinates(id_value, (0.0, 0.0, 0.0))
                self.__update_real_coords_table()
        else:
            QTableWidget.keyPressEvent(self.real_coords_table, event)

    def __on_undo(self):
        """Обработка отмены действия."""
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
        """Обработка повтора действия."""
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

    def preprocess_real_coordinates_setter_page(self) -> None:
        """Подготовка страницы установки реальных координат."""
        self.__update_real_coords_table()
