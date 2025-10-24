"""
Lambda Functions - Day 15
compact, one-line functions
"""

# Regular function vs Lambda
def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(square(5))   # 25
print(square_lambda(5))  # 25

# Lambda with multiple arguments 
multiply = lambda x, y: x * y 
print(multiply(3, 4))  # 12

# Lambda in sorting
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'charlie', 'grade': 78}
]

# Sort by group
sorted_students = sorted(students, key =lambda s: s['grade'], reverse=True)

print('\nStudents sorted by grade:')
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")

# Lambda in filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f'\nEven numbers: {evens}')

# Lambda in mapping
squared = list(map(lambda x: x ** 2, numbers))
print(f'Squared numbers: {squared}')

# Practical example: Grade calculation
calculate_letter = lambda grade: (
    'A' if grade >= 90 else
    'B' if grade >= 80 else
    'C' if grade >= 70 else
    'D' if grade >= 60 else
    'F'
)

print(f'\nGrade 85 is: {calculate_letter(85)}')
print(f'Grade 92 is: {calculate_letter(92)}')
