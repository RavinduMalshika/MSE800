class Department:
    def __init__(self, department_name, head):
        self.department_name = department_name
        self.head = head

    def show_department(self):
        print(f"Name of Department: {self.department_name}")
        print(f"Head of Department: {self.head}")

class University:
    def __init__(self, name):
        self.name = name
        self.department = Department("Software Engineering", "John")

    def show_university(self):
        print(f"University: {self.name}")
        self.department.show_department()

def main():
    university = University("Auckland University")
    university.show_university()

if __name__ == "__main__":
    main()
