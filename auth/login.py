import sqlite3 as sql

# User Login
class UserLogin:
    def __init__(self, db):
        self.db = db
        self.con = sql.connect(self.db)
        self.cur = self.con.cursor()

    def login(self, username, password):
        self.cur.execute('SELECT * FROM users')
        datas = self.cur.fetchall()
        for data in datas:
            if username in data[0]:
                if username == data[0] and password == data[2]:
                    return True
                else:
                    return False