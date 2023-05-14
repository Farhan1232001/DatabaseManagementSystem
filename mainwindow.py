from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu, QMessageBox, QTableWidget
from PyQt5.QtGui import QIcon

from Ui_MainWindow import Ui_MainWindow
# from login_dialog import LoginDialog
from student_table_widget import StudentTableWidget
from database_manager import DatabaseManager
from console_widget import ConsoleWidget
from SettingsDialog import SettingsDialog
import os

# Set paths to Assets
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, 'assets', 'refreshIcon.png')
settingIconPath = os.path.join(current_dir, 'assets', 'settingsIcon.png')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # initalize QMainWindow Base Class
        self.setup_ui()

        self.database_manager = DatabaseManager()

        self.crudTabs = self.ui.CRUDTabWidget
        self.updateModeCheckBox = self.ui.updateMode_checkbox

            

        

        
    def __del__(self):
        self.database_manager.close()

    def setup_ui(self):
        # Set up the main window layout and widgets using Qt Designer
        # ----------------------------------------------------------------
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #  inherited from the Ui_MainWindow class. 

        self.setWindowTitle("Student Database Management System")

        # Connect signals and slots
        # ----------------------------------------------------------------
        self.ui.addStudent_btn.clicked.connect(self.on_click_addStudent_btn)
        self.ui.deleteStudent_btn.clicked.connect(self.on_click_deleteStudent_btn)
        self.ui.refresh_btn.clicked.connect(self.refresh_student_table)
        self.ui.settings_btn.clicked.connect(self.open_settings_dialog)
        #self.ui.CRUDTabWidget.currentChanged.connect(self.toggleUpdateMode)

        # Set up console window
        self.consoleWidget = ConsoleWidget(self)

        # Set up table
        self.student_table_widget = StudentTableWidget(self)

        # Enable smooth scrolling
        self.student_table_widget.setVerticalScrollMode(QTableWidget.ScrollMode.ScrollPerPixel)
        self.student_table_widget.horizontalScrollBar().setSingleStep(1)
        self.student_table_widget.verticalScrollBar().setSingleStep(1)

        # Set up Buttons
        refreshBtn = self.ui.refresh_btn
        refreshBtn.setIcon(QIcon.fromTheme(icon_path))
        
        settingsBtn = self.ui.settings_btn
        settingsBtn.setIcon(QIcon.fromTheme(settingIconPath))


    def open_settings_dialog(self):
        s = SettingsDialog(self)
        s.exec_()
        

        
    def on_click_addStudent_btn(self):
        # Check if all form fields are filled out
        firstName = self.ui.firstName_lineEdit.text()
        lastName = self.ui.lastName_lineEdit.text()
        id = self.ui.studentID_add_lineEdit.text()
        phoneNum = self.ui.phoneNum_lineEdit.text()
        email= self.ui.email_lineEdit.text()
        department = self.ui.department_lineEdit.text()
        major = self.ui.major_lineEdit.text()
        gpa = self.ui.gpa_spinBox.text()
        birthday = self.ui.birthday_lineEdit.text()

        # Order of list matters!
        data = [id, firstName, lastName, phoneNum, email, department, major, gpa, birthday]


        if firstName == '' or lastName == '' or id == '' or phoneNum == '' or email == '' or department == '' or major == '' or gpa == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please fill out all fields!')
            self.consoleWidget.println('FAILED to add Entry: Please fill out all fields!')
            return
        
        if self.database_manager.doesStudentIdExist(id):
            self.consoleWidget.println("Student ID already exists")
            print("Student ID already exists")
            self.ui.studentID_add_lineEdit.clear()


        # Add the student to the database
        self.database_manager.add_student(data)
        self.consoleWidget.println("Student Added")
        #print("add clicked:  ", data)

        # Clearn form
        self.clearForm()

        # Refresh the student table
        self.refresh_student_table()


    def on_click_deleteStudent_btn(self):
        id = self.ui.studentID_delete_lineEdit.text()

        if id.isspace():
            QMessageBox.warning(self, 'Warning', 'Please enter Student ID!')
            return
        
        if self.database_manager.doesStudentIdExist(id):
            self.database_manager.delete_student(id)

            self.consoleWidget.println(f"Student {id} deleted successfully.")
            QMessageBox.information(self, 'Success', f"Student {id} deleted successfully.")
        else:
            self.consoleWidget.println(f"Failed to delete student {id}.")
            QMessageBox.warning(self, 'Error', f"Failed to delete student {id}.")

        # Clear the form fields
        self.ui.studentID_delete_lineEdit.clear()

        # Refresh the student table
        self.refresh_student_table()


    def show_student_table_widget(self):
        # Set up the student table widget and display it
        self.refresh_student_table()
        self.setCentralWidget(self.student_table_widget)

    def show_add_student_dialog(self):
        # Display the add student dialog
        if self.add_student_dialog.exec_() == QtWidgets.QDialog.Accepted:
            # If the user adds a new student, refresh the student table
            self.refresh_student_table()

    def show_edit_student_dialog(self, student_id):
        # Display the edit student dialog
        self.edit_student_dialog.set_student_id(student_id)
        if self.edit_student_dialog.exec_() == QtWidgets.QDialog.Accepted:
            # If the user edits a student, refresh the student table
            self.refresh_student_table()

    def refresh_student_table(self):
        # Retrieve the list of students from the database and update the student table widget
        self.student_table_widget.load_students()

    def show_main_window(self):
        self.show()

    def clearForm(self):
        # Clear the form fields
        self.ui.firstName_lineEdit.clear()
        self.ui.lastName_lineEdit.clear()
        self.ui.email_lineEdit.clear()
        self.ui.studentID_add_lineEdit.clear()
        self.ui.phoneNum_lineEdit.clear()
        self.ui.department_lineEdit.clear()
        self.ui.major_lineEdit.clear()
        self.ui.gpa_spinBox.clear()
        self.ui.birthday_lineEdit.clear()


    def toggleUpdateMode(self):
        self.updateModeCheckBox.toggle()
