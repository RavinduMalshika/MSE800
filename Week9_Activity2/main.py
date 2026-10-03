def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

students = {
    "Ali": [70, 80, 65],
    "Sara": [85, 90, 88],
    "John": [60, 55, 70]
}

results = 0

for name, marks in students.items():
    average = calculate_average(marks)
    results += average
    print(name, "average:", average)

highest = max(students)
print("Student with highest marks:", highest)

print("Result:", results)
