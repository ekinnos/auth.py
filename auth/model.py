import sqlite3 as sql

# User Model
class UserModel:
    def __init__(self, db):
        self.db = db
        self.con = sql.connect(self.db)
        self.cur = self.con.cursor()

        # ...
        self.cur.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, role TEXT, password TEXT)')

    def add_user(self, username, password):
        self.cur.execute(f'INSERT INTO users VALUES("{username}","","{password}")')
        if __name__ == '__main__':
            self.con.commit()
            self.con.close()

    def del_user(self, username):
        self.cur.execute(f'DELETE FROM users WHERE username="{username}"')
        if __name__ == '__main__':
            self.con.commit()
            self.con.close()

    def load_user(self, username):
        self.cur.execute(f'SELECT * FROM users WHERE username="{username}"')
        data = self.cur.fetchall()
        return data