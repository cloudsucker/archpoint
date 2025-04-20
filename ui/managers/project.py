import os

from PySide6.QtWidgets import QMainWindow, QFileDialog

from ui.forms.ui_form import Ui_Widget
from ui.managers.abstract import AbstractGUIManager
from archpoint.handlers import ProjectHandler


class ProjectManager(AbstractGUIManager):
    def __init__(
        self, ui: Ui_Widget, main_window: QMainWindow, handler: ProjectHandler
    ):
        self.ui = ui
        self.main_window = main_window
        self.handler = handler

        self.__connect_buttons()

    def __connect_buttons(self) -> None:
        self.connect_button(
            # PROJECT INITAL OPTIONS PAGE -> NEW PROJECT CREATING PAGE
            self.ui.pushButton_newProject,
            self.ui.page_processingNewProjectCreating,
        )
        self.connect_button(
            # NEW PROJECT CREATING PAGE -> PROJECT INITAL OPTIONS PAGE
            self.ui.pushButton_newProjectCreatingCancel,
            self.ui.page_processingChoiceProject,
        )
        self.connect_button(
            # NEW PROJECT PATH CHOOSING
            self.ui.pushButton_newProjectCreatingPathChoose,
            self.__on_new_project_creating_path_choose_clicked,
        )

    def __on_new_project_creating_path_choose_clicked(self) -> None:
        project_path = QFileDialog.getExistingDirectory(
            self.main_window, "Выберите папку проекта"
        )
        if project_path and os.path.isdir(project_path):
            self.ui.lineEdit_newProjectCreatingPathField.setText(project_path)
