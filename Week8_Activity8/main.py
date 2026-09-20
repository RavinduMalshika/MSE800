class Observer:
    def update(self, stock_price):
        pass

class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, stock_price):
        print(f"{self.name} received new stock price: {stock_price}")

class Stock:
    def __init__(self):
        self.investors = []

    def add_investor(self, investor):
        self.investors.append(investor)

    def notify(self, stock_price):
        for investor in self.investors:
            investor.update(stock_price)

investor1 = Investor("Ali")
investor2 = Investor("Sam")

stock = Stock()
stock.add_investor(investor1)
stock.add_investor(investor2)
stock.notify(150)
