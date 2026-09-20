class Payment:
    def pay(self):
        pass

class OldPayment:
    def make_payment(self, amount):
        print(f"Payment on ${amount} made using Old Payment System.")

class AdapterOne(Payment):
    def __init__(self, old_payment):
        self.old_payment = old_payment

    def pay(self, amount):
        self.old_payment.make_payment(amount)

old_payment = OldPayment()
adapter_one = AdapterOne(old_payment)
adapter_one.pay(500)

class AdapterTwo(Payment, OldPayment):
    def pay(self, amount):
        self.make_payment(amount)

adapter_two = AdapterTwo()
adapter_two.pay(1000)
