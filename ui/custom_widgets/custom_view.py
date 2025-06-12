from PySide6.QtCore import Qt, Signal, QPoint, QPointF
from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsEllipseItem,
    QMenu,
)
from PySide6.QtGui import (
    QWheelEvent,
    QMouseEvent,
    QKeyEvent,
    QPen,
    QBrush,
    QColor,
    QFont,
)


class CustomGraphicsView(QGraphicsView):
    point_clicked = Signal(QPointF)
    point_selected = Signal(str)
    point_moved = Signal(str, QPointF)
    point_moved_finished = Signal(str, QPointF)
    point_removed = Signal(str)
    point_id_changed = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._zoom_factor = 1.2
        self._base_point_size = 10
        self._base_font_size = 13
        self._current_zoom = 1.0
        self._min_font_size = 3
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.NoDrag)
        self.setInteractive(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self._is_panning = False
        self._pan_start_pos = None
        self._is_dragging = False
        self._selected_point_id = None
        self._drag_start_pos = None
        self._point_items = {}
        self._text_items = {}
        self._last_click_time = 0
        self._double_click_threshold = 300

    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.modifiers() == Qt.ControlModifier:
            if event.angleDelta().y() > 0:
                zoom = self._zoom_factor

            else:
                zoom = 1 / self._zoom_factor

            self._current_zoom *= zoom
            self.scale(zoom, zoom)
            self.update_point_sizes()

        else:
            super().wheelEvent(event)

    def update_point_sizes(self) -> None:
        for point_id, item in self._point_items.items():
            center_x = item.rect().center().x()
            center_y = item.rect().center().y()

            size = self._base_point_size / self._current_zoom
            item.setRect(center_x - size / 2, center_y - size / 2, size, size)

            if point_id in self._text_items:
                font = self._text_items[point_id].font()
                font.setPixelSize(
                    max(
                        self._min_font_size,
                        int(self._base_font_size / self._current_zoom),
                    )
                )
                self._text_items[point_id].setFont(font)
                self._text_items[point_id].setPos(
                    center_x + 5 / self._current_zoom,
                    center_y - 10 / self._current_zoom,
                )

    def mousePressEvent(self, event: QMouseEvent):
        scene_pos = self.mapToScene(event.pos())

        if event.button() == Qt.LeftButton:
            item = self.itemAt(event.pos())

            if isinstance(item, QGraphicsEllipseItem):
                point_id = None

                for pid, pitem in self._point_items.items():
                    if pitem == item:
                        point_id = pid
                        break

                if point_id and self._selected_point_id == point_id:
                    self._is_dragging = True
                    self._drag_start_pos = scene_pos

            else:
                if self._selected_point_id:
                    self.deselect_point()

                else:
                    self.point_clicked.emit(scene_pos)

        elif event.button() == Qt.MiddleButton:
            self._is_panning = True
            self._pan_start_pos = event.pos()
            self.setCursor(Qt.ClosedHandCursor)

        elif event.button() == Qt.RightButton:
            item = self.itemAt(event.pos())

            if isinstance(item, QGraphicsEllipseItem):
                point_id = None

                for pid, pitem in self._point_items.items():
                    if pitem == item:
                        point_id = pid
                        break

                if point_id:
                    self.select_point(point_id)
                    self.point_selected.emit(point_id)
                    self.__show_context_menu(point_id, event.pos())

        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            item = self.itemAt(event.pos())

            if isinstance(item, QGraphicsEllipseItem):
                point_id = None

                for pid, pitem in self._point_items.items():
                    if pitem == item:
                        point_id = pid
                        break

                if point_id:
                    self.select_point(point_id)
                    self.point_selected.emit(point_id)

        super().mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        scene_pos = self.mapToScene(event.pos())

        if self._is_panning and self._pan_start_pos:
            delta = event.pos() - self._pan_start_pos
            self._pan_start_pos = event.pos()

            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta.x()
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta.y()
            )

        elif self._is_dragging and self._selected_point_id:
            self.point_moved.emit(self._selected_point_id, scene_pos)

        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self._is_panning = False
            self.setCursor(Qt.ArrowCursor)

        elif event.button() == Qt.LeftButton and self._is_dragging:
            self._is_dragging = False
            scene_pos = self.mapToScene(event.pos())

            if self._selected_point_id:
                self.point_moved_finished.emit(self._selected_point_id, scene_pos)

            self._drag_start_pos = None

        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Z and event.modifiers() == Qt.ControlModifier:
            self.undo_action()

        elif event.key() == Qt.Key_Z and event.modifiers() == (
            Qt.ControlModifier | Qt.ShiftModifier
        ):
            self.redo_action()

        elif event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            self.deselect_point()
        super().keyPressEvent(event)

    def undo_action(self) -> None:
        self.scene().undo_action.emit()

    def redo_action(self) -> None:
        self.scene().redo_action.emit()

    def select_point(self, point_id: str) -> None:
        if self._selected_point_id and self._selected_point_id in self._point_items:
            self._point_items[self._selected_point_id].setBrush(QBrush(QColor("red")))

        self._selected_point_id = point_id
        if point_id in self._point_items:
            self._point_items[point_id].setBrush(QBrush(QColor("blue")))
            self._is_dragging = False

    def deselect_point(self) -> None:
        if self._selected_point_id and self._selected_point_id in self._point_items:
            self._point_items[self._selected_point_id].setBrush(QBrush(QColor("red")))

        self._selected_point_id = None
        self._is_dragging = False

    def add_point_item(self, point_id: str, x: float, y: float) -> None:
        size = self._base_point_size / self._current_zoom
        pen = QPen(QColor("black"), 2 / self._current_zoom)

        item = self.scene().addEllipse(
            x - size / 2,
            y - size / 2,
            size,
            size,
            pen=pen,
            brush=QBrush(QColor("red")),
        )

        self._point_items[point_id] = item
        text = self.scene().addText(point_id)
        font = QFont()
        font.setPixelSize(
            max(self._min_font_size, int(self._base_font_size / self._current_zoom))
        )
        font.setBold(True)
        text.setFont(font)
        text.setPos(x + 5 / self._current_zoom, y - 10 / self._current_zoom)
        self._text_items[point_id] = text

    def update_point_position(self, point_id: str, x: float, y: float) -> None:
        if point_id in self._point_items:
            size = self._base_point_size / self._current_zoom
            pen = QPen(QColor("black"), 2 / self._current_zoom)
            self._point_items[point_id].setRect(x - size / 2, y - size / 2, size, size)
            self._point_items[point_id].setPen(pen)

            if point_id in self._text_items:
                font = self._text_items[point_id].font()
                font.setPixelSize(
                    max(
                        self._min_font_size,
                        int(self._base_font_size / self._current_zoom),
                    )
                )
                font.setBold(True)
                self._text_items[point_id].setFont(font)
                self._text_items[point_id].setPos(
                    x + 5 / self._current_zoom, y - 10 / self._current_zoom
                )

    def remove_point_item(self, point_id: str) -> None:
        if point_id in self._point_items:
            self.scene().removeItem(self._point_items[point_id])
            del self._point_items[point_id]

        if point_id in self._text_items:
            self.scene().removeItem(self._text_items[point_id])
            del self._text_items[point_id]

    def __show_context_menu(self, point_id: str, pos: QPoint) -> None:
        menu = QMenu(self)
        delete_action = menu.addAction("Удалить")
        change_id_action = menu.addAction("Изменить ID")
        action = menu.exec_(self.mapToGlobal(pos))

        if action == delete_action:
            self.point_removed.emit(point_id)

        elif action == change_id_action:
            self.point_id_changed.emit(point_id, "")
