from ui.managers.abstract import AbstractGUIManager


class SettingsManager(AbstractGUIManager):
    def __init__(self, ui):
        self.ui = ui
