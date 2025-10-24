import math

class Calculator:
    """Base calculator with histroy tracking - Day 8 OOP"""

    def __init__(self, name ="Basic Calculator"):
        self.name= name
        self.history = []
        self.memory = 0

    def add(self, a, b):
        result = a + b
        self._record_operation(f'{a} + {b} = {result}')
        return result
    
    def subtract(self, a, b):
        result = a - b
        self._record_operation(f'{a} - {b} = {result}')
        return result
    
    def multiply(self, a, b):
        result = a * b
        self._record_operation(f'{a} * {b} = {result}')
        return result
    
    def divide(self, a, b):
        try:
            result = a / b
            self._record_operation(f'{a} / {b} = {result}')
            return result
        except ZeroDivisionError:
            return 'Error: Cannot divide by zero'
        
    def _record_operation(self, operation):
        """Private method to track histroy"""
        self.history.append(operation)

    def show_history(self):
        """Display all calculations"""
        print(f'\n--- {self.name} History ---')
        if not self.history:
            print('No calculations yet')
        else:
            for i, calc in enumerate(self.history, 1):
                print(f'{i}. {calc}')

    def clear_history(self):
        """Reset calculation history"""
        self.history = []
        print('History cleared!')

    def store_memory(self, value):
        """Store value in memory"""
        self.memory = value
        print(f'Stored {value} in memory')

    def recall_memory(self):
        """Recall stored value"""
        return self.memory
    
    def __str__(self):
        """String representation"""
        return f'{self.name} - {len(self.history)} calculations performed'
    
class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__(name="Scientific Calculator")

    def power(self, base, exponent):
        """Raise to power"""
        result = base ** exponent
        self._record_operation(f'{base} ^ {exponent} = {result}')
        return result 
    
    def square_root(self, number):
        """Calculate square root"""
        if number < 0:
            return 'Error: Cannot take square root of negative number'
        result = math.sqrt(number)
        self._record_operation(f'√{number} = {result}')
        return result
    
    def sine(self, angle):
        """Calcuilate sine (angle in degrees)"""
        result = math.sin(math.radians(angle))
        self._record_operation(f'sin{angle}°) = {result:.4f}')
        return result 
    
    def cosine(self, angle):
        """Calculate cosine (angle in degrees"""
        result = math.cos(math.radians(angle))
        self._record_operation(f'cos({angle}*) = {result:.4f}')
        return result 
    
    def logarithm(self, number, base=10):
        """Calculate logarithm"""
        if number <= 0:
            return 'Error: Cannot take log of non-positive number'
        result = math.log(number, base)
        self._record_operation(f'log_{base}({number}) = {result:.4f}')
        return result 
    
class StatisticsCalculator(Calculator):
    """Calculator for statistical operations"""

    def __init__(self):
        super().__init__('Statistical Calculator')


    def mean(self, numbers):
        """Calculate average"""
        if not numbers:
            return 'Error: Empty list'
        result = sum(numbers) / len(numbers)
        self._record_operation(f'Mean of {numbers} = {result:.2f}')
        return result
    
    def median(self, numbers):
        """Calculate median (middle value)"""
        if not numbers:
            return 'Error: Empty list'
        
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        mid = n // 2

        if n % 2 == 0: #Even number of items
            result = (sorted_nums[mid-1] + sorted_nums[mid]) / 2
        else:
            result = sorted_nums[mid]

        self._record_operation(f'Median of {numbers} = {result:.2f}')
        return result

    def mode(self, numbers):
            """Find most common number(s)"""
            if not numbers:
                return 'Error: Empty list'
            
            from collections import Counter
            counts = Counter(numbers)
            max_count = max(counts.values())
            modes = [num for num, count in counts.items() if count == max_count]

            self._record_operation(f'Mode of {numbers} = {modes}')
            return modes
        
    def range_calc(self, numbers):
            """Calculate range (max - min)"""
            if not numbers:
                return 'Error : Empty list'
            result = max(numbers) - min(numbers)
            self._record_operation(f'Range of {numbers} = {result}')
            return result 
        
    def standard_deviation(self, numbers):
        """Calculate standard deviation"""
        if not numbers:
            return 'Error: Empty list'
        
        avg = sum(numbers) / len(numbers)
        variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
        result = variance ** 0.5
        self._record_operation(f'Std Dev of {numbers} = {result:.2f}')
        return result 
    
