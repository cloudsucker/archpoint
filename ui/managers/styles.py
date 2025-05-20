import os

from PySide6.QtWidgets import QMainWindow, QMessageBox


class StylesManager:
    def __init__(self, window: QMainWindow):
        self.window = window
        self.theme = "light"

        self.window.adjustSize()

    def switch_theme(self) -> None:
        self.theme = "dark" if self.theme == "light" else "light"
        self.__apply_styles()

    def __apply_styles(self) -> None:
        path = f"static/styles/{self.theme}.css"

        if not os.path.exists(path):
            QMessageBox.critical(
                self.window,
                "Ошибка",
                f"Файл стилей {path} не найден.",
            )
            return

        with open(path, "r") as f:
            self.window.window().setStyleSheet(f.read())
