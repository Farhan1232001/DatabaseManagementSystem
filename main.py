from mainwindow import MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor


if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])

    # Set the light mode style
    app.setStyle('Fusion')

    main_window = MainWindow()
    main_window.show()
    app.exec_()
