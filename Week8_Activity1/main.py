class Pizza:
    def prepare(self):
        print("Pizza is being prepeared.")

class Burger:
    def prepare(self):
        print("Burger is being prepeared.")

class Pasta:
    def prepare(self):
        print("Pasta is being prepeared.")

class FoodFactory:
    @staticmethod
    def create(choice):
        if choice == "pizza":
            return Pizza()
        elif choice == "burger":
            return Burger()
        elif choice == "pasta":
            return Pasta()

food = FoodFactory.create("burger")
food.prepare()
