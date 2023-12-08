import sqlite3 as sql

# User Manager
class UserManager:
    def __init__(self, users, roles):
        self.users = users
        self.roles = roles

        self.users_con = sql.connect(self.users)
        self.roles_con = sql.connect(self.roles)
        self.users_cur = self.users_con.cursor()
        self.roles_cur = self.roles_con.cursor()

    # Give Role to User
    def give_role(self, username, role):
        self.roles_cur.execute('SELECT * FROM roles')
        roles_data = self.roles_cur.fetchall()
        try:
            if role in roles_data:
                query = 'UPDATE users SET role=? WHERE username=?'
                self.cur.execute(query, (role,username,))
                if __name__ == '__main__':
                    self.users_con.commit()
                    self.users_con.close()
                    return True
        except sql.Error as error:
            return error
        finally:
            if self.users_con:
                self.users_con.close()
                return 'db closed'