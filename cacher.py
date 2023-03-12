import sqlite3 as sql
from PyQt6.QtCore import QCoreApplication
# MAJOR TODO: make this cache actually worthwhile:
#             - If at all possible, find a way to make the cache more efficient than the regular search
#             - Make the table not just a big fucking list (hopefully)
#             - Try to search the cache when there is a specific name (for info like cmc) (not usable by end user, probably)
class Cacher:
    def __init__(self):
        self.conn = ""
        filepath = QCoreApplication.applicationDirPath()
        self.conn = sql.connect(filepath + 'cache.db')

        self.cursor = self.conn.cursor()

        self.createTable()

    def createTable(self): # Here entirely to avoid having to refactor each statement as columns get added.
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cardCache (name BLOB, 
                                                                     manaCost BLOB, 
                                                                     typeLine BLOB,
                                                                     oracleText BLOB,
                                                                     power integer,
                                                                     toughness integer,
                                                                     loyalty integer)""")

    def search(self, name): # TODO: add in for columns.
        # assert type(name)
        exact = self.searchExact(name)
        if not exact:
            toExec = "SELECT * FROM cardCache WHERE name LIKE '%' || ? || '%'"
            return self.cursor.execute(toExec, (name,)).fetchall()
        else:
            return exact

    def searchExact(self, name):
        # assert type(name)
        toExec = "SELECT * FROM cardCache WHERE name LIKE ?"
        return self.cursor.execute(toExec, (name,)).fetchall()

    def add(self, data):
        if not self.searchExact(data[0]):
            toExec = "INSERT INTO cardCache (name, manaCost, typeLine, oracleText, power, toughness, loyalty) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(toExec, (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
            self.conn.commit()

    def printTable(self):
        print(self.cursor.execute("SELECT * FROM cardCache").fetchall())

    def clear(self):
        self.cursor.execute("DROP TABLE cardCache")
        self.createTable()

    def close(self):
        self.cursor.close()
        self.conn.close()
