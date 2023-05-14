from PyQt5.QtWidgets import QDialog
from Ui_SettingsWindow import Ui_SettingsWindow
from Authentication import Authentication

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.setup_ui()

        authenticationManager = Authentication()

    def setup_ui(self):
        # Create instance of the generated UI class
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        # Set attributes of the dialog
        self.setWindowTitle("Settings")

        