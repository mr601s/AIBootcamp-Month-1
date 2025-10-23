"""
STUDENT GRADE MANAGER - Week 1 Concepts Review
This project demonstrates ALL major concepts from days 1-7.
Each section is annotated to show what concept is being used.
"""

import json # Module import- Day 5 concept (working with JSON files)
from datetime import datetime # MODULE IMPORT - Getting current date/time

#============================================================================
# Day 1: VARIABLES & DATA TYPES
#============================================================================

# Global variables (data stored for the entire program)
GRADE_FILE = 'student_grade.json'  # STRING - stores filename 
PASSING_GRADE = 60.0 # Float - numeric threshhold for passing 

#============================================================================
# Day 5: File I/O & JSON functions
#============================================================================

def load_students(): 
    """
    Load student data from JSON file.
    
    Concepts Used:
    - File I/O (reading files)
    - JSON deserialization (converting JSON string to Python dict)
    - Error handling (try/except)
    - Return values
    """

    try:
        # OPEN FILE - 'r' means read mode 
        with open (GRADE_FILE, 'r') as file:
            # JSON.LOAD - converts JSON file to python dictionary
            return json.load(file)
    except FileNotFoundError:
        # ERROR HANDLING - if file doesn't exist, return empty dict 
        print(f'No existing data found. Starting fresh!')
        return {} # Return - empty dictionary (no students yet)
    
def save_students(students):
    """
    Save student data to JSON file.
    
    Concepts Used:
    - File I/O (Writing files)
    - JSON serialization (converting python dict to JSON string)
    indent = 4 makes the JSON file readable
    """
    # Open File - 'w' means WRITE mode (overwrites existing file)
    with open(GRADE_FILE, 'w') as file:
        # JSON.DUMP - converts python dictionary to JSON string
        json.dump(students, file, indent=4)
    print(f'Data saved to {GRADE_FILE}')

#============================================================================
# Day 2: Functions & Control Flow
#============================================================================

def calculate_average(grades):
    """
    Calculate the average of a list of grades. 
    
    Concepts used:
        - If/Else - conditional logic
        - Built-In Functions - sum(), len()
        - Return Values 
        Division operator (/)
    """

    # IF STATEMENT - check if list is empty
    if not grades: # 'not grades' is True when list is empty
        return 0.0 # RETURN - exit function early with default value
    
    # CALCULATION - sum of all grades divided by count of grades
    total = sum(grades) # BUILT-IN FUNCTION - sum()
    count = len(grades) # BUILT-IN FUNCTION - len()
    average = total / count # Division operator (/)

    return average # RETURN - return calculated average

def get_letter_grade(average):
    """
    Convert numeric average to letter grade.
    
    Concepts used:
        - If/Elif/Else - multi-branch conditional logic
        - Comparison Operators - <, >=
        - Return Values
    """

    # IF/ELIF/ELSE - determine letter grade based on average
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    
#=============================================================================
# Day 3: Lists & Iterations
#=============================================================================

def add_grade(students, name, assignment, grade):
    """
    Add a grade for a student.
    
    Concepts used:
        - Lists - storing multiple grades
        - Dictionaries - storing student data
        - For Loops - iterating over lists
        - Append Method - adding items to a list
    """

    # Dictionary .get() - safely access key, return default if not found
    # # If student doesn't exist, create new entry with empty list 
    if name not in students:
        students[name] = []

    # Dictionary with nested structure - each grade is a dict with details 
    grade_entry = {
        'assignment': assignment,
        'grade': grade,
        'date': datetime.now().strftime('%Y-%m-%d') # Current date as string
    }

    # List .append() - add items to end of list
    students[name].append(grade_entry)
    print(f'Added grade {grade} for {name} on {assignment}')

def view_student_report(students, name):
    """
    Display detailed report for one student. 
    
    Concepts used: 
    IF/ELSE conditional logic
    FOR LOOP - iteration over list
    STRING FORMATION - f-strings
    LIST INDEXING - accessing items by position
    - Function Calls - calling other functions
    """
    # If statement - check if student exists in dictionary

    if name not in students:
        print(f'❌ Student {'name'} not found!')
        return # Return - exit function early (no value saved)
    
    # Variable Assignment - get student's grade list from dictionary
    grades = students[name] 

    # String Formatting - f-strings with embedded expressions
    print(f'\n{"-"*60}')
    print(f'REPORT CARD FOR: {name.upper()}')
    print(f'{"-"*60}')

    # FOR LOOP - iterate through each grade entry
    for i, entry in enumerate(grades, 1):  # enumerate() gives index and item
        assignment = entry['assignment']
        grade = entry['grade']
        date = entry['date']
        # STRING FORMATTING with alignment
        print(f"{i}. {assignment:20s} | Grade: {grade:5.1f} | Date: {date}")
    
    # CALCULATE STATISTICS for this student
    numeric_grades = [g['grade'] for g in grades]  # LIST COMPREHENSION
    avg = calculate_average(numeric_grades)  # FUNCTION CALL
    letter = get_letter_grade(avg)  # FUNCTION CALL
    
    # Display summary
    print(f"{'-'*60}")
    print(f"Total Assignments: {len(grades)}")
    print(f"Average Grade:     {avg:.2f} ({letter})")
    
    # CONDITIONAL - check if passing
    if avg >= PASSING_GRADE:  # Using GLOBAL CONSTANT
        print(f"Status:            ✓ PASSING")
    else:
        print(f"Status:            ✗ FAILING")
    print(f"{'-'*60}\n")

