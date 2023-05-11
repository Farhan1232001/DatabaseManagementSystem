import tkinter as tk
import sqlite3

class StudentDatabase:

    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, address TEXT, zip_code TEXT, gender TEXT, dob TEXT, mobile TEXT, email TEXT, phone_number TEXT)')
        self.conn.commit()

        self.window = tk.Tk()
        self.window.title('Student Database')

        # Create input fields
        tk.Label(self.window, text='Student ID').grid(row=0, column=0)
        self.id_entry = tk.Entry(self.window)
        self.id_entry.grid(row=0, column=1)
        tk.Label(self.window, text='First Name').grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self.window)
        self.first_name_entry.grid(row=1, column=1)
        tk.Label(self.window, text='Last Name').grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self.window)
        self.last_name_entry.grid(row=2, column=1)
        tk.Label(self.window, text='Address').grid(row=3, column=0)
        self.address_entry = tk.Entry(self.window)
        self.address_entry.grid(row=3, column=1)
        tk.Label(self.window, text='Zip Code').grid(row=4, column=0)
        self.zip_code_entry = tk.Entry(self.window)
        self.zip_code_entry.grid(row=4, column=1)
        tk.Label(self.window, text='Gender').grid(row=5, column=0)
        self.gender_entry = tk.Entry(self.window)
        self.gender_entry.grid(row=5, column=1)
        tk.Label(self.window, text='Date of Birth').grid(row=6, column=0)
        self.dob_entry = tk.Entry(self.window)
        self.dob_entry.grid(row=6, column=1)
        tk.Label(self.window, text='Mobile').grid(row=7, column=0)
        self.mobile_entry = tk.Entry(self.window)
        self.mobile_entry.grid(row=7, column=1)
        tk.Label(self.window, text='Email').grid(row=8, column=0)
        self.email_entry = tk.Entry(self.window)
        self.email_entry.grid(row=8, column=1)
        tk.Label(self.window, text='Phone Number').grid(row=9, column=0)
        self.phone_number_entry = tk.Entry(self.window)
        self.phone_number_entry.grid(row=9, column=1)

        # Create buttons
        tk.Button(self.window, text='Add Student', command=self.add_student).grid(row=10, column=0)
        tk.Button(self.window, text='Show Database', command=self.show_database).grid(row=10, column=1)

        # Create table to display database
        self.table = tk.Label(self.window, text='')
        self.table.grid(row=11, column=0, columnspan=2)

        self.window.mainloop()


    def add_student(self):
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (self.id, self.first_name, self.last_name, self.address, self.zip_code, self.gender, self.dob,self. mobile, self.email, self.phone_number))
        conn.commit()
        conn.close()

    def show_database(self):
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM students')
        rows = cur.fetchall()
        conn.close()
        return rows


if __name__ == "__main__":
    app = StudentDatabase()