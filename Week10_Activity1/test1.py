try:
    text = input("Enter value:")
    value = int(text)
    result = 100 / value
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
