from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from Ui_SettingsWindow import Ui_SettingsWindow
from Authentication import Authentication


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.parent = parent
        self.tableWidget = self.ui.adminInfo_tableWidget

        self.authenticationManager = Authentication()

        self.setup_ui()

    def setup_ui(self):
       

        # Connect signals and slots
        # ----------------------------------------------------------------
        self.ui.add_admin_btn.clicked.connect(self.addAdministrator)

        # Set attributes of the dialog
        self.setWindowTitle("Settings")
        self.tableWidget.setItem(0,0,QTableWidgetItem("10"))

        #self.fillInAdminTable()

    def fillInAdminTable(self):
        table = self.authenticationManager.getAdminTable()

        # Set the number of rows and columns in the table widget
        num_rows = len(table)
        num_cols = len(table[0])
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)

        # Iterate over the table data and insert it into the table widget
        for row in range(num_rows):
            for col in range(num_cols):
                item = QTableWidgetItem(str(table[row][col]))
                self.tableWidget.setItem(row, col, item)


    def addAdministrator(self):
        # Check inputs
        username = self.ui.username_lineEdit.text()
        password = self.ui.password_lineEdit.text()

        if username == "" or password == "": return

        if not self.authenticationManager.check_password(password) and not self.authenticationManager.check_username(username):
            if self.authenticationManager.isPasswordValid(password):
                if self.authenticationManager.add_usr(username, password, password):
                    QMessageBox.information(self, "Admin Added", "Administrator added successfully.")
                    print("Admin added")
                else:
                    QMessageBox.warning(self, "Error", "Failed to add administrator. Username or password already in use.")
                    print("Username/password already in use")
            else:
                QMessageBox.warning(self, "Error", "Failed to add administrator. Username or password already in use.")
                print("Password already in use")
        else:
            QMessageBox.warning(self, "Error", "Failed to add administrator. Username and password already in use.")
            print("Username/password already in use")

        self.ui.username_lineEdit.clear()
        self.ui.password_lineEdit.clear()

    def deleteAdministrator(self):
        # Check inputs
        username = self.ui.username_lineEdit.text()
        password = self.ui.password_lineEdit.text()

        if username == "" or password == "": return

        if self.authenticationManager.check_usr(username, password):
            self.authenticationManager.delete_usr(username)

        self.ui.username_del_lineEdit.clear()
        self.ui.password_del_lineEdit.clear()



        # if self.authenticationManager.check_usr(username, password):
        #     print("Admin cannot be added b/c username&password taken")
        # else:
        #     # add admin
        #     if not self.authenticationManager.check_password(password):
                
        #     else:
        #         print("Password already in use")
            



        