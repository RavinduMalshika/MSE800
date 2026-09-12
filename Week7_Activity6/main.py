class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, doctor_id):
        super().__init__(name)
        self.doctor_id = doctor_id

class Nurse(Person):
    def __init__(self, name, nurse_id):
        super().__init__(name)
        self.nurse_id = nurse_id

class SeniorNurse(Nurse):
    def __init__(self, name, nurse_id, ward):
        super().__init__(name, nurse_id)
        self.ward = ward

    def display_details(self):
        print("Senior Nurse\n")
        print(f"Name: {self.name}")
        print(f"Nurse ID: {self.nurse_id}")
        print(f"Ward: {self.ward}")

def main():
    senior_nurse = SeniorNurse("John", "N001", "Pediatric")
    senior_nurse.display_details()

if __name__ == "__main__":
    main()

# This uses Hybrid Inheritance
