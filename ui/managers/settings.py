from ui.managers import AbstractWindow, AbstractGUIManager


class SettingsManager(AbstractGUIManager):
    def __init__(self, window: AbstractWindow):
        self.window = window
