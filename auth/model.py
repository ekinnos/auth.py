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
            self.cur.close()
            return True

    def del_user(self, username):
        try:
            query = 'DELETE FROM users WHERE username=?'
            self.cur.execute(query, (username,))
            self.con.commit()
            self.cur.close()
            return True
        except sql.Error as error:
            return error
        finally:
            if self.con:
                self.con.close()
                return 'db closed'

    def load_user(self, username):
        self.cur.execute(f'SELECT * FROM users WHERE username="{username}"')
        data = self.cur.fetchall()
        return data