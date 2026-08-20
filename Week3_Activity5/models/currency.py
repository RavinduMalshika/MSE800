from database import Database

class CurrencyManager:
    def __init__(self, db: Database):
        self.db = db

    def add_currency(self, code: str, name: str):
        self.db.cursor.execute(
            "INSERT OR REPLACE INTO currencies VALUES (?, ?)", 
            (code.upper(), name)
        )
        self.db.conn.commit()

    def set_rate(self, from_code: str, to_code: str, rate: float):
        self.db.cursor.execute(
            "INSERT INTO rates (from_code, to_code, rate) VALUES (?, ?, ?)",
            (from_code.upper(), to_code.upper(), rate)
        )
        self.db.conn.commit()

    def get_rate(self, from_code: str, to_code: str) -> float:
        self.db.cursor.execute(
            "SELECT rate FROM rates WHERE from_code=? AND to_code=? ORDER BY id DESC LIMIT 1",
            (from_code.upper(), to_code.upper())
        )
        row = self.db.cursor.fetchone()
        return row[0] if row else None
