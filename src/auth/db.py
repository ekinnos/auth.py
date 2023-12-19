# db.py | Auth.py

from .model import UserModel
import sqlite3 as sql

class DB(UserModel):
    def __init__(self, db):
        self.db = db
        self.con = sql.connect(self.db)
        self.cur = self.con.cursor()

    def add_table(self, table, columns):
        full_column = ''
        for column in columns:
            full_column += column + ','

        full_column = full_column[:-1]
        query = f'CREATE TABLE IF NOT EXISTS {table}({full_column})'
        if True:
            self.cur.execute(query)
            return True
        
    def init(self, table, values):
        full_value = ''
        try:
            for value in values:
                full_value += f'"{value}",'

            full_value = full_value[:-1]
            query = f'INSERT INTO {table} VALUES({full_value})'
            if True:
                self.cur.execute(query)
                return True
        except Exception as e:
            print(e)
            return False
    
    def migrate(self):
        if True:
            self.con.commit()
            return True