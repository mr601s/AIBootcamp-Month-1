"""
Statistics Calculator Module
Extends the base calculator with statistical analysis operations.
"""

from calculator_base import Calculator

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
        """Calculate median"""
        if not numbers:
            return 'Error empty list'
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        mid = n // 2

        if n % 2 == 0:
            result = (sorted_nums[mid-1] + sorted_nums[mid]) / 2 
        else:
            result = sorted_nums[mid]

        self._record_operation(f'Median of {numbers} = {result}')
        return result
    
    def mode(self, numbers):
        """Find most common number"""
        if not numbers:
            return 'Error: Empty list'
        
        from collections import Counter
        counts = Counter(numbers)
        max_count = max(counts.values())
        modes = [num for num, count in counts.items() if count == max_count]

        self._record_operation(f'Mode of {numbers} = {modes}')
        return modes 
    
    def range_calc(self, numbers):
        """Calculate range"""
        if not numbers:
            return 'Error: empty list'
        result = max(numbers) - min(numbers)
        self._record_operation(f'Range of {numbers} = {result}')
        return result 
    
    def standard_deviation(self, numbers):
        """Calculate standard deviation"""
        if not numbers:
            return 'Error: empty list'
        
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        result = variance ** 0.5
        self._record_operation(f'STD Dev of {numbers} = {result:.2f}')
        return result 
    
# Test code 
if __name__ == '__main__':
    print('Testing Statistics Calculator Module...')
    stats = StatisticsCalculator()
    print(stats.mean([1, 2, 3, 4, 5]))
    print(stats.median([3, 1, 4, 2, 5]))
    print(stats.mode([1, 2, 2, 3, 4]))
    print(stats.range_calc([10, 2, 8, 4, 6]))
    print(stats.standard_deviation([1, 2, 3, 4, 5]))
    stats.show_history()
    print('✓ Statistics calculator module working!') 
