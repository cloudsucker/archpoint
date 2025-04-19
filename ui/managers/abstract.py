from abc import abstractmethod

from PySide6.QtWidgets import QPushButton, QWidget


class AbstractGUIManager:
    @abstractmethod
    def __connect_buttons(self):
        pass

    def connect_navigation_button(self, button: QPushButton, target_widget: QWidget):
        """Метод для связки навигационных кнопок и целевых виджетов."""
        if button and target_widget:
            button.clicked.connect(
                lambda: self.ui.stackedWidget_workSpace.setCurrentWidget(target_widget)
            )
