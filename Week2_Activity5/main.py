class TemperatureConverter:
    def __init__(self, value):
        # Store the raw input string (e.g., 'C100' or 'F32')
        self.value = value

    def convertCelsiusToFahrenheit(self, value):
        # Formula: °F = (°C * 1.8) + 32
        convertedValue = (value * 1.8) + 32
        # Display result formatted to 2 decimal places
        print(f"{self.value} degrees Celsius is converted to {convertedValue:.2f} degrees Fahrenheit\n")

    def convertFahrenheitToCelsius(self, value):
        # Formula: °C = (°F - 32) / 1.8
        convertedValue = (value - 32) / 1.8
        # Display result formatted to 2 decimal places
        print(f"{self.value.upper()} degrees Fahrenheit is converted to {convertedValue:.2f} degrees Celsius\n")

    def continueOperation(self):
        # Keep prompting until a valid choice ('y' or 'n') is provided
        while (True):
            isEnd = input("Do you want to convert another value? (y/n): ").upper()
            if (isEnd == "Y"):
                return True   # Continue the main loop
            elif (isEnd == "N"):
                print("-"*40 + "\n")
                return False  # Signal the main loop to stop
            else:
                print("Invalid input. Enter 'y' or 'n'.")

def main():
    # Loop control flag
    isRunning = True

    # Display program banner and instructions
    print(("-"*10) + "Temperature Converter" + ("-"*10))
    print("(please prefix with C for celsius and F for Fahrenheit)")

    while (isRunning):
        # Read temperature input and standardize case for prefix checking
        userValue = input("\nPlease enter the value to convert: ").upper()
        
        # Check if the prefix specifies Celsius
        if (userValue[0] == "C"):
            try:
                # Validate and parse the numeric string following the 'C' prefix
                float(userValue[1:]) 
                
                # Instantiate converter and run Celsius to Fahrenheit conversion
                converter = TemperatureConverter(userValue)
                converter.convertCelsiusToFahrenheit(float(converter.value[1:]))
                
                # Check if the user wants to perform another conversion
                if (converter.continueOperation() == False):
                    isRunning = False
            except:
                # Catches non-numeric inputs (e.g., 'Cabc') or empty string indexing errors
                print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix. eg: C32")

        # Check if the prefix specifies Fahrenheit
        elif (userValue[0] == "F"):
            try:
                # Validate and parse the numeric string following the 'F' prefix
                float(userValue[1:]) 
                
                # Instantiate converter and run Fahrenheit to Celsius conversion
                converter = TemperatureConverter(userValue)
                converter.convertFahrenheitToCelsius(float(converter.value[1:]))
                
                # Check if the user wants to perform another conversion
                if (converter.continueOperation() == False):
                    isRunning = False
            except:
                # Catches non-numeric inputs (e.g., 'Fabc') or empty string indexing errors
                print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix. eg: C32")        
        else:
            # Rejects inputs that do not start with 'C' or 'F'
            print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix")

if __name__ == "__main__":
    main()
