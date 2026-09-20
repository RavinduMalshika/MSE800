class Car:
    def cost(self):
        return 25000

    def description(self):
        return "Car"

class CarDecorator:
    def __init__(self, car):
        self.car = car

    def cost(self):
        return self.car.cost()

class GPSDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 500

class SunroofDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1000

class LeatherSeatDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1500

class PremiumSoundsDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 800

car = CarDecorator(LeatherSeatDecorator(SunroofDecorator(GPSDecorator(PremiumSoundsDecorator(Car())))))
print(f"Cost of the car is ${car.cost()}")
