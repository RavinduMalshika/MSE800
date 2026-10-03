isRunning = True

class RangeException(Exception):
    pass

def read_int(prompt, minimum=None, maximum=None):
    global isRunning
    try:
        number = int(prompt)

        if(minimum > number or maximum < number):
            raise RangeException
    except ValueError:
        print("Please enter a whole number")
    except RangeException:
        print("Number entered not in range")
    else:
        isRunning = False

while isRunning:
    prompt = input("Enter whole number:")
    read_int(prompt, 1, 10)
            