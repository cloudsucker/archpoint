from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, QMovie
from PySide6.QtWidgets import QLabel

# TODO: ADD THE TRAY ICON OR DELETE THIS
# from PySide6.QtWidgets import QSystemTrayIcon

from ui.managers import AbstractWindow, AbstractGUIManager


class ImagesManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow):
        self.window = window

        self.app_logo_black_icon = QIcon("static/logo_v2_black.png")
        self.app_logo_white_icon = QIcon("static/logo_v2_white.png")
        self.app_logo_black_pixmap = QPixmap("static/logo_v2_black.png")
        self.app_logo_white_pixmap = QPixmap("static/logo_v2_white.png")

        self.__label_icon_objects = set()

        self.DEFAULT_ICON_WIDTH = 100
        self.DEFAULT_ICON_HEIGHT = 70
        self.DEFAULT_ICON_SIZE = 70

        self.theme = "light"

        self.preprocess_app_images()

    def __get_label_icon_objects(self):
        # APP LOGO
        self.__label_icon_objects.add(self.ui.label_appLogo)

        # CALIBRATION OPTIONS
        self.__label_icon_objects.add(self.ui.label_page_calibrationFromFileOptionIcon)
        self.__label_icon_objects.add(self.ui.label_page_calibrationStartOptionIcon)
        self.__label_icon_objects.add(self.ui.label_page_calibrationSkipOptionIcon)

        # CALIBRATION STEPS
        self.__label_icon_objects.add(self.ui.label_calibrationSteps_0_MethodAutoIcon)
        self.__label_icon_objects.add(self.ui.label_calibrationSteps_0_MethodManualIcon)

        # PROJECT OPTIONS
        self.__label_icon_objects.add(self.ui.label_newProjectIcon)
        self.__label_icon_objects.add(self.ui.label_chooseProjectIcon)

    def __hide_labels_without_icons(self):
        for label in self.__label_icon_objects:
            if not label.pixmap() and not label.movie():
                label.setVisible(False)
            else:
                label.setVisible(True)

    def switch_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.preprocess_app_images()

    def preprocess_app_images(self):
        self.__get_label_icon_objects()

        if self.theme == "light":
            self.main_window.setWindowIcon(self.app_logo_black_icon)
            self.ui.label_appLogo.setPixmap(
                self.app_logo_black_pixmap.scaledToHeight(155)
            )
        elif self.theme == "dark":
            self.ui.label_appLogo.setPixmap(
                self.app_logo_white_pixmap.scaledToHeight(155)
            )

        # self.__preprocess_calibration_images()
        # self.__preprocess_project_images()

        # TODO: ADD THE TRAY ICON OR DELETE THIS
        # self.window.tray_icon = QSystemTrayIcon(self)
        # self.window.tray_icon.setIcon(self.app_logo_icon)
        # self.window.tray_icon.setVisible(True)

        # HIDING UNLOADED IMAGE LABELS:
        self.__hide_labels_without_icons()

    # def __preprocess_calibration_images(self):
    #     self.ui.label_page_calibrationFromFileOptionIcon.setPixmap(
    #         QPixmap("static/file/file-black.png").scaledToHeight(self.DEFAULT_ICON_SIZE)
    #     )
    #     self.__load_calibration_from_file_gif()
    #     # TODO: ADD START CALIBRATION GIF HERE
    #     self.__load_calibration_skip_gif()

    # def __load_calibration_from_file_gif(self):
    #     calibration_from_file_path = "static/gifs/calibration_from_file.gif"
    #     calibration_from_file_label = self.ui.label_page_calibrationFromFileOptionIcon
    #     self.__load_gif(calibration_from_file_path, calibration_from_file_label)

    # def __load_calibration_skip_gif(self):
    #     calibration_skip_path = "static/gifs/calibration_skip.gif"
    #     calibration_skip_label = self.ui.label_page_calibrationSkipOptionIcon
    #     self.__load_gif(calibration_skip_path, calibration_skip_label)

    # def __preprocess_project_images(self):
    #     self.__load_new_project_gif()
    #     self.__load_choose_project_gif()

    # def __load_new_project_gif(self):
    #     new_project_path = "static/gifs/new_project.gif"
    #     new_project_label = self.ui.label_newProjectIcon
    #     self.__load_gif(new_project_path, new_project_label)

    # def __load_choose_project_gif(self):
    #     choose_project_path = "static/gifs/choose_project.gif"
    #     choose_project_label = self.ui.label_chooseProjectIcon
    #     self.__load_gif(choose_project_path, choose_project_label)

    # def __load_gif(self, path: str, label: QLabel):
    #     movie = QMovie(path)
    #     label.setMovie(movie)
    #     movie.start()
