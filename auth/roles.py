import sqlite3 as sql

import auth.model


# User Roles
class UserRoles:
    def __init__(self, db):
        self.db = db
        self.con = sql.connect(db)
        self.cur = self.con.cursor()

        # ...
        self.cur.execute('CREATE TABLE IF NOT EXISTS roles(role TEXT)')

    def add_role(self, role):
        for value in role:
            self.cur.execute(f'INSERT INTO roles VALUES("{value}")')
            self.con.commit()

    def del_role(self, role):
        self.cur.execute(f'DELETE FROM roles WHERE role="{role}"')
        self.con.commit()