from database import Database

class CustomerManager:
    def __init__(self, db: Database):
        self.db = db

    def add_customer(self, name: str, email: str) -> int:
        self.db.cursor.execute(
            "INSERT INTO customers (name, email) VALUES (?, ?)", 
            (name, email)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get_customer_by_id(self, customer_id: int):
        self.db.cursor.execute(
            "SELECT id, name, email FROM customers WHERE id = ?",
            (customer_id,)
        )
        return self.db.cursor.fetchone()

    def get_customer_by_email(self, email: str):
        self.db.cursor.execute(
            "SELECT id, name, email FROM customers WHERE LOWER(email) = LOWER(?)",
            (email.strip(),)
        )
        return self.db.cursor.fetchone()

    def get_all_customers(self):
        self.db.cursor.execute(
            "SELECT * FROM customers ORDER BY id ASC"
        )
        return self.db.cursor.fetchall()

    def update_customer(self, customer_id: int, name: str = None, email: str = None) -> bool:
        current = self.get_customer_by_id(customer_id)
        if not current:
            raise ValueError(f"Customer with ID {customer_id} does not exist.")

        new_name = name if name is not None else current[1]
        new_email = email if email is not None else current[2]

        self.db.cursor.execute(
            "UPDATE customers SET name = ?, email = ? WHERE id = ?",
            (new_name, new_email, customer_id)
        )
        self.db.conn.commit()
        return True

    def delete_customer(self, customer_id: int) -> bool:
        current = self.get_customer_by_id(customer_id)
        if not current:
            return False

        self.db.cursor.execute(
            "DELETE FROM customers WHERE id = ?",
            (customer_id,)
        )
        self.db.conn.commit()
        return True
