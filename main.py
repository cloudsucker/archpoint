import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget

from ui.forms.ui_form import Ui_Widget
from archpoint.handlers import ProjectHandler, HLOC_Handler, CalibrationHandler
from ui.managers import (
    CalibrationManager,
    DotsCreatorManager,
    ImagesManager,
    ProcessingManager,
    ProjectManager,
    SettingsManager,
    StylesManager,
)
from ui.app_router import AppRouter


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        central_widget = QWidget()
        self.ui.setupUi(central_widget)
        self.setCentralWidget(central_widget)

        # APP PREPROCESS
        self.setWindowTitle("Archpoint")

        # HANDLERS
        self.calibration_handler = CalibrationHandler()
        self.project_handler = ProjectHandler()
        self.hloc_handler = HLOC_Handler()

        # MANAGERS
        self.calibration_manager = CalibrationManager(
            self.ui, self, self.calibration_handler
        )
        self.dots_creator_manager = DotsCreatorManager(self.ui, self)
        self.images_manager = ImagesManager(self.ui, self)
        self.processing_manager = ProcessingManager(self.ui, self, self.hloc_handler)
        self.project_manager = ProjectManager(self.ui, self, self.project_handler)
        self.settings_manager = SettingsManager(self.ui)
        self.styles_manager = StylesManager(self)

        # APP ROUTER
        self.app_router = AppRouter(
            self.ui,
            self,
            self.calibration_manager,
            self.dots_creator_manager,
            self.images_manager,
            self.processing_manager,
            self.project_manager,
            self.settings_manager,
            self.styles_manager,
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# LITTLE BEAUTIES TODO:
#   - Добавить кнопку "Отменить" для проекта (обработки).
#   - При пропуске калибровки установить состояние отказа от калибровки, редиректить на страницу отказа.
#   - Добавить отображение названия проекта после его открытия или создания на странице обработки.
#   - Перерисововать логотип.
#   - Добавить все иконки для кнопок.
#   - Переделать визуальное оформление страниц.
