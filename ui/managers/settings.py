from ui.managers.abstract import AbstractWindow, AbstractGUIManager


class SettingsManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow):
        self.window = window
