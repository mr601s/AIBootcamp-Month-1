"""
Calculator Menu Module
Provides interactive menu system for all calculator types.
"""

from calculator_base import Calculator
from calculator_scientific import ScientificCalculator
from calculator_statistics import StatisticsCalculator 


def calculator_menu():
    """Main interactive menu for Calculator 2.0."""

    print('\n' + '='*60)
    print(' '*15 + 'CALCULATOR 2.0')
    print(' '*10 + 'Modular Architecture Edition')
    print('='*60)

    # Create all calculator instances
    calculators = {
        '1': Calculator('Basic Calculator'),
        '2': ScientificCalculator(),
        '3': StatisticsCalculator()
    }

    current_calc = None 

    while True:
        # Calculator Selection menu
        if current_calc is None:
            print('\n' + '-'*60)
            print('Select Calculator Type:')
            print('-'*60)
            print('1. Basic Calculator')
            print('2. Scientific Calculator')
            print('3. Statistics Calculator')
            print('4. Exit')
            print('-'*60)

            choice = input('\nSelect calculator (1-4): ').strip()

            if choice == '4':
                print('\n' + '='*60)
                print('Thanks for using Calculator 2.0!')
                print('Modular design by: Marcus')
                print('='*60)
                break

            if choice in calculators:
                current_calc = calculators[choice]
                print(f'\n✓ Loaded: {current_calc.name}')  # ✅ FIXED: \n not /n
            else:
                print('❌ Invalid choice. Please select 1-4')
                continue

        # Operations menu based on calculator type
        print('\n' + '-'*60)
        print(f'CURRENT: {current_calc.name}')
        print('-'*60)

        if isinstance(current_calc, StatisticsCalculator):
            print('1. Mean  2. Median  3. Mode  4. Range  5. Std Dev')
            print('6. History  7. Clear  8. Switch Calculator')
            print('-'*60)

            op = input('\nChoose operation (1-8): ').strip()

            if op == '8':  # ✅ FIXED: Changed 'g' to '8'
                current_calc = None
                continue
            elif op == '6':
                current_calc.show_history()
            elif op == '7':
                current_calc.clear_history()
            elif op in ['1', '2', '3', '4', '5']:
                try:
                    nums_input = input('Enter numbers (space-separated): ')
                    numbers = [float(x) for x in nums_input.split()]

                    if op == '1':
                        result = current_calc.mean(numbers)
                    elif op == '2':
                        result = current_calc.median(numbers)
                    elif op == '3':
                        result = current_calc.mode(numbers)
                    elif op == '4':
                        result = current_calc.range_calc(numbers)  # ✅ FIXED
                    elif op == '5':
                        result = current_calc.standard_deviation(numbers)  # ✅ FIXED

                    print(f'\n→ Result: {result}')  # ✅ FIXED: \n not /n
                except ValueError:
                    print('❌ Invalid input. Please enter numeric values only.')

        elif isinstance(current_calc, ScientificCalculator):
            print('1. Power  2. Sqrt  3. Sin  4. Cos  5. Log')
            print('6. History  7. Clear  8. Switch Calculator')
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
                    if op == '1':
                        base = float(input('Enter base: '))
                        exp = float(input('Enter exponent: '))
                        result = current_calc.power(base, exp)
                    elif op == '2':
                        num = float(input('Enter number: '))
                        result = current_calc.square_root(num)  # ✅ FIXED
                    elif op == '3':
                        angle = float(input('Enter angle in degrees: '))
                        result = current_calc.sine(angle)  # ✅ FIXED
                    elif op == '4':
                        angle = float(input('Enter angle in degrees: '))
                        result = current_calc.cosine(angle)  # ✅ FIXED
                    elif op == '5':
                        num = float(input('Enter number: '))
                        result = current_calc.logarithm(num)  # ✅ FIXED

                    print(f'\n→ Result: {result}')  # ✅ FIXED: \n not /n
                except ValueError:
                    print('❌ Invalid input. Please enter numeric values only.')

        else:  # Basic Calculator
            print('1. Add  2. Subtract  3. Multiply  4. Divide')
            print('5. Memory Store  6. Memory Recall')
            print('7. History  8. Clear  9. Switch Calculator')
            print('-'*60)

            op = input('\nChoose operation (1-9): ').strip()

            if op == '9':
                current_calc = None
                continue
            elif op == '7':
                current_calc.show_history()
            elif op == '8':
                current_calc.clear_history()
            elif op == '6':
                mem_value = current_calc.recall_memory()  # ✅ FIXED
                print(f'\n→ Memory: {mem_value}')  # ✅ FIXED: \n not /n
            elif op == '5':  # ✅ ADDED: Memory Store option
                try:
                    value = float(input('Enter value to store: '))
                    current_calc.store_memory(value)
                except ValueError:
                    print('❌ Invalid input. Please enter a number.')
            elif op in ['1', '2', '3', '4']:
                try:
                    num1 = float(input('Enter first number: '))
                    num2 = float(input('Enter second number: '))

                    if op == '1':
                        result = current_calc.add(num1, num2)
                    elif op == '2':
                        result = current_calc.subtract(num1, num2)
                    elif op == '3':
                        result = current_calc.multiply(num1, num2)
                    elif op == '4':
                        result = current_calc.divide(num1, num2)

                    print(f'\n→ Result: {result}')  # ✅ FIXED: \n not /n
                except ValueError:
                    print('❌ Invalid input. Please enter numeric values only.')

        input('\nPress ENTER to continue...')  # ✅ FIXED: Proper indentation


if __name__ == '__main__':
    calculator_menu()