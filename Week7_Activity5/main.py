class AcademicInformation:
    def __init__(self, programme, gpa):
        self.programme = programme
        self.gpa = gpa

    def display_details(self):
        print("\nAcademic Information")
        print(f"Programme: {self.programme}")
        print(f"GPA: {self.gpa}")

class ContactInformation:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

    def display_details(self):
        print("\nContact Information")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone}")

class Student(AcademicInformation, ContactInformation):
    def __init__(self, programme, gpa, email, phone, name):
        AcademicInformation.__init__(self,programme, gpa)
        ContactInformation.__init__(self, email, phone)
        self.name = name

    def display_details(self):
        print("\nStudent Information")
        print(f"Name: {self.name}")
        AcademicInformation.display_details(self)
        ContactInformation.display_details(self)

def main():
    student = Student("Python", 3.4, "john@email.com", "02502512345", "John")
    student.display_details()

if __name__ == "__main__":
    main()