def calculator_menu():
    """Main menu demonstrating polymorphism"""

    print('\n' + '='*60)
    print(' '*15 + 'Calculator 2.0')
    print(' '*10 + 'Powered by OOP Inheritance')
    print('='*60)

    # Create all calculator instances
    calculators = {
        '1': Calculator('Basic Calulator'),
        '2': ScientificCalculator(),
        '3': StatisticsCalculator()
    }

    current_calc = None

    while True:
        # Calculator slection menu
        if current_calc is None:
            print('\n' + '-'*60)
            print('Select Calculator Type:')
            print('-'*60)
            print('1. Basic Calculator  (Add, Subtract, Multiply, Divide)')
            print('2. Scientific Calculator  (Powers, Roots, Trig, Logs)')
            print('3. Statistics Calculator (Mean, Median, Mode, Range, Std Dev)')
            print('4. Exit Program')
            print('-'*60)

            choice = input('\nSelect calculator (1-4): ').strip()

            if choice == '4':
                print('\n' + '='*60)
                print('Thanks fo using Calculator 2.0!')
                print('Built with Python OOP by: Marcus Ritchie')
                print('='*60)
                break

            if choice in calculators:
                current_calc = calculators[choice]
                print(f'\n✓ Loaded: {current_calc.name}')
            else:
                print('❌ Invalid choice. Please select 1-4.')
                continue

        # Operations menu based on calculator type
        print('\n' + '-'*60)
        print(f'CURRENT: {current_calc.name}')
        print('-'*60)

        if isinstance(current_calc, StatisticsCalculator):
            print('OPERATIONS:')
            print('1. Mean (Average)')
            print('2. Median (Middle Value)')
            print('3. Mode (Most Frequent)')
            print('4. Range (Max - Min)')
            print('5. Standard Deviation')
            print('6. Show History')
            print('7. Clear History')
            print('8. Switch Calculator')
            print('-'*60)

            op = input('\nChoose operation (1-8): ').strip()

            if op == '8':
                current_calc = None
                continue 
            elif op == '6':
                current_calc.show_history()
            elif op == '7':
                current_calc.clear_history()
            elif op in ['1', '2', '3', '4', '5']:
                try:
                    nums_input = input('Enter numbers seperated by spaces: ')
                    numbers = [float(x) for x in nums_input.split()]

                    if op == '1':
                        result = current_calc.mean(numbers)
                        print(f'\n→ Mean = {result}')
                    elif op == '2':
                        result = current_calc.median(numbers)
                        print(f'\n→ Median = {result}')
                    elif op == '3':
                        result = current_calc.mode(numbers)
                        print(f'\n→ Mode = {result}')
                    elif op == '4':
                        result = current_calc.range_calc(numbers)
                        print(f'\n→ Range = {result}')
                    elif op == '5':
                        result = current_calc.standard_deviation(numbers)
                        print(f'\n→ Standard Deviation = {result}')
                except ValueError:
                    print('❌ Invalid input. Please enter numeric values only.')
                else:
                    print('❌ Invalid operation.')

            elif isinstance(current_calc, ScientificCalculator):
                print('OPERATIONS:')
                print('1. Add')
                print('2. Subtract')
                print('3. Multiply')
                print('4. Divide')
                print('5. Power (x^t)')
                print('6. Square Root')
                print('7. Sine')
                print('8. Cosine')
                print('9. Logarithm')
                print('10. Show History')
                print('11. Clear History')
                print('12. Switch Calculator')
                print('-'*60)

                op = input('\nChoose operation (1-12): ').strip()

                if op == '12':
                    current_calc = None
                    continue
                elif op == '10':
                    current_calc.show_history()
                elif op == '11':
                    current_calc.clear_history()
                elif op in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    try:
                        if op in ['1', '2', '3', '4', '5']:
                            a = float(input('Enter first number: '))
                            b = float(input('Enter second number: '))

                            if op == '1':
                                result = current_calc.add(a, b)
                                print(f'\n→ Result = {result}')
                            elif op == '2':
                                result = current_calc.subtract(a, b)
                                print(f'\n→ Result = {result}')
                            elif op == '3':
                                result = current_calc.multiply(a, b)
                                print(f'\n→ Result = {result}')
                            elif op == '4':
                                result = current_calc.divide(a, b)
                                print(f'\n→ Result = {result}')
                            elif op == '5':
                                result = current_calc.power(a, b)
                                print(f'\n→ Result = {result}')
                        elif op == '6':
                            num = float(input('Enter number: '))
                            result = current_calc.square_root(num)
                            print(f'\n→ Result = {result}')
                        elif op == '7':
                            angle = float(input('Enter angle in degrees: '))
                            result = current_calc.sine(angle)
                            print(f'\n→ Result = {result:.4f}')
                        elif op == '8':
                            angle = float(input('Enter angle in degrees: '))
                            result = current_calc.cosine(angle)
                            print(f'\n→ Result = {result:.4f}')
                        elif op == '9':
                            num = float(input('Enter number: '))
                            base_input = input('Enter base (default 10): ').strip()
                            base = float(base_input) if base_input else 10
                            result = current_calc.logarithm(num, base)
                            print(f'\n→ Result = {result:.4f}')

                    except ValueError:
                        print('❌ Invalid input. Please enter numeric values only.')
                else:
                    print('❌ Invalid operation.')

            else:
                print('❌ Invalid operation.')

        else: #Basic Calculator
            print('OPERATIONS:')
            print('1. Add')
            print('2. Subtract')
            print('3. Multiply')
            print('4. Divide')
            print('5. Show History')
            print('6. Clear History')
            print('7. Switch Calculator')
            print('-'*60)

            op = input('\nChoose operation (1-7): ').strip()

            if op == '7':
                current_calc = None
                continue 
            elif op == '5':
                current_calc.show_history()
            elif op == '6':
                current_calc.clear_history()
            elif op in ['1', '2', '3', '4']:
                try:
                    a = float(input('Enter first number: '))
                    b = float(input('Enter second number: '))

                    if op == '1':
                        result = current_calc.add(a, b)
                        print(f'\n→ Result = {result}')
                    elif op == '2':
                        result = current_calc.subtract(a, b)
                        print(f'\n→ Result = {result}')
                    elif op == '3':
                        result = current_calc.multiply(a, b)
                        print(f'\n→ Result = {result}')
                    elif op == '4':
                        result = current_calc.divide(a, b)
                        print(f'\n→ Result = {result}')
                except ValueError:
                    print('❌ Invalid input. Please enter numeric values only.')
            else:
                print('❌ Invalid operation.')

        input('\nPress ENTER to continue...')

# ========== REPLACE YOUR TEST CODE WITH THIS ==========
if __name__ == "__main__":
    # Run the automated tests first
    print("="*60)
    print("RUNNING AUTOMATED TESTS...")
    print("="*60)
    
    # Quick test
    calc = Calculator()
    calc.add(5, 3)
    
    sci = ScientificCalculator()
    sci.power(2, 8)
    
    stats = StatisticsCalculator()
    stats.mean([10, 20, 30])
    
    print("\n✓ All classes working!")
    print("\nStarting interactive calculator...")
    
    # Launch interactive menu
    calculator_menu()