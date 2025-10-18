def calculate_average(scores):
    """Calculate average of a list of scores"""
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
        
    if count > 0:
        average = total / count
        return average
    return 0

def assign_grade(average):
    """Assign letter grade based on average score"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
def process_student(student):
    """Process a single student's data"""
    name = student['name']
    scores = student['scores']
    print(f'\nProcessing {name}:')
    for score in scores:
        if score < 60:
            print(f' Warning: Low score {score}')
        elif score >= 90:
            print(f' Excellent: {score}')
    average = calculate_average(scores)
    grade = assign_grade(average)
    print(f' Average: {average:.1f}')
    print(f' Grade: {grade}')

def process_all_students(students):
    """Process a list of students"""
    print('=== Student Grade Report ===')
    passing_count = 0
    failing_count = 0
    for student in students:
        process_student(student)
        name = student['name']
        scores = student['scores']
        average = calculate_average(scores)
        if average >= 60:
            passing_count += 1
            print(f'{name} passed')
        else:
            failing_count += 1
            print(f'{name} failed')
    
    print(f'\nTotal Passing: {passing_count}')
    print(f'Total Failing: {failing_count}\n')
                  