def search_students(students, search_term):
    """
    Search for students by name (partial match).
    
    Concepts used:
    - LIST COMPREHENSION - filtering items
    - STRING METHODS - .lower() for case-insensitive search
    - IN operator - checking if substring exists
    """
    # LIST COMPREHENSION with conditional filtering
    matches = [name for name in students.keys() 
               if search_term.lower() in name.lower()]
    return matches

def get_class_statistics(students):
    """
    Display statistics for entire class.
    
    Concepts used:
    - FOR LOOP - iteration
    - LIST - storing calculated averages
    - BUILT-IN FUNCTIONS - max(), min(), len()
    - LIST COMPREHENSION
    """
    # Check if there are any students
    if not students:
        print("\n❌ No students in the system yet.")
        return
    
    # LIST to store all student averages
    all_averages = []
    
    # FOR LOOP through dictionary items (key-value pairs)
    for name, grades in students.items():  # .items() gives both key and value
        # LIST COMPREHENSION - extract numeric grades
        numeric_grades = [g['grade'] for g in grades]
        # FUNCTION CALL + LIST .append()
        avg = calculate_average(numeric_grades)
        all_averages.append(avg)
    
    # STATISTICS using built-in functions
    class_avg = calculate_average(all_averages)
    highest = max(all_averages)  # MAX() - returns largest value
    lowest = min(all_averages)   # MIN() - returns smallest value
    
    # STRING FORMATTING with multiple lines
    print(f"\n{'='*60}")
    print("CLASS STATISTICS")
    print(f"{'='*60}")
    print(f"Total Students:   {len(students)}")  # LEN() counts dictionary keys
    print(f"Class Average:    {class_avg:.2f}")
    print(f"Highest Average:  {highest:.2f}")
    print(f"Lowest Average:   {lowest:.2f}")
    print(f"{'='*60}\n")


# ============================================================================
# DAY 2: MENU-DRIVEN PROGRAM (WHILE LOOP + IF/ELIF/ELSE)
# ============================================================================

def main_menu():
    """
    Main menu for the grade manager.
    
    CONCEPTS USED:
    - WHILE LOOP - runs until break statement
    - INPUT - getting user input
    - STRING METHODS - .strip()
    - IF/ELIF/ELSE - menu routing
    - FUNCTION CALLS
    - TRY/EXCEPT - error handling
    """
    # FUNCTION CALL - load data at program start
    students = load_students()
    
    # WHILE LOOP - infinite loop until user chooses to exit
    while True:
        # STRING FORMATTING - menu display
        print("\n" + "="*60)
        print(" "*20 + "GRADE MANAGER")
        print("="*60)
        print("1. Add Grade")
        print("2. View Student Report")
        print("3. View All Students")
        print("4. Search Students")
        print("5. Class Statistics")
        print("6. Save & Exit")
        print("-"*60)
        
        # INPUT - get user choice (returns string)
        choice = input("Select option (1-6): ").strip()  # .strip() removes whitespace
        
        # IF/ELIF/ELSE - route to correct function based on choice
        if choice == '1':
            # INPUT calls to get multiple values
            name = input("Student name: ").strip().title()  # .title() capitalizes each word
            assignment = input("Assignment name: ").strip()
            
            # TRY/EXCEPT - handle invalid numeric input
            try:
                grade = float(input("Grade (0-100): "))  # FLOAT() converts string to number
                
                # VALIDATION - check if grade is in valid range
                if 0 <= grade <= 100:  # COMPOUND COMPARISON
                    # FUNCTION CALL with multiple arguments
                    add_grade(students, name, assignment, grade)
                else:
                    print("❌ Grade must be between 0 and 100")
            except ValueError:  # EXCEPTION HANDLING
                print("❌ Invalid grade. Please enter a number.")
        
        elif choice == '2':
            name = input("Student name: ").strip().title()
            # FUNCTION CALL
            view_student_report(students, name)
        
        elif choice == '3':
            # FOR LOOP through dictionary
            print(f"\n{'='*60}")
            print("ALL STUDENTS")
            print(f"{'='*60}")
            
            # CHECK if empty
            if not students:
                print("No students yet.")
            else:
                # FOR LOOP with enumerate
                for i, name in enumerate(students.keys(), 1):
                    # Calculate average for each student
                    grades = [g['grade'] for g in students[name]]
                    avg = calculate_average(grades)
                    letter = get_letter_grade(avg)
                    # STRING FORMATTING with padding
                    print(f"{i}. {name:20s} | Avg: {avg:5.1f} ({letter})")
            print(f"{'='*60}")
        
        elif choice == '4':
            search = input("Search term: ")
            # FUNCTION CALL
            matches = search_students(students, search)
            
            # IF/ELSE based on list length
            if matches:
                print(f"\nFound {len(matches)} match(es):")
                # FOR LOOP through results
                for name in matches:
                    print(f"  - {name}")
            else:
                print("No matches found.")
        
        elif choice == '5':
            # FUNCTION CALL
            get_class_statistics(students)
        
        elif choice == '6':
            # FUNCTION CALL to save data
            save_students(students)
            print("\n✓ Goodbye!")
            break  # BREAK - exit the while loop
        
        else:
            print("❌ Invalid option. Please choose 1-6.")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    CONCEPT: __name__ == "__main__" pattern
    - Runs ONLY when file is executed directly
    - Doesn't run when file is imported as module
    """
    main_menu()  # FUNCTION CALL - start the program