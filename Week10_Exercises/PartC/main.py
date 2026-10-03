def read_first_line(path):
    try:
        with open(path) as f:
            return f.readline().strip()
    except FileNotFoundError:
        print("File path is invalid")
    except PermissionError:
        print(f"No permission to read: {path}")
        
print(read_first_line("Week10_Exercises/PartC/test.txt"))
