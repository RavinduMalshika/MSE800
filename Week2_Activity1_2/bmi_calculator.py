class BmiCalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height= height

    def calculateBmi(self):
        bmi = self.weight / ((self.height / 100) ** 2)
        return bmi

    
def main():
    userWeight = float(input("Please enter your weight(kg): "))
    userHeight = float(input("Please enter your height(cm): "))
    calculator = BmiCalculator(userWeight, userHeight)
    print(f"Your BMI is {calculator.calculateBmi():.2f}")

if __name__ == "__main__":
    main()
