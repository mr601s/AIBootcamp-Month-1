""" Decorators - Day 15
Function wrappers that add superpowers
"""

from sys import exception
import time
from datetime import datetime

# Example 1: Basic decorator
def my_decorator(func):
    """Wrap a function with extra behavior"""
    def wrapper():
        print('Something before the function')
        func()
        print('something after the function')
    return wrapper

@my_decorator
def say_hello():
    print('hello!')

print('Example 1: Basic decorator')
say_hello()
print()

# Example 2: decorators with arguments 
def smart_decorator(func):
    """Decorator that handles function arguments"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@smart_decorator
def add(a, b):
    return a + b

print('Example 2: Decorator with args')
print(f'Add 5 + 3 = {add(5, 3)}')
print()

# Example 3: Timing decorator (SUPER USEFUL)
def timer(func):
    """Measure how long a function takes"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f'Function "{func.__name__}" took {duration:.4f} seconds')
        return result
    return wrapper

@timer
def slow_function():
    """Simulate slow operation"""
    time.sleep(1)
    return 'Done!'

print('Example 3: Timing decorator')
result = slow_function()
print(f'Result: {result}')
print()

# Example 4: Logging decorator
def logger(func):
    """Log function calls with timestamp"""
    def wrapper(*args, **kwargs):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{now}] Calling function "{func.__name__}" with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'[{now}] Function "{func.__name__}" returned: {result}')
        return result
    return wrapper

@logger
def calculate_total(items):
    """Calculate total price"""
    return sum(items)

print('Example 4: Logging decorator')
total = calculate_total([10, 20, 30, 40, 50])
print()

# Example 5: Multiple decorators (STACKING)
@timer
@logger
def complex_operation(x, y):
    """Operation with both logging and timing"""
    time.sleep(0.5)
    return x * y

print('Example 5: Stacked decorators')
result = complex_operation(5, 10)
print(f'Final Result: {result}')
print()

# Example 6: Practical - Retry decorator
def retry(max_attempts=3):
    """Retry a function if it raises an exception"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f'Attempt {attempts} failed: {e}')
                    if attempts == max_attempts:
                        print('Max attempts reached. Raising exception.')
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function(will_fail=True):
    """Simulates an unreliable API call"""
    if will_fail:
        raise ValueError('Simulated failure')
    return 'Success!'

print('Example 6: Retry decorator')
try:
    unreliable_function(will_fail=True)
except Exception as e:
    print(f'Final exception caught: {e}')