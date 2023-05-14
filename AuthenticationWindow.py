from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from Ui_AuthenticationWindow import Ui_AuthenticationWindow
from Authentication import Authentication

class AuthenticationWindow(QtWidgets.QWidget):
    login_successful = QtCore.pyqtSignal()  # Signal to indicate successful login

    def __init__(self):
        super(AuthenticationWindow, self).__init__()
        self.__isAuthenticated = False
        
        # Set up the user interface from the generated UI file
        self.ui = Ui_AuthenticationWindow()
        self.ui.setupUi(self)   # sets up ui using Ui_AuthenticationWindow class
        self.auth = Authentication()

        # Set ui for the widget (your custum us)
        self.setupui()
        
        # Connect signals and slots
        self.ui.login_btn.clicked.connect(self.on_login_button_clicked)

    def __del__(self):
        del self.auth

    def closeWindow(self):
        self.close()
        self.__del__()

    def setupui(self):
        self.setWindowTitle("Authentication")
        
    def on_login_button_clicked(self):
        # Handle the login button click event
        username = self.ui.username_lineEdit.text()
        password = self.ui.password_lineEdit.text()

        # Perform login authentication logic here
        if self.auth.check_usr(username, password):
            print("Login successful")
            self.login_successful.emit()     # Emit the signal for successful login
            self.__isAuthenticated = True
            self.closeWindow()
        else:
            QMessageBox.warning(self, 'Authentication Failed', 'Invalid username or password.')

        self.ui.username_lineEdit.clear()
        self.ui.password_lineEdit.clear()

    def isAuthenticated(self):
        return self.__isAuthenticated