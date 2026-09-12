class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

class PostgradStudent(Student):
    def __init__(self, name, student_id, research_topic):
        super().__init__(name, student_id)
        self.research_topic = research_topic

    def display_details(self):
        print(("*" * 10) + "Postgraduate Student" + ("*" * 10))
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Research Topic: {self.research_topic}")

def main():
    postgrad = PostgradStudent("John", "ST001", "Large Language Models")
    postgrad.display_details()

if __name__ == "__main__":
    main()
