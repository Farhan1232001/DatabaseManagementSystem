from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from database_manager import DatabaseManager

class StudentTableWidget(QTableWidget):
    """
    Creates table widget. Can load items to widget and update itself.
    """
    def __init__(self, parent = None):
        super(StudentTableWidget, self).__init__()
        self.database_manager = DatabaseManager()

        self.parent = parent
        
        # Get widgets from parent (parent is MainWindow)
        self.tableWidget = parent.ui.student_table_widget
        self.updateMode_checkbox = parent.ui.updateMode_checkbox
        self.console = parent.consoleWidget

        # Connect signals and slots
        self.tableWidget.itemChanged.connect(self.on_item_changed)
        self.updateMode_checkbox.stateChanged.connect(self.toggleUpdateMode)

        self.isInUpdateMode = False

        self.setup_ui()
        
    def set_item_changed_connection(self, con):
        """if con true, sig/slot connect. Otherwise disconnected"""
        if con:
            self.tableWidget.itemChanged.connect(self.on_item_changed)
        else:
            self.tableWidget.itemChanged.disconnect(self.on_item_changed)



    def setup_ui(self):
        """Sets up ui for student_table_widget."""
        # Set up the table widget
        self.tableWidget.setColumnCount(8)
        self.load_students()
        self.tableWidget.setHorizontalHeaderLabels(self.database_manager.getStudentFields())

        # Set the table widget to read-only mode
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.updateMode_checkbox.setChecked(False)

        self.field_names = self.database_manager.getStudentFields()
        

    def load_students(self):
        """Method loads self (table) with students table."""
        # Retrieve the list of students from the database and populate the table widget

        # Temporary turn of item changed sig/slot
        self.set_item_changed_connection(False)

        self.tableWidget.clearContents()
        students = self.database_manager.get_all_students()

        self.tableWidget.setRowCount(len(students))
        for row, student in enumerate(students):
            for col, value in enumerate(student):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)

        self.set_item_changed_connection(True)

    def on_item_changed(self, item):
        """Method runs when item from table is editied."""
        if self.isInUpdateMode == False: return
        if item is None: return

        # # Disconnect the itemChanged signal temporarily (so that on_item_changed isnt called recursively)
        # self.tableWidget.itemChanged.disconnect(self.on_item_changed)

        row = item.row()
        column = item.column()

        new_value = item.text()
        student_id = self.tableWidget.item(row, 0).text()
        column_name = self.tableWidget.horizontalHeaderItem(column).text()

        print(item.text())
        print(new_value)

        if column_name == self.field_names[0]:
            self.console.println("UPDATING ID NOT ALLOWED")
            print("cannot update id...")
            self.load_students()
            return

        # Update the record in the database
        resultSuccess = self.database_manager.update_student_field(row, column, new_value, student_id)

        if resultSuccess:
            print(resultSuccess)
            self.console.println("Update Successful")
        else:
            print(f"Failed to update {column_name} for student {row}.")
            print(f"Failed to update {column_name} for student {row}.")
            self.console.println(f"Failed to update {column_name} for student {row}.")


        self.load_students()



    def toggleUpdateMode(self):
        """Method is used to turn update mode on/off."""
        if self.isInUpdateMode == True:
            self.isInUpdateMode = False
            self.updateMode_checkbox.setChecked(False)

            # Set the table widget to read-only mode
            self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

            self.parent.consoleWidget.println("UpdateMode SET to FALSE")
        else:
            self.isInUpdateMode = True
            self.updateMode_checkbox.setChecked(True)
            
            # Turn off the read-only mode and allow editing again
            self.tableWidget.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.EditKeyPressed)
            self.parent.consoleWidget.println("UpdateMode SET to TRUE")

