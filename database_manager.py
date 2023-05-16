import sqlite3
from console_widget import ConsoleWidget

class DatabaseManager:
    """
    This class communicates with the SQLite3 database.
    Can add, update, and delete students table.
    """

    __instance = None
    
    def __new__(cls):
        """Creates a singleton object for DatabaseManager"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # Connect to the database
            cls.__instance.con = sqlite3.connect('students.db')
            cls.__instance.c = cls.__instance.con.cursor()

            # Check if the students table already exists
            cls.__instance.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
            table_exists = cls.__instance.c.fetchone()

            if not table_exists:
                # If the students table does not exist, create it
                cls.__instance.c.execute('''
                    CREATE TABLE students (
                        id TEXT PRIMARY KEY,
                        firstName TEXT,
                        lastName TEXT,
                        phoneNumber TEXT,
                        email TEXT,
                        department TEXT,
                        Major TEXT,
                        gpa TEXT,
                        birthday TEXT
                    )
                ''')
                print("Students table created successfully.")
            else:
                print("Students table already exists.")

        return cls.__instance

    def __del__(self):
        """Deletes database manager instance."""
        # Close the cursor and connection
        self.c.close()
        self.con.close()

    def close(self):
        """Closes database manager instance."""
        del self


    def add_student(self, data):
        """Adds student to students database."""
        # Build the SQL query
        query = "INSERT INTO students VALUES ("
        placeholders = ", ".join("?" * len(data))
        query += placeholders + ")"

        try:
            # Execute the SQL query with the given data
            self.c.execute(query, data)

            # Commit the changes
            self.con.commit()
            return "Student added successfully."
        except sqlite3.IntegrityError:
            self.con.rollback()
            return "The user already exists"
        
        display_students()

    def update_student(self, row, column, value):
        """Updates student in students database."""
        # Build the SQL query
        query = f"UPDATE students SET {column.lower()} = ? WHERE row = ?"

        try:
            # Execute the SQL query with the given data
            self.c.execute(query, (value, row))

            # Commit the changes
            self.con.commit()
            return f"{column.capitalize()} for student {row} updated successfully."
        except:
            self.con.rollback()
            return f"Failed to update {column} for student {row}."
        
    def update_student_field(self, row, col, new_value, student_id):
        """Updates students field. Runs if cell is edited."""
        # Map the column index to the corresponding field name
        field_names = self.getStudentFields()
        field_name = field_names[col]

        # Build the SQL query
        query = f"UPDATE students SET {field_name} = ? WHERE id = ?"

        try:
            # Execute the SQL query with the given data
            self.c.execute(query, (new_value, student_id))

            # Commit the changes
            self.con.commit()
            return f"{field_name.capitalize()} for student {student_id} updated successfully."
        except Exception as e:
            self.con.rollback()
            return f"Failed to update {field_name} for student {student_id}: {str(e)}"


    def delete_student(self, student_id):
        """Method deletes student from students table, given id."""
        # Establish a connection to the database

        # Delete the student from the 'students' table based on the provided student_id
        try:
            self.c.execute("DELETE FROM students WHERE id=?", (student_id,))

            # Check if any row was affected (i.e., deletion was successful)
            if self.c.rowcount > 0:
                self.con.commit()
                return True
            else:
                self.con.rollback()
                return False
            
        except Exception:
            self.con.rollback()
            return False

    def getStudentFields(self):
        """Return columns of 'students' Table"""
        # Get the list of fields for a table
        self.c.execute(f"SELECT * FROM students")
        return [description[0] for description in self.c.description]

    def display_students(self):
        """Utility method that displays students table to std out."""
        # Retrieve all data from the students table
        self.c.execute("SELECT * FROM students")
        data = self.c.fetchall()

        # Display the data in a tabular format
        print("{:<15} {:<15} {:<15} {:<15} {:<25} {:<15} {:<25} {:<10} {:<15}".format(
            "Student ID", "First Name", "Last Name", "Phone Number", "Email", "Department", "Major", "GPA", "Birthday"))
        print("-" * 140)
        for row in data:
            print("{:<15} {:<15} {:<15} {:<15} {:<25} {:<15} {:<25} {:<10} {:<15}".format(*row))

        # Close the database connection
        self.con.close()


    def get_all_students(self):
        """Retrieves all entries in students table."""
        self.c

        # Retrieve all rows from the specified table
        self.c.execute(f"SELECT * FROM students")
        rows = self.c.fetchall()

        # Combine the column names and rows into a list of lists
        result = [] + list(rows)

        print("Result: ", result)
        return result

    def get_column_count(self, table_name):
        query = f"SELECT COUNT(*) FROM pragma_table_info('{table_name}')"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0
        
    def doesStudentIdExist(self, student_id):
        """Method checks if student id exists. Student id exists iff student exists."""
        # Build the SQL query to check if a student with the given ID exists
        query = "SELECT COUNT(*) FROM students WHERE id = ?"
        self.c.execute(query, (student_id,))
        result = self.c.fetchone()

        if result[0] > 0:
            return True  # Student exists
        else:
            return False  # Student does not exist
        
    # == Methods dealing with Adminstors table =================================
    