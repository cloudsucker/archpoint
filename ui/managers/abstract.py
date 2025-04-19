from abc import abstractmethod
from typing import Callable, Union
from PySide6.QtWidgets import QPushButton, QWidget

from ui.forms.ui_form import Ui_Widget


class AbstractGUIManager:
    def __init__(self, ui: Ui_Widget, main_window: QWidget):
        self.main_window = main_window
        self.ui = ui

    @abstractmethod
    def __connect_buttons(self):
        pass

    def connect_button(self, button: QPushButton, target: Union[QWidget, Callable]):
        """Метод для связки навигационных кнопок и целевых виджетов."""
        if not button or not target:
            return

        if callable(target):
            button.clicked.connect(target)
        elif isinstance(target, QWidget):
            sw = getattr(self.ui, "stackedWidget_workSpace", None)
            if sw:
                button.clicked.connect(lambda: sw.setCurrentWidget(target))
