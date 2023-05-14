

import sqlite3
import hashlib

class Authentication:
    def __init__(self, db_file='students.db'):
        self.con = sqlite3.connect(db_file)
        self.cur = self.con.cursor()
        

        # Create the authentication table if it doesn't exist
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Administrators (
                            username TEXT PRIMARY KEY,
                            password TEXT NOT NULL
                        )''')

        # Add a default user and password if the database is being created for the first time
        self.cur.execute('SELECT COUNT(*) FROM Administrators')
        count = self.cur.fetchone()[0]
        if count == 0:
            hashed_password = hashlib.sha256('password'.encode('utf-8')).hexdigest()
            self.cur.execute('INSERT INTO Administrators VALUES (?, ?)', ('admin', hashed_password))
            self.con.commit()

    # def __del__(self):
    #     # Close the cursor and connection
    #     self.con.close()
    #     self.cur.close()

    def closeWindow(self):
        self.close()
        del self

    # Check if a user is valid
    def check_usr(self, username, password):
        """Checks if usrname/passwrd in admin tableReturns true if valid"""
        # Execute a SELECT query to check if the username exists
        self.cur.execute('SELECT * FROM Administrators WHERE username=?', (username,))
        row = self.cur.fetchone()
        if row is None:
            return False
        else:
            # Hash the input password using the SHA-256 algorithm
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            # Check if the hashed password matches the one in the database
            if row[1] == hashed_password:
                return True
            else:
                return False


    def check_username(self, username):
        """Checks if usrname in admin tableReturns true if it exists"""
        # Execute a SELECT query to check if the password exists
        self.cur.execute('SELECT * FROM Administrators WHERE username=?', (username,))
        row = self.cur.fetchone()
        if row is None:
            return False
        else:
            return True

    def check_password(self, password):
        """Checks if the given password exists in the admin table.
        
        Returns:
        bool: True if the password exists, False otherwise.
        """
        # Execute a SELECT query to check if the password exists
        self.cur.execute('SELECT * FROM Administrators WHERE password=?', (password,))
        row = self.cur.fetchone()

        if row is None:
            return False
        else:
            # Hash the input password using the SHA-256 algorithm
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            # Check if the hashed password matches the one in the database
            if row[1] == hashed_password:
                return True
            else:
                return False


    def getAdminTable(self):
        """Returns the contents of the Administrators table"""
        self.cur.execute('SELECT * FROM Administrators')
        rows = self.cur.fetchall()
        return rows


    # Add a new user to the database
    def add_usr(self, username, password, repassword):
        # Execute a SELECT query to check if the username already exists
        self.cur.execute('SELECT * FROM Administrators WHERE username=?', (username,))
        row = self.cur.fetchone()
        if row is not None:
            return False
        else:
            # Check if the password and re-password match
            if password != repassword:
                return False
            else:
                # Hash the password using the SHA-256 algorithm
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                # Execute an INSERT query to add the new user to the database
                self.cur.execute('INSERT INTO Administrators VALUES (?, ?)', (username, hashed_password))
                self.con.commit()
                return True

    # Delete a user from the database
    def delete_usr(self, username):
        # Execute a SELECT query to check if there are at least two usernames in the database
        self.cur.execute('SELECT COUNT(*) FROM Administrators')
        count = self.cur.fetchone()[0]
        if count < 2:
            return False
        else:
            # Execute a DELETE query to delete the user from the database
            self.cur.execute('DELETE FROM Administrators WHERE username=?', (username,))
            self.con.commit()
            return True
        
    def isPasswordValid(self, password):
        """Checks if the given password can be used to create a new admin"""
        # Hash the input password using the SHA-256 algorithm
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Execute a SELECT query to check if the hashed password exists
        self.cur.execute('SELECT * FROM Administrators WHERE password=?', (hashed_password,))
        row = self.cur.fetchone()

        if row is None:
            return True
        else:
            return False

