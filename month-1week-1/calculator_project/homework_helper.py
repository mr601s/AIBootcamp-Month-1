"""
Math Homework Helper
Uses calculator modules to help students solve math problems.
Demonstrates practical module reusability.
"""

from calculator_base import Calculator
from calculator_scientific import ScientificCalculator
from calculator_statistics import StatisticsCalculator
from datetime import datetime

class HomeworkSession:
    """Manages a homework session with problem tracking"""

    def __init__(self, student_name):
        self.student_name = student_name
        self.start_time = datetime.now()
        self.problems = []
        self.basic_calc = Calculator()
        self.sci_calc = ScientificCalculator()
        self.stats_calc = StatisticsCalculator()

    def add_problem(self, problem_type, description, answer):
        """Record a solved problem"""
        problem = {
            'type': problem_type,
            'description': description,
            'answer': answer,
            'timestamp': datetime.now().strftime("%H:%M:%S")
        }
        self.problems.append(problem)

    def generate_report(self):
        """Create homework completion report"""
        print('\n' + '='*60)
        print(f'HOMEWORK REPORT - {self.student_name}')
        print('='*60)
        print(f'Session Start Time: {self.start_time.strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'Total Problems Solved: {len(self.problems)}\n')
        print('\nSolutions:')
        print('-'*60)

        for i, problem in enumerate(self.problems, 1):
            print(f'\n{i}. [{problem['type']}] {problem['description']}')
            print(f'  Answer: {problem['answer']}')
            print(f' Time: {problem['timestamp']}')

        print('\n' + '='*60)
        print('✓ Homework session complete!')
        print('='*60)

    def save_to_file(self, filename='homework_report.txt'):
        """Save homework report to file"""
        with open(filename, 'w') as f:
            f.write(f'HOMEWORK REPORT - {self.student_name}\n')
            f.write('='*60 + '\n')
            f.write(f"Date: {self.start_time.strftime('%B %d, %Y')}\n")
            f.write(f"Start Time: {self.start_time.strftime('%I:%M %p')}\n")
            f.write(f"Problems Solved: {len(self.problems)}\n\n")
            
            for i, problem in enumerate(self.problems, 1):
                f.write(f"{i}. [{problem['type']}] {problem['description']}\n")
                f.write(f"   Answer: {problem['answer']}\n")
                f.write(f"   Time: {problem['timestamp']}\n\n")

        print(f'✓ Report saved to {filename}')

def homework_menu():
    """Interactive menu for homework helper"""

    print('\n' + '='*60)
    print('MATH HOMEWORK HELPER')
    print(' '*10 + "Powered by Calculator Modules")
    print('='*60)

    name = input('\nStudent name:: ')
    session = HomeworkSession(name)

    while True:
        print('\n' + '-'*60)
        print('PROBLEM TYPES:')
        print('-'*60)
        print('1. Basic Arithmatic (add, subtract, multiply, divide)')
        print('2. Scientific Calculations (sin, cos, tan, log, exp)')
        print('3. Statistics (mean, median, mode, stddev)')
        print('4. View Homework Report')
        print('5. Save Report to File')
        print('-'*60)

        choice = input('\nSelect problem type (1-5) or Q to quit:: ').strip().lower()

        if choice == '5':
            session.generate_report()
            filename = f'homework_{name.replace(" ", "_").lower()}.txt'
            session.save_to_file(filename)
            break

        elif choice == '4':
            session.generate_report()

        elif choice == '1':
            solve_basic_problem(session)

        elif choice == '2':
            solve_scientific_problem(session)

        elif choice == '3':
            solve_statistics_problem(session)

        else:
            print('Invalid choice')

def solve_basic_problem(session):
    """Handle basic arithmetic problems"""
    print('\nBASIC ARITHMETIC PROBLEMS')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')

    choice = input('\nSelect operation (1-4):: ').strip()

    try:
        num1 = float(input('Enter first number:: '))
        num2 = float(input('Enter second number:: '))

        if choice == '1':
            result = session.basic_calc.add(num1, num2)
            description = f'{num1} + {num2}'
        elif choice == '2':
            result = session.basic_calc.subtract(num1, num2)
            description = f'{num1} - {num2}'
        elif choice == '3':
            result = session.basic_calc.multiply(num1, num2)
            description = f'{num1} * {num2}'
        elif choice == '4':
            result = session.basic_calc.divide(num1, num2)
            description = f'{num1} / {num2}'
        else:
            print('Invalid operation choice')
            return

        session.add_problem('Basic Arithmetic', description, result)
        print(f'Solution: {description} = {result}')

    except ValueError:
        print('Invalid input. Please enter numeric values.')

def solve_scientific_problem(session):
    """Handle scientific calculation problems"""
    print('\nSCIENTIFIC CALCULATION PROBLEMS')
    print('1. Sine')
    print('2. Cosine')
    print('3. Tangent')
    print('4. Logarithm')
    print('5. Exponential')

    choice = input('\nSelect operation (1-5):: ').strip()

    try:
        num = float(input('Enter number (in degrees for trig functions):: '))

        if choice == '1':
            result = session.sci_calc.sin(num)
            description = f'sin({num})'
        elif choice == '2':
            result = session.sci_calc.cos(num)
            description = f'cos({num})'
        elif choice == '3':
            result = session.sci_calc.tan(num)
            description = f'tan({num})'
        elif choice == '4':
            result = session.sci_calc.log(num)
            description = f'log({num})'
        elif choice == '5':
            result = session.sci_calc.exp(num)
            description = f'exp({num})'
        else:
            print('Invalid operation choice')
            return

        session.add_problem('Scientific Calculation', description, result)
        print(f'Solution: {description} = {result}')

    except ValueError:
        print('Invalid input. Please enter numeric values.')

def solve_statistics_problem(session):
    """Solve a statistics problem"""
    print('\nSTATISTICS PROBLEMS')
    print('1. Mean')
    print('2. Median')
    print('3. Mode')
    print('4. Standard Deviation')

    choice = input('\nSelect operation (1-4):: ').strip()

    try:
        data_input = input('Enter numbers separated by commas:: ')
        data = [float(x.strip()) for x in data_input.split(',')]

        if choice == '1':
            result = session.stats_calc.mean(data)
            description = f'Mean of {data}'
        elif choice == '2':
            result = session.stats_calc.median(data)
            description = f'Median of {data}'
        elif choice == '3':
            result = session.stats_calc.mode(data)
            description = f'Mode of {data}'
        elif choice == '4':
            result = session.stats_calc.stddev(data)
            description = f'Standard Deviation of {data}'
        else:
            print('Invalid operation choice')
            return

        session.add_problem('Statistics', description, result)
        print(f'Solution: {description} = {result}')

    except ValueError:
        print('Invalid input. Please enter numeric values.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    homework_menu()