from PySide6.QtGui import QIcon, QPixmap

# TODO: ADD THE TRAY ICON OR DELETE THIS
# from PySide6.QtWidgets import QSystemTrayIcon

from ui.managers import AbstractWindow, AbstractGUIManager


class ImagesManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow):
        self.window = window

        self.app_logo_icon = QIcon("static/logo_v2_black.png")
        self.app_logo_pixmap = QPixmap("static/logo_v2_black.png")

        self.preprocess_app_images()

    def preprocess_app_images(self) -> None:
        self.window.setWindowIcon(self.app_logo_icon)
        self.window.ui.label_appLogo.setPixmap(self.app_logo_pixmap.scaledToHeight(155))

        self.__preprocess_calibration_images()

        # TODO: ADD THE TRAY ICON OR DELETE THIS
        # self.window.tray_icon = QSystemTrayIcon(self)
        # self.window.tray_icon.setIcon(self.app_logo_icon)
        # self.window.tray_icon.setVisible(True)

    def __preprocess_calibration_images(self) -> None:
        self.window.ui.label_page_calibrationFromFileOptionIcon.setPixmap(
            QPixmap("static/file/file-black.png").scaledToHeight(70)
        )
