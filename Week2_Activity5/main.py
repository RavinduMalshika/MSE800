class TemperatureConverter:
    def __init__(self, value):
        self.value = value

    def convertCelsiusToFahrenheit(self, value):
        convertedValue = (value * 1.8) + 32 #celsius to fahrenheit conversion
        print(f"{self.value} degrees Celsius is converted to {convertedValue:.2f} degrees Fahrenheit\n")

    def convertFahrenheitToCelsius(self, value):
        convertedValue = (value - 32) / 1.8 #fahrenheit to celsius conversion
        print(f"{self.value.upper()} degrees Fahrenheit is converted to {convertedValue:.2f} degrees Celsius\n")

    def continueOperation(self):
        while (True):
            isEnd = input("Do you want to convert another value? (y/n): ").upper()
            if (isEnd == "Y"):
                return True
            elif (isEnd == "N"):
                print("-"*40 + "\n")
                return False
            else:
                print("Invalid input. Enter 'y' or 'n'.")

def main():
    isRunning = True

    print(("-"*10) + "Temperature Converter" + ("-"*10))
    print("(please prefix with C for celsius and F for Fahrenheit)")

    while (isRunning):
        userValue = input("\nPlease enter the value to convert: ").upper()
        if (userValue[0] == "C"):
            try:
                float(userValue[1:]) #check if the rest of input valid
                converter = TemperatureConverter(userValue)
                converter.convertCelsiusToFahrenheit(float(converter.value[1:]))
                if (converter.continueOperation() == False):
                    isRunning = False
            except:
                print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix. eg: C32")

        elif (userValue[0] == "F"):
            try:
                float(userValue[1:]) #check if the rest of input valid
                converter = TemperatureConverter(userValue)
                converter.convertFahrenheitToCelsius(float(converter.value[1:]))
                if (converter.continueOperation() == False):
                    isRunning = False
            except:
                print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix. eg: C32")        
        else:
            print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix")

if __name__ == "__main__":
    main()
