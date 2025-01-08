# Define a list to store student tuples
students = []

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter score of student {i+1}: "))
    age = int(input(f"Enter age of student {i+1}: "))
    students.append((name, score, age))

# Sort students by score (descending) and age (ascending)
sorted_students = sorted(students, key=lambda student: (-student[1], student[2]))

print("\nSorted Students (by score descending, age ascending):")
for student in sorted_students:
    print(student)
