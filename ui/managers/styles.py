import os

from PySide6.QtWidgets import QMessageBox

from ui.managers import AbstractWindow


class StylesManager:
    def __init__(self, window: AbstractWindow):
        self.window = window
        self.theme = "dark"
        self.__apply_styles()
        self.window.adjustSize()

    def switch_theme(self) -> None:
        self.theme = "dark" if self.theme == "light" else "light"
        self.__apply_styles()

    def __apply_styles(self) -> None:
        path = f"static/styles/{self.theme}.qss"

        if not os.path.exists(path):
            QMessageBox.critical(
                self.window,
                "Ошибка",
                f"Файл стилей {path} не найден.",
            )
            return

        with open(path, "r") as f:
            self.window.window().setStyleSheet(f.read())
