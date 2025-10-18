# Day 2: Grade Calculator with Input Verification

def calculate_grade(score):
    """
    Takes a numerical score (0-100) and returns letter grade.
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59
    """
    if score < 0 or score > 100:
        return "Invalid score! Must be 0-100"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_grade_description(letter_grade):
    """Returns description of what the grade means"""
    descriptions = {
        "A": "Excellent! Outstanding work!",
        "B": "Good job! Above average performance.",
        "C": "Satisfactory.  Meeting expectations.",
        "D": "Below average.  Needs improvement.",
        "F": "Failing. Significant improvement needed."
    }
    return descriptions.get(letter_grade, "Unknown grade")

def calculate_gpa_point(letter_grade):
    """Returns GPA point equivalent of letter grade"""
    gpa_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }
    return gpa_points.get(letter_grade, None)

# Interactive version with user input
def grade_calculator_interactive():
    """
    Main program that asks user for score and provides full grade info
    """
    print("=== Grade Calculator ===")
    print("Enter a score between 0 and 100\n")
    
    # Get input from user
    try:
        score = float(input("Enter score: "))
        
        # Calculate grade
        letter = calculate_grade(score)
        
        # If valid grade, show all info
        if letter in ["A", "B", "C", "D", "F"]:
            description = get_grade_description(letter)
            gpa = calculate_gpa_point(letter)
            
            print(f"\n--- Results ---")
            print(f"Score: {score}")
            print(f"Letter Grade: {letter}")
            print(f"Description: {description}")
            print(f"GPA Point: {gpa}")
        else:
            print(f"\n{letter}")  # Error message
            
    except ValueError:
        print("Error: Please enter a valid number!")


# Test the functions
if __name__ == "__main__":
    # Automated tests
    print("=== Automated Tests ===")
    test_scores = [95, 85, 75, 65, 55, 100, 0, -5, 105]
    
    for score in test_scores:
        grade = calculate_grade(score)
        print(f"Score {score}: {grade}")

if __name__
    
    print("\n" + "="*40 + "\n")
    
    # Run interactive version
    grade_calculator_interactive()

def calculate_detailed_grade(score):
    """
    Returns grades with +/- modifiers
    A: 93-100, A-: 90-92
    B+: 87-89, B: 83-86, B-: 80-82
    C+: 77-79, C: 73-76, C-: 70-72
    D+: 67-69, D: 63-66, D-: 60-62
    F: 0-59
    """
    if score < 0 or score > 100:
        return "Invalid"
    elif score >+ 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 63:
        return "D"
    elif score >= 60:
        return "D-"
    else:
        return "F"
    

def get_detailed_gpa(detailed_grade):
    """Convert detailed grade to GPA (4.0 scale with +/- adjustments)"""
    gpa_scale = {
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "D-": 0.7,
        "F": 0.0
    }
    return gpa_scale.get(detailed_grade, None)