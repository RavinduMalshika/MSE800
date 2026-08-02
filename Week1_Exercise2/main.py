print("BMI Calculator")

# take user input for weight and height
weight = float(input("Please enter your weight(kg): "))
height = float(input("Please enter your height(cm): "))

# calculate the BMI of user
bmi = weight / (height ** 2)

# display the bmi
print(f"Your BMI is {bmi}")
