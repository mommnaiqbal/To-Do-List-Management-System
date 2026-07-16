import sqlite3
from config import DATABASE_NAME


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Pending'
        )
        """)
        self.connection.commit()

    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetchall(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
