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
        query = f'INSERT INTO roles VALUES("{role}")'
        self.cur.execute(query)
        if __name__ == '__main__':
            self.con.commit()
            self.cur.close()
            return True

    def del_role(self, role):
        try:
            query = f'DELETE FROM roles WHERE role=?'
            self.cur.execute(query, (role,))
            self.con.commit()
            self.cur.close()
            return True
        except sql.Error as error:
            return error
        finally:
            if self.con:
                return 'db closed'