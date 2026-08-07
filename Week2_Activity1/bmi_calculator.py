class BmiCalculator:
    def calculateBmi(weight, height):
        bmi = weight / (height ** 2)
        return bmi

    
def main():
    calculator = BmiCalculator()
    calculator.weight = float(input("Please enter your weight(kg): "))
    calculator.height = float(input("Please enter your height(cm): "))
    print(f"Your BMI is {BmiCalculator.calculateBmi(calculator.weight, calculator.height)}")

if __name__ == "__main__":
    main()
