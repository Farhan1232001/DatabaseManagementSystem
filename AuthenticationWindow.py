from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from Ui_AuthenticationWindow import Ui_AuthenticationWindow
from Authentication import Authentication

class AuthenticationWindow(QtWidgets.QWidget):
    """
    Class cretes authentication window. Takes in username and password and verifies if user
    is an administrator.
    """
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

        # Set the tab order (ie. focus order for when tab key is clicked)
        self.setTabOrder(self.ui.username_lineEdit, self.ui.password_lineEdit)
        self.setTabOrder(self.ui.password_lineEdit, self.ui.login_btn)

    def __del__(self):
        del self.auth

    def closeWindow(self):
        """Method closes Authentication window"""
        self.close()
        self.__del__()

    def setupui(self):
        """Sets up ui for authentication window"""
        self.setWindowTitle("Authentication")
        
    def on_login_button_clicked(self):
        """Runs when login button clicked."""
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
            QMessageBox.information(self, 'Authentication Failed', 'Invalid username or password.')

        self.ui.username_lineEdit.clear()
        self.ui.password_lineEdit.clear()

    def isAuthenticated(self):
        """Method checks if user is authenticated."""
        return self.__isAuthenticated