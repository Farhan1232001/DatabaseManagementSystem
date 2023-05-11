import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
import sqlite3

class StudentDatabase(QMainWindow):

    def __init__(self):
        super().__init__()

        # Initialize database
        self.conn = sqlite3.connect('students.db')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, address TEXT)')

        # Create main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create stacked widget to hold input and display pages
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Create input page
        self.input_page = QWidget()
        self.stacked_widget.addWidget(self.input_page)

        # Create input page layout
        input_layout = QVBoxLayout(self.input_page)
        input_layout.addWidget(QLabel('Name'))
        self.name_input = QLineEdit()
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(QLabel('ID'))
        self.id_input = QLineEdit()
        input_layout.addWidget(self.id_input)
        input_layout.addWidget(QLabel('Address'))
        self.address_input = QLineEdit()
        input_layout.addWidget(self.address_input)
        input_button_layout = QHBoxLayout()
        input_layout.addLayout(input_button_layout)
        add_button = QPushButton('Add Student')
        add_button.clicked.connect(self.add_student)
        input_button_layout.addWidget(add_button)
        show_button = QPushButton('Show Database')
        show_button.clicked.connect(self.show_database)
        input_button_layout.addWidget(show_button)

        # Create display page
        self.display_page = QWidget()
        self.stacked_widget.addWidget(self.display_page)

        # Create display page layout
        display_layout = QVBoxLayout(self.display_page)
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Address'])
        display_layout.addWidget(self.table)

    def add_student(self):
        # Add student to database
        name = self.name_input.text()
        id = self.id_input.text()
        address = self.address_input.text()
        self.cur.execute('INSERT INTO students (id, name, address) VALUES (?, ?, ?)', (id, name, address))
        self.conn.commit()
        self.name_input.setText('')
        self.id_input.setText('')
        self.address_input.setText('')

    def show_database(self):
        # Show contents of database
        self.cur.execute('SELECT * FROM students')
        rows = self.cur.fetchall()
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.stacked_widget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    student_db = StudentDatabase()
    student_db.show()
    sys.exit(app.exec_())
