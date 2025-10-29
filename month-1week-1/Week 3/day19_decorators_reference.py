"""
Day 19: Decorators Reference
Complete examples for future reference
"""

import time
from datetime import datetime

# ============================================
# BASIC DECORATOR
# ============================================

def simple_decorator(func):
    """Basic decorator pattern."""
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper


# ============================================
# TIMING DECORATOR
# ============================================

def timer(func):
    """Measure function execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


# ============================================
# LOGGING DECORATOR
# ============================================

def log_calls(func):
    """Log function calls with timestamp."""
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {func.__name__} called")
        print(f"  Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"  Returned: {result}")
        return result
    return wrapper


# ============================================
# VALIDATION DECORATOR
# ============================================

def validate_positive(func):
    """Ensure all arguments are positive."""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument must be positive, got {arg}")
        result = func(*args, **kwargs)
        return result
    return wrapper


# ============================================
# PROPERTY DECORATOR (CLASS)
# ============================================

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        """Get balance."""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        """Set balance with validation."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount


# ============================================
# CLASS & STATIC METHODS
# ============================================

class MathOperations:
    multiplier = 2  # Class variable
    
    def __init__(self, value):
        self.value = value
    
    def double(self):
        """Instance method."""
        return self.value * 2
    
    @classmethod
    def set_multiplier(cls, value):
        """Class method - modifies class variable."""
        cls.multiplier = value
    
    @staticmethod
    def add(a, b):
        """Static method - utility function."""
        return a + b


# ============================================
# TESTS
# ============================================

if __name__ == "__main__":
    # Test simple decorator
    @simple_decorator
    def greet():
        print("Hello!")
    
    print("=== Simple Decorator ===")
    greet()
    
    # Test timer
    @timer
    def slow_function():
        time.sleep(0.5)
        return "Done"
    
    print("\n=== Timer Decorator ===")
    slow_function()
    
    # Test logging
    @log_calls
    def add(a, b):
        return a + b
    
    print("\n=== Logging Decorator ===")
    add(5, 3)
    
    # Test validation
    @validate_positive
    def calculate_area(length, width):
        return length * width
    
    print("\n=== Validation Decorator ===")
    print("Area:", calculate_area(5, 3))
    
    # Test property
    print("\n=== Property Decorator ===")
    account = BankAccount(1000)
    print("Balance:", account.balance)
    account.balance = 1500
    print("New balance:", account.balance)
    
    # Test class/static methods
    print("\n=== Class & Static Methods ===")
    print("Add:", MathOperations.add(5, 3))
    MathOperations.set_multiplier(5)
    print("Multiplier:", MathOperations.multiplier)