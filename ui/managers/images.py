from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow

# TODO: ADD THE TRAY ICON OR DELETE THIS
# from PySide6.QtWidgets import QSystemTrayIcon

from ui.forms.ui_form import Ui_Widget
from ui.managers.abstract import AbstractGUIManager


class ImagesManager(AbstractGUIManager):
    def __init__(self, ui: Ui_Widget, main_window: QMainWindow):
        self.ui = ui
        self.main_window = main_window

        self.app_logo_icon = QIcon("static/logo_v2_black.png")
        self.app_logo_pixmap = QPixmap("static/logo_v2_black.png")

        self.preprocess_app_images()

    def preprocess_app_images(self) -> None:
        self.main_window.setWindowIcon(self.app_logo_icon)
        self.ui.label_appLogo.setPixmap(self.app_logo_pixmap.scaledToHeight(155))

        self.__preprocess_calibration_images()

        # TODO: ADD THE TRAY ICON OR DELETE THIS
        # self.main_window.tray_icon = QSystemTrayIcon(self)
        # self.main_window.tray_icon.setIcon(self.app_logo_icon)
        # self.main_window.tray_icon.setVisible(True)

    def __preprocess_calibration_images(self) -> None:
        self.ui.label_page_calibrationFromFileOptionIcon.setPixmap(
            QPixmap("static/file/file-black.png").scaledToHeight(70)
        )
