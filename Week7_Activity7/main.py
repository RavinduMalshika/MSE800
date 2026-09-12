class Person:
    def __init__(self, name):
        self.name = name

    def display_details(self):
        print(f"Name: {self.name}")

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        super().display_details()

class AcademicStaff(Employee):
    def __init__(self, name, employee_id, subject):
        super().__init__(name, employee_id)
        self.subject = subject

    def display_details(self):
        super().display_details()
        print(f"Subject: {self.subject}")

class NonAcademicStaff(Employee):
    def __init__(self, name, employee_id, role):
        super().__init__(name, employee_id)
        self.role = role

    def display_details(self):
        print("\nNon Academic Staff Details")
        super().display_details()
        print(f"Role: {self.role}")

class Lecturer(AcademicStaff):
    def __init__(self, name, employee_id, subject, publications):
        super().__init__(name, employee_id, subject)
        self.publications = publications

    def display_details(self):
        print("\nLecturer Details")
        super().display_details()
        print(f"Role: {self.publications}")

class TA(AcademicStaff):
    def __init__(self, name, employee_id, subject, class_id):
        super().__init__(name, employee_id, subject)
        self.class_id = class_id

    def display_details(self):
        print("\nTeaching Assistant Details")
        super().display_details()
        print(f"Class: {self.class_id}")

class Student(Person):
    def __init__(self, name, student_id, courses):
        super().__init__(name)
        self.student_id = student_id
        self.courses = courses

    def display_details(self):
        print("\nStudent Details")
        super().display_details()
        print(f"Student ID: {self.student_id}")
        print(f"Courses: {self.courses}")

def main():
    lecturer = Lecturer("John", "EMP01", "Python", ["pub1", "pub2"])
    lecturer.display_details()

    ta = TA("Sam", "EMP02", "Python", "C401")
    ta.display_details()

    nonAcademic = NonAcademicStaff("Jane", "EMP03", "Janitor")
    nonAcademic.display_details()

    student = Student("Will", "ST01", ["Python"])
    student.display_details()

if __name__ == "__main__":
    main()
