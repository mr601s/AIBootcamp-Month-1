"""
Scientific Calculator Module
Extends the base Calculator with advanced mathematical operations. 
"""

import math
from calculator_base import Calculator  # Import YOUR module!


class ScientificCalculator(Calculator):
    """Advanced calculator with scientific functions"""

    def __init__(self):
        super().__init__('Scientific Calculator')

    def power(self, base, exponent):
        """Raise base to exponent"""
        result = base ** exponent
        self._record_operation(f'{base}^{exponent} = {result}')
        return result 
    
    def square_root(self, number):
        """Calculate square root"""
        if number < 0:
            return 'Error: Cannot take square root of negative number'
        result = math.sqrt(number)
        self._record_operation(f'√{number} = {result:.4f}')
        return result 

    def sine(self, angle):
        """Calculate sine (angle in degrees)"""
        result = math.sin(math.radians(angle))
        self._record_operation(f'sin({angle}°) = {result:.4f}')
        return result

    def cosine(self, angle):
        """Calculate cosine (angle in degrees)"""
        result = math.cos(math.radians(angle))
        self._record_operation(f'cos({angle}°) = {result:.4f}')
        return result 
    
    def logarithm(self, number, base=10):
        """Calculate logarithm"""
        if number <= 0:
            return 'Error: Logarithm undefined for non-positive numbers'
        result = math.log(number, base)
        self._record_operation(f'log_{base}({number}) = {result:.4f}')
        return result


# Test code
if __name__ == '__main__':
    print('Testing Scientific Calculator Module...')
    sci = ScientificCalculator()
    print(sci.power(2, 8))
    print(sci.square_root(144))
    print(sci.sine(90))
    sci.show_history()
    print('✓ Scientific calculator module working!')