class BmiCalculator:
    pass

    def calculateBmi(weight, height):
        bmi = weight / (height ** 2)
        return bmi

    
def main():
    BmiCalculator.weight = float(input("Please enter your weight(kg): "))
    BmiCalculator.height = float(input("Please enter your height(cm): "))
    print(f"Your BMI is {BmiCalculator.calculateBmi(BmiCalculator.weight, BmiCalculator.height)}")

if __name__ == "__main__":
    main()
