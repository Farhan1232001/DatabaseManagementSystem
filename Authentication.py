"""

#file name (authentication)

#takes username and password as paramaters
#returns true if valid 
#returns false if invalid
def check_usr(username,password)
    does username exist 
        if false return False
        else 
            is password correct
                if false return False
                else return true


#takes username password, and repassword as paramaters
#returns true if succesfully added 
#returns false if couldnt add (usr already exist or re password doesnt match)
def add_usr(username,password,repassword)
    does username already exist 
        if true return False
        else 
            does password == repassword
                if false return False
                else store new username and return True
            

#takes username (can only use function when signed in)
#returns true if deleted 
#returns false if error (username doesnt exist or only one usr remaining )
def delete_usr(username)
    is there atleast 2 usernames
        if true
            does username already exist 
                if true delete user &return true
                else return False
        else return false
            """

import sqlite3
import hashlib

class Authentication:
    def __init__(self, db_file='students.db'):
        self.con = sqlite3.connect(db_file)
        self.cur = self.con.cursor()

        # Create the authentication table if it doesn't exist
        self.cur.execute('''CREATE TABLE IF NOT EXISTS authentication (
                            username TEXT PRIMARY KEY,
                            password TEXT NOT NULL
                        )''')

        # Add a default user and password if the database is being created for the first time
        self.cur.execute('SELECT COUNT(*) FROM authentication')
        count = self.cur.fetchone()[0]
        if count == 0:
            hashed_password = hashlib.sha256('password'.encode('utf-8')).hexdigest()
            self.cur.execute('INSERT INTO authentication VALUES (?, ?)', ('admin', hashed_password))
            self.con.commit()

    # Check if a user is valid
    def check_usr(self, username, password):
        """Returns true if valid"""
        # Execute a SELECT query to check if the username exists
        self.cur.execute('SELECT * FROM authentication WHERE username=?', (username,))
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

    # Add a new user to the database
    def add_usr(self, username, password, repassword):
        # Execute a SELECT query to check if the username already exists
        self.cur.execute('SELECT * FROM authentication WHERE username=?', (username,))
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
                self.cur.execute('INSERT INTO authentication VALUES (?, ?)', (username, hashed_password))
                self.con.commit()
                return True

    # Delete a user from the database
    def delete_usr(self, username):
        # Execute a SELECT query to check if there are at least two usernames in the database
        self.cur.execute('SELECT COUNT(*) FROM authentication')
        count = self.cur.fetchone()[0]
        if count < 2:
            return False
        else:
            # Execute a DELETE query to delete the user from the database
            self.cur.execute('DELETE FROM authentication WHERE username=?', (username,))
            self.con.commit()
            return True
