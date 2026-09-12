class PaymentMethod:
    def __init__(self, amount):
        self.amount = amount

    def make_payment(self):
        print(f"Payment of {self.amount} paid")

class CreditCard(PaymentMethod):
    def __init__(self, amount):
        super().__init__(amount)

    def make_payment(self):
        print(f"Payment of {self.amount} paid through Credit Card")

class PayPal(PaymentMethod):
    def __init__(self, amount):
        super().__init__(amount)

    def make_payment(self):
        print(f"Payment of {self.amount} paid through PayPal")

class BankTransfer(PaymentMethod):
    def __init__(self, amount):
        super().__init__(amount)

    def make_payment(self):
        print(f"Payment of {self.amount} paid through Bank Transfer")

def main():
    payments = [
        CreditCard(500),
        PayPal(1000),
        BankTransfer(5000)
    ]

    for payment in payments:
        payment.make_payment()

if __name__ == "__main__":
    main()
