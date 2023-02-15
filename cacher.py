import sqlite3 as sql
from PyQt6.QtCore import QCoreApplication

class Cacher:
    def __init__(self):
        self.conn = ""
        try:
            filepath = QCoreApplication.applicationDirPath()
            self.conn = sql.connect(filepath + "cache.db")
        except Exception as e:
            print("Database Connection Error: ensure that cache.db is in the same directory as this file or create a new file named cache.db.")
            print(e)
            exit(0)

        self.cursor = self.conn.cursor()

        self.createTable()

    def createTable(self): # Here entirely to avoid having to refactor each statement as columns get added.
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cardCache (
                                                                        name BLOB, 
                                                                        smallImgURI BLOB, 
                                                                        normalImgURI BLOB, 
                                                                        manaCost BLOB, 
                                                                        typeLine BLOB,
                                                                        oracleText BLOB,
                                                                        power integer,
                                                                        toughness integer,
                                                                        loyalty integer)""")

    def search(self, name): # TODO: add in for columns.
        return self.cursor.execute("SELECT * FROM cardCache WHERE name LIKE '%' || ? || '%'", (name,)).fetchall()

    def searchExact(self, name):
        return self.cursor.execute("SELECT * FROM cardCache WHERE name LIKE ?", (name,)).fetchall()

    def add(self, name):
        if not self.searchExact(name):
            self.cursor.execute("INSERT INTO cardCache (name) VALUES (?)", (name,))
            self.conn.commit()

    def printTable(self):
        print(self.cursor.execute("SELECT * FROM cardCache").fetchall())

    def clear(self):
        self.cursor.execute("DROP TABLE cardCache")
        self.createTable()

    def close(self):
        self.cursor.close()
        self.conn.close()
