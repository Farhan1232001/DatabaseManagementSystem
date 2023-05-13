from mainwindow import MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor
from AuthenticationWindow import AuthenticationWindow

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])

    # Set the light mode style
    app.setStyle('Fusion')

    # Create all widgets that'll be used in app
    authentication_window = AuthenticationWindow()
    main_window = MainWindow()

    # Connect the login_successful signal to the show_main_window slot
    authentication_window.login_successful.connect(main_window.show_main_window)

    # Show 1st widget of app
    authentication_window.show()

    app.exec_()
