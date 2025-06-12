from abc import abstractmethod
from typing import Callable, Union
from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget

from ui.forms.ui_form import Ui_Widget


class AbstractWindow(QMainWindow):
    def __init__(self, ui: Ui_Widget):
        self.ui = ui


class AbstractGUIManager:
    def __init__(self, window: QWidget):
        self.window: AbstractWindow = window

    @abstractmethod
    def __connect_buttons(self) -> None:
        pass

    def connect_button(
        self, button: QPushButton, target: Union[QWidget, Callable]
    ) -> None:
        """Метод для связки навигационных кнопок и целевых виджетов."""
        if not button or not target:
            return

        if callable(target):
            button.clicked.connect(target)
        elif isinstance(target, QWidget):
            if sw := getattr(self.window.ui, "stackedWidget_workSpace", None):
                button.clicked.connect(lambda: sw.setCurrentWidget(target))
