class Employee:
    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name

class Manager(Employee):
    def __init__(self, employee_id, employee_name, department):
        super().__init__(employee_id, employee_name)
        self.department = department

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee ID: {self.employee_name}")
        print(f"Employee ID: {self.department}")

def main():
    manager = Manager("EMP01", "John", "Marketing")
    manager.display_details()

if __name__ == "__main__":
    main()
