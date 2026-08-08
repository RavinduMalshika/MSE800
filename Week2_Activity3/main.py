class Student:
    def __init__(self, fullName, age, address, studentId):
        self.fullName = fullName
        self.age = age
        self.address = address
        self.studentId = studentId

students = []

def sortStudentByAge():
    students = students.sort(key=lambda student: student.age)

def printStudents():
    print("Full Name\t Age\t Address\t Student ID")
    for i in students:
        print(f"{i.fullName}\t {i.age}\t {i.address}\t {i.studentId}")

def main():
    while(True):
        print("Student Information")
        fullName = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        address = input("Enter Student Address: ")
        studentId = input("Enter Student ID: ")
        student = Student(fullName, age, address, studentId)
        students.append(student)
        students.sort(key=lambda student: student.age)
        printStudents()
        while True:
            choice = input("Do you want to add another student? (y/n): ").lower()

            if choice == "y":
                break
            elif choice == "n":
                return
            else:
                print("Please enter y or n.")

if __name__ == "__main__":
    main()
