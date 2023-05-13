import sqlite3
from console_widget import ConsoleWidget
class DatabaseManager:
    
    def __init__(self):
        # Connect to the database
        self.con = sqlite3.connect('test.db')
        self.c = self.con.cursor()

        # Check if the students table already exists
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
        table_exists = self.c.fetchone()

        if not table_exists:
            # If the students table does not exist, create it
            self.c.execute('''
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

    def __del__(self):
        # Close the cursor and connection
        self.c.close()
        self.con.close()


    def add_student(self, data):
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
            return "The user already exists"
        
        display_students()

    def update_student(self, row, column, value):
        # Build the SQL query
        query = f"UPDATE students SET {column.lower()} = ? WHERE row = ?"

        try:
            # Execute the SQL query with the given data
            self.c.execute(query, (value, row))

            # Commit the changes
            self.con.commit()
            return f"{column.capitalize()} for student {row} updated successfully."
        except:
            return f"Failed to update {column} for student {row}."
        
    def update_student_field(self, row, col, new_value, student_id):
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
            return f"Failed to update {field_name} for student {student_id}: {str(e)}"


    def delete_student(self, student_id):
        # Build the SQL query to find the row containing the student_id
        query = "SELECT row FROM students WHERE row = ?"
        self.c.execute(query, (student_id,))
        row = self.c.fetchone()

        # If the row containing the student_id exists, delete the whole row
        if row:
            # Build the SQL query to delete the row
            query = "DELETE FROM students WHERE row = ?"

            try:
                # Execute the SQL query with the given data
                self.c.execute(query, (student_id,))

                # Commit the changes
                self.con.commit()
                self.console.println(f"Student {student_id} deleted successfully.")
                return f"Student {student_id} deleted successfully."
            except:
                self.console.println(f"Failed to delete student {student_id}.")
                return f"Failed to delete student {student_id}."
        else:
            return f"No student found with ID {student_id}."
        

    """
    def delete_student(self, student_id):
        # Connect to the database
        con = sqlite3.connect('test.db')
        c = con.cursor()

        # Build the SQL query to find the row containing the student_id
        query = "SELECT row FROM students WHERE row = ?"
        c.execute(query, (student_id,))
        row = c.fetchone()

        # If the row containing the student_id exists, delete the whole row
        if row:
            # Build the SQL query to delete the row
            query = "DELETE FROM students WHERE row = ?"

            try:
                # Execute the SQL query with the given data
                c.execute(query, (student_id,))

                # Commit the changes and close the database connection
                con.commit()
                con.close()
                return f"Student {student_id} deleted successfully."
            except:
                # Close the database connection
                con.close()
                return f"Failed to delete student {student_id}."
        else:
            # Close the database connection
            con.close()
            return f"No student found with ID {student_id}."
    """

    def getStudentFields(self):
        """Return columns of 'students' Table"""
        # Get the list of fields for a table
        self.c.execute(f"SELECT * FROM students")
        return [description[0] for description in self.c.description]

    def display_students(self):
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
        c = self.c

        # Retrieve all rows from the specified table
        c.execute(f"SELECT * FROM students")
        rows = c.fetchall()

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