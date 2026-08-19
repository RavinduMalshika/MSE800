from database import create_tables, populate_tables
from student_manager import get_all_students, get_student_count_in_each_course, get_all_students_enrolled_in_multiple_course
from tabulate import tabulate

#Selection Screen
def menu():
    print("\n==== Student Information ====")
    print("1. View All Students")
    print("2. View Student Count in Courses")
    print("3. View Students Enrolled in Multiple Courses")
    print("4. Exit")

def fetchAllStudents():
    students = get_all_students()
    headers = ["NID", "First Name", "Last Name", "Birth Date"]
    print(tabulate(students, headers=headers, tablefmt="grid"))

def fetchStudentCountInCourses():
    studentCountInEachCourse = get_student_count_in_each_course()
    headers = ["Subject Code", "Course Name", "Student Count"]
    print(tabulate(studentCountInEachCourse, headers=headers, tablefmt="grid"))

def fetchAllStudentsEnrolledInMultipleCourses():
    studentsEnrolledInMultipleCourses = get_all_students_enrolled_in_multiple_course()
    headers = ["NID", "First Name", "Last Name", "Number of Courses"]
    print(tabulate(studentsEnrolledInMultipleCourses, headers=headers, tablefmt="grid"))

def main():
    create_tables() # Create DB and Tables if not exist
    populate_tables() # Populate the table with dummy data

    while True:
        menu()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            fetchAllStudents()
        elif choice == '2':
            fetchStudentCountInCourses()
        elif choice == '3':
            fetchAllStudentsEnrolledInMultipleCourses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
