import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = 