"""
Quick Stats Analyzer
Command-line tool for instant statistical analysis.
Demonstrates lightweight module usage.
"""

import sys
import os

# Add parent directory to path to import calculator modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator_statistics import StatisticsCalculator


def analyze_data(numbers):
    """Perform complete statistical analysis on data"""

    stats = StatisticsCalculator()

    print('\n' + '='*60)
    print('STATISTICAL ANALYSIS')
    print('='*60)
    print(f'Dataset: {numbers}')
    print(f'Count: {len(numbers)} values')
    print('-'*60)

    # Calculate all statistics 

    print(f'Mean (Average): {stats.mean(numbers):.2f}')
    print(f'Median: {stats.median(numbers)}')
    print(f'Mode (Most Common): {stats.mode(numbers)}')
    print(f'Range (Max - Min): {stats.range_calc(numbers)}')
    print(f'Standard Deviation: {stats.standard_deviation(numbers):.2f}')
    print(f'Sum: {sum(numbers)}')
    print(f'Minimum: {min(numbers)}')
    print(f'Maximum: {max(numbers)}')

    print('='*60)

    # Show calculation history
    print('\nCalculations Performed:')
    stats.show_history()

def main():
    """Main entry point for quick stats"""

    print('\n' + '='*60)
    print(' '*15 + 'QUICK STATS ANALYZER')
    print(' '*10 + 'Instant Statistical Analysis')
    print('='*60)

    # Two modes: Interactive or command-line arguments
    if len(sys.argv) > 1:
        try:
            numbers = [float(x) for x in sys.argv[1:]]
            analyze_data(numbers)
        except ValueError:
            print('❌ Error: All arguments must be numbers')
            print('Usage: python quick_stats.py 10 20 30 40 50')
    else:
        # Interactive mode
        print(f'\nEnter numbers to analyze')
        print('(space-seperated or coma-seperated)')

        try:
            user_input = input('\nNumbers: ').strip()

            # Handle both space and comma seperation
            if ',' in user_input:
                numbers = [float(x) for x in user_input.split(',')]
            else:
                numbers = [float(x) for x in user_input.split()]

            if not numbers:
                print('❌ Error: No numbers entered')
                return
            
            analyze_data(numbers)

        except ValueError:
            print('❌ Error: Please enter valid numbers only')
        except KeyboardInterrupt:
            print('\n❌ Process interrupted by user')

if __name__ == '__main__':
    main()