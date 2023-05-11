import sqlite3
import tkinter as tk

class StudentDatabase:

    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)')
        self.conn.commit()

        self.window = tk.Tk()
        self.window.title('Student Database')

        # Create input fields
        tk.Label(self.window, text='Name').grid(row=0, column=0)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        # Create buttons
        tk.Button(self.window, text='Add Student', command=self.add_student).grid(row=1, column=0)
        tk.Button(self.window, text='Show Database', command=self.show_database).grid(row=1, column=1)

        self.window.mainloop()

    def add_student(self):
        name = self.name_entry.get()
        self.cur.execute('INSERT INTO students (name) VALUES (?)', (name,))
        self.conn.commit()
        self.name_entry.delete(0, tk.END)

    def show_database(self):
        self.cur.execute('SELECT * FROM students')
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

db = StudentDatabase()