from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QTableWidget
from Ui_SettingsWindow import Ui_SettingsWindow
from Authentication import Authentication


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.parent = parent
        

        self.authenticationManager = Authentication()

        self.setup_ui()

    def setup_ui(self):
        self.tableWidget = self.ui.adminInfo_tableWidget
        
        
        # Connect signals and slots
        # ----------------------------------------------------------------
        self.ui.add_admin_btn.clicked.connect(self.addAdministrator)
        self.ui.delete_btn.clicked.connect(self.deleteAdministrator)

        # Set attributes of the dialog
        self.setWindowTitle("Settings")

        self.loadAdminTable()

        # Set the table widget to read-only mode
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def loadAdminTable(self):
        self.tableWidget.clearContents()
        self.adminTable = self.authenticationManager.getAdminTable()

        # Set the number of rows and columns in the table widget
        num_rows = len(self.adminTable)
        num_cols = len(self.adminTable[0])
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)

        # Iterate over the table data and insert it into the table widget
        for row in range(num_rows):
            for col in range(num_cols):
                item = QTableWidgetItem(str(self.adminTable[row][col]))
                self.tableWidget.setItem(row, col, item)

        # Resize columns and rows to fit the contents
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


    def addAdministrator(self):
        # Check inputs
        username = self.ui.username_lineEdit.text()
        password = self.ui.password_lineEdit.text()

        if username == "" or password == "": return

        if self.authenticationManager.check_username(username):
            QMessageBox.warning(self, "Error", "Username already in use.")
            print("Username already in use.")
        else:
            if self.authenticationManager.add_usr(username, password, password):
                    QMessageBox.information(self, "Admin Added", "Administrator added successfully.")
                    print("Admin added")
            else:
                QMessageBox.warning(self, "Error", "Failed to add administrator. Username already in use.")
                print("Username already in use")


        # if not self.authenticationManager.check_password(password) and not self.authenticationManager.check_username(username):
        #     if self.authenticationManager.isPasswordValid(password):
        #         if self.authenticationManager.add_usr(username, password, password):
        #             QMessageBox.information(self, "Admin Added", "Administrator added successfully.")
        #             print("Admin added")
        #         else:
        #             QMessageBox.warning(self, "Error", "Failed to add administrator. Username or password already in use.")
        #             print("Username/password already in use")
        #     else:
        #         QMessageBox.warning(self, "Error", "Failed to add administrator. Username or password already in use.")
        #         print("Password already in use")
        # else:
        #     QMessageBox.warning(self, "Error", "Failed to add administrator. Username and password already in use.")
        #     print("Username/password already in use")

        self.ui.username_lineEdit.clear()
        self.ui.password_lineEdit.clear()
        self.loadAdminTable()

    def deleteAdministrator(self):
        # Check inputs
        username = self.ui.username_del_lineEdit.text()
        password = self.ui.password_del_lineEdit.text()

        if username.isspace() or password.isspace(): return

        if self.authenticationManager.check_usr(username, password):
            self.authenticationManager.delete_usr(username)
            QMessageBox.warning(self, "Admin Removed", "Administrator removed from Admin Table")
            print("Administrator removed from Admin Table")
            self.loadAdminTable()
        else:
            QMessageBox.warning(self, "Admin login/password incorrect.")
            print("Admin login/password incorrect.")

        self.ui.username_del_lineEdit.clear()
        self.ui.password_del_lineEdit.clear()


        