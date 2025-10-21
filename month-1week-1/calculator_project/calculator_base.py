"""
Base Calculator Module
Contains the calculator class with basic operations and history tracking
"""

class Calculator:
    """Base calculator with history tracking and memory functions"""

    def __init__(self, name='Basic Calculator'):
        self.name = name
        self.history = []
        self.memory = 0

    def add(self, a, b):
        """Add two numbers"""
        result = a + b  # ✅ FIXED: Changed = to +
        self._record_operation(f'{a} + {b} = {result}')
        return result 
    
    def subtract(self, a, b):
        """Subtract b from a"""
        result = a - b
        self._record_operation(f'{a} - {b} = {result}')
        return result 
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self._record_operation(f'{a} * {b} = {result}')
        return result 
    
    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            return 'Error: Cannot divide by zero'
        result = a / b
        self._record_operation(f'{a} / {b} = {result:.4f}')
        return result
    
    def _record_operation(self, operation):
        """Private method to track history"""
        self.history.append(operation)

    def show_history(self):
        """Display all calculations"""
        print(f'\n--- {self.name} History ---')
        if not self.history:
            print('No calculations yet')
        else:
            for i, calc in enumerate(self.history, 1):
                print(f'{i}. {calc}')

    def clear_history(self):  # ✅ FIXED: Removed extra 't'
        """Reset calculation history"""
        self.history = []
        print('History cleared!')

    def store_memory(self, value):
        """Store value in memory"""
        self.memory = value
        print(f'Stored {value} in memory')

    def recall_memory(self):
        """Recall stored memory"""
        return self.memory
    
    def __str__(self):
        """String representation"""
        return f'{self.name} - {len(self.history)} calculations performed'
    

if __name__ == '__main__':
    print('Testing calculator Base Module...')
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(10, 4))
    calc.show_history()
    print('✓ Calculator base module working!')