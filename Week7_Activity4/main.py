class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

class Lecturer(Employee):
    def __init__(self, employee_id, name, teaching_subject):
        super().__init__(employee_id, name)
        self.teaching_subject = teaching_subject

    def display_details(self):
        print()
        print(("*" * 10) + "Lecturer" + ("*" * 10))
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Teaching Subject: {self.teaching_subject}")


class Administrator(Employee):
    def __init__(self, employee_id, name, department):
        super().__init__(employee_id, name)
        self.department = department

    def display_details(self):
        print()
        print(("*" * 10) + "Administrator" + ("*" * 10))
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")

class Technician(Employee):
    def __init__(self, employee_id, name, specialisation):
        super().__init__(employee_id, name)
        self.specialisation = specialisation

    def display_details(self):
        print()
        print(("*" * 10) + "Technician" + ("*" * 10))
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Technical Specialisation: {self.specialisation}")

def main():
    lecturer = Lecturer("EMP001", "John", "Python")
    lecturer.display_details()

    admin = Administrator("EMP002", "Jane", "HR")
    admin.display_details()

    tech = Technician("EMP003", "Sam", "Electrician")
    tech.display_details()

if __name__ == "__main__":
    main()
