import sqlite3
import pathlib


class DB:
    def __init__(self):  # checking if the database is exist, if it's not exist he create
        self.conn = sqlite3.connect(
            str(pathlib.Path(__file__).parent.resolve())+r'\all_users.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS all_users(username text, password text)''')

    def insert(self, username, password):  # create a new account
        # Insert a row of data
        self.c.execute("INSERT INTO all_users VALUES (?,?)",
                       (username, password))
        # Save (commit) the changes
        self.conn.commit()

    def username_exists(self, username):  # checking if the account is exist
        self.c.execute('SELECT username FROM all_users')
        rows = self.c.fetchall()

        for row in rows:
            if (row[0] == username):
                return True
        return False

    def check_password(self, username, password):  # checking if the password is correct
        self.c.execute('SELECT username, password FROM all_users')
        rows = self.c.fetchall()

        for row in rows:
            if row[0] == username and row[1] == password:
                return True
        return False
