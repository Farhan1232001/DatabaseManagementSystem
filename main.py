from mainwindow import MainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
