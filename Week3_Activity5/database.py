import sqlite3

class Database:
    def __init__(self, db_name="Week3_Activity5/money_exchange.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = ON;") # Enable Foreign Key support in SQLite
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        with open("Week3_Activity5/schema.sql", "r") as schema:
            sql_script = schema.read()
        
        # Execute the script
        self.cursor.executescript(sql_script)
        self.conn.commit()
