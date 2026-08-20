from database import Database
from .currency import CurrencyManager

class ExchangeService:
    def __init__(self, db: Database, currency_mgr: CurrencyManager):
        self.db = db
        self.currency_mgr = currency_mgr

    def execute_trade(self, customer_id: int, from_code: str, to_code: str, amount: float):
        rate = self.currency_mgr.get_rate(from_code, to_code)
        if not rate:
            raise ValueError("Exchange rate not configured.")

        converted_amount = amount * rate
        with self.db.conn:
            cursor = self.db.conn.cursor()
            cursor.execute(
                """INSERT INTO transactions 
                   (customer_id, from_code, to_code, amount_given, amount_received) 
                   VALUES (?, ?, ?, ?, ?)""",
                (customer_id, from_code.upper(), to_code.upper(), amount, converted_amount)
            )
        return converted_amount

    def get_all_transactions(self):
        cursor = self.db.conn.cursor()
        cursor.execute(
            """SELECT t.id, c.name, t.from_code, t.to_code, t.amount_given, t.amount_received, t.timestamp
               FROM transactions t
               LEFT JOIN customers c ON t.customer_id = c.id
               ORDER BY t.timestamp DESC"""
        )
        return cursor.fetchall()

    def get_transactions_by_customer_id(self, customer_id: int):
        cursor = self.db.conn.cursor()
        cursor.execute(
            """SELECT t.id, c.name, t.from_code, t.to_code, t.amount_given, t.amount_received, t.timestamp
               FROM transactions t
               LEFT JOIN customers c ON t.customer_id = c.id
               WHERE t.customer_id = ?
               ORDER BY t.timestamp DESC""",
            (customer_id,)
        )
        return cursor.fetchall()

    def get_transactions_by_customer_email(self, customer_email: str):
            cursor = self.db.conn.cursor()
            cursor.execute(
            """SELECT t.id, c.name, t.from_code, t.to_code, t.amount_given, t.amount_received, t.timestamp
               FROM transactions t
               JOIN customers c ON t.customer_id = c.id
               WHERE LOWER(c.email) = LOWER(?)
               ORDER BY t.timestamp DESC""",
            (customer_email.strip(),)
            )
            return cursor.fetchall()
