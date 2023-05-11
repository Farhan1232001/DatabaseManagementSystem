from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from database_manager import DatabaseManager

class StudentTableWidget(QTableWidget):
    """
    Creates table widget. Can load items to widget and update itself.
    """
    def __init__(self):
        super().__init__()
        self.database_manager = DatabaseManager()
        self.setup_ui()


    def setup_ui(self):
        # Set up the table widget
        self.setColumnCount(8)
        self.setHorizontalHeaderLabels(["First Name", "Last Name", "ID", "Phone", "Email", "Department", "Major", "GPA"])
        self.load_students()

    def load_students(self):
        # Retrieve the list of students from the database and populate the table widget
        students = self.database_manager.get_all_students()

        self.setRowCount(len(students))
        for row, student in enumerate(students):
            for col, value in enumerate(student):
                item = QTableWidgetItem(str(value))
                self.setItem(row, col, item)

    def on_item_changed(self, item):
        # Retrieve the new cell value and update the corresponding record in the database
        new_value = item.text()
        row = item.row()
        col = item.column()
        student_id = self.item(row, 0).text()
        column_name = self.horizontalHeaderItem(col).text()

        # Update the record in the database
        self.database_manager.update_student_info(student_id, column_name, new_value)


    def load_hardcoded_data(self):
        data = [
        ("John", "Doe", "1", "555-1234", "johndoe@email.com", "Math", "Applied Math", "3.8", "123 Main St", "New York"),
        ("Jane", "Doe", "2", "555-5678", "janedoe@email.com", "English", "Creative Writing", "3.5", "456 Elm St", "Los Angeles"),
        ("Bob", "Smith", "3", "555-9876", "bobsmith@email.com", "History", "American History", "3.2", "789 Oak St", "Chicago"),
        ("Alice", "Johnson", "4", "555-4321", "alicejohnson@email.com", "Biology", "Genetics", "3.9", "321 Cedar St", "San Francisco"),
        ("Alice", "Johnson", "5", "555-4321", "alicejohnson@email.com", "Biology", "Genetics", "3.9", "321 Cedar St", "San Francisco")
        ]
        self.setRowCount(len(data))
        for row, student in enumerate(data):
            for col, value in enumerate(student):
                item = QTableWidgetItem(str(value))
                self.setItem(row, col, item)

