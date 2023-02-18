import sqlite3 as sql
from PyQt6.QtCore import QCoreApplication

class Cacher:
    def __init__(self):
        self.conn = ""
        filepath = QCoreApplication.applicationDirPath()
        self.conn = sql.connect(filepath + 'cache.db')

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
        exact = self.searchExact(name)
        if not exact:
            return self.cursor.execute("SELECT * FROM cardCache WHERE name LIKE '%' || ? || '%'", (name,)).fetchall()
        else:
            return exact

    def searchExact(self, name):
        return self.cursor.execute("SELECT * FROM cardCache WHERE name LIKE ?", (name,)).fetchall()

    def add(self, data):
        if not self.searchExact(data[0]):
            self.cursor.execute("INSERT INTO cardCache (name, smallImgURI, normalImgURI, manaCost, typeLine, oracleText, power, toughness, loyalty) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
            self.conn.commit()

    def printTable(self):
        print(self.cursor.execute("SELECT * FROM cardCache").fetchall())

    def clear(self):
        self.cursor.execute("DROP TABLE cardCache")
        self.createTable()

    def close(self):
        self.cursor.close()
        self.conn.close()
