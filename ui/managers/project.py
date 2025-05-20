import os

from PySide6.QtWidgets import QFileDialog

from ui.managers import AbstractWindow, AbstractGUIManager
from archpoint.handlers import ProjectHandler


class ProjectManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow, handler: ProjectHandler):
        self.window = window
        self.handler = handler

        self.__connect_buttons()

    def __connect_buttons(self) -> None:
        self.connect_button(
            # PROJECT INITAL OPTIONS PAGE -> NEW PROJECT CREATING PAGE
            self.window.ui.pushButton_newProject,
            self.window.ui.page_processingNewProjectCreating,
        )
        self.connect_button(
            # NEW PROJECT CREATING PAGE -> PROJECT INITAL OPTIONS PAGE
            self.window.ui.pushButton_newProjectCreatingCancel,
            self.window.ui.page_processingChoiceProject,
        )
        self.connect_button(
            # NEW PROJECT PATH CHOOSING
            self.window.ui.pushButton_newProjectCreatingPathChoose,
            self.__on_new_project_creating_path_choose_clicked,
        )

    def __on_new_project_creating_path_choose_clicked(self) -> None:
        project_path = QFileDialog.getExistingDirectory(
            self.window, "Выберите папку проекта"
        )
        if project_path and os.path.isdir(project_path):
            self.window.ui.lineEdit_newProjectCreatingPathField.setText(project_path)
