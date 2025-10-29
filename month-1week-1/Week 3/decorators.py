"""
Custom decorators for banking operations
"""

import time
from datetime import datetime
from functools import wraps 

def log_transaction(func):
    """
    Decorator that logs all transactions to console and file.

    Usage: @log_transaction above any method that modifies account
    """

    @wraps(func) # Preserves original function name/docstring
    def wrapper(self, *args, **kwargs):
        # Get function name and arguments
        func_name = func.__name__
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Log before transaction
        log_message = f'[{timestamp}] {self.owner} - {func_name} - Args: {args}'
        print(log_message)

        # Write to file
        with open('transactions.log', 'a') as f:
            f.write(log_message + '\n')

        # Execute the transaction
        result = func(self, *args, **kwargs)

        # Log after transaction
        result_message = f'-> Result: {result}, New Balance: ${self.balance:.2f}'
        print(result_message)
        
        with open('transactions.log', 'a') as f:
            f.write(result_message + '\n')

        return result
    
    return wrapper

def timer(func):
    """
    Decorator that measures execution time.
    Usage: @timer above any method to track performance
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        duration = (end_time - start_time) * 1000 # convert to milliseconds
        print(f'Timer: {func.__name__} took {duration:.2f}ms')

        return result  
    
    return wrapper

def validate_amount(func):
    """
    Decorator that validates transaction amounts.
    Ensures amount is positive and numeric
    
    Usage: @validate_amount above deposit/withdrawal methods
    """

    @wraps(func)
    def wrapper(self, amount, *args, **kwargs):
        # Validate amount is a number
        if not isinstance(amount, (int, float)):
            raise TypeError(f'Amount must be a number, got {type(amount).__name__}')
        
        # Validate amount is positive
        if amount <= 0:
            raise ValueError(f'Amount must be positive, got {amount}')
        
        # If valid, proceed with transaction
        return func(self, amount, *args, **kwargs)
    
    return wrapper 

if __name__ == "__main__":
    @timer
    def test_function():
        time.sleep(0.01)
        return "Done"
    
    result = test_function()
    print(f"Result: {result}")