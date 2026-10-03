students = []

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getAverage(self):
        return sum(self.marks)/len(self.marks)

def getStudentData():
    studentMarks = []
    name = input("Enter student name:")
    maths = int(input("Enter maths marks:"))
    science = int(input("Enter science marks:"))
    studentMarks.append(maths)
    studentMarks.append(science)

    return Student(name, studentMarks)


for i in range(2):
    student = getStudentData()
    students.append(student)

print("Name \t Average Score \t Status")

for student in students:
    average = student.getAverage()
    isPass = "Fail"
    if (average > 50):
        isPass = "Pass"
    print(f"{student.name} \t {average} \t\t {isPass}")




