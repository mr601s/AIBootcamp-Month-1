"""
Professional function toolkit - day 15 project
Reusable decorators for production applications
"""

import time
import functools
from datetime import datetime

class Functiontoolkit:
    """Collection of useful function decorators"""

    @staticmethod
    def timer(func):
        """Measure execution time"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'⏱ Function "{func.__name__}" executed in {end - start:.4f} seconds')
            return result
        return wrapper
    
    @staticmethod
    def logger(func):
        """Log function calls"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'[{timestamp}] Calling function "{func.__name__}" with args: {args}, kwargs: {kwargs}')
            result = func(*args, **kwargs)
            print(f'[{timestamp}] Function "{func.__name__}" returned: {result}')
            return result
        return wrapper
    
    @staticmethod
    def retry(max_attempts=3, delay=1):
        """Retry a function on failure"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                attempts = 0
                while attempts < max_attempts:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        attempts += 1
                        print(f'⚠️ Attempt {attempts} failed: {e}')
                        time.sleep(delay)
                raise Exception(f'Function "{func.__name__}" failed after {max_attempts} attempts')
            return wrapper
        return decorator
    
    @staticmethod
    def validate_types(**type_checks):
        """Validate function argument types"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Check kwargs against type_checks
                for arg_name, expected_type in type_checks.items():
                    if arg_name in kwargs:
                        value = kwargs[arg_name]
                        if not isinstance(value, expected_type):
                            raise TypeError(
                                f'{arg_name} must be {expected_type.__name__},'
                                f' got {type(value).__name__}'
                            )
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @staticmethod
    def cache(func):
        """Cache function results"""
        cached_results = {}

        @functools.wraps(func)
        def wrapper(*args):
            if args in cached_results:
                print(f'🔁 Returning cached result for {args}')
                return cached_results[args]
            
            result = func(*args)
            cached_results[args] = result
            return result
        return wrapper
    
# Example usage of the toolkit
if __name__ == '__main__':
    print('='*60)
    print('PROFESSIONAL FUNCTION TOOLKIT - Day 15')
    print('='*60)
    print()

    # Example 1: timed function
    @Functiontoolkit.timer
    def slow_calculation(n):
        """Calculate sum of squares"""
        total = sum(i ** 2 for i in range(n))
        return total 
    
    print('Example 1: timer decorator')
    result = slow_calculation(1000000)
    print(f'Result: {result}')
    print()

# Example 2: Logged function
@Functiontoolkit.logger
def process_data(data):
    """Process some data"""
    return [x * 2 for x in data]

print('Example 2: logger decorator')
result = process_data([1, 2, 3, 4, 5])
print(f'Result: {result}')
print()

# Example 3: Cached expensive function
@Functiontoolkit.cache
@Functiontoolkit.timer
def fibonacci(n):
    """Calculate fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print('Example 3: cache decorator')
print(f'Fibonacci(10): {fibonacci(10)}')
print(f'Fibonacci(15): {fibonacci(15)}')
print()

# Example 4: type validation
@Functiontoolkit.validate_types(x=int, y=int)
def create_user(name, age):
    """Create a user"""
    return {'name': name, 'age': age}

print('Example 4: Type validation')
try:
    user = create_user(name='Marcus', age='35')
    print('Created user: {user}')

    # This will fail
    user = create_user(name='Marcus', age='thirty-five')
except TypeError as e:
    print(f'❌ Type Error: {e}')
print()

# Example 5: Retry decorator
@Functiontoolkit.retry(max_attempts=3, delay=0.5)
@Functiontoolkit.logger
def unreliable_api_call(success_rate=0.3):
    """Simulate unreliable API"""
    import random
    if random.random() > success_rate:
        raise Exception('API timeout')
    return {'status': 'success', 'data': [1, 2, 3]}

print('example 5: Retry decorator')
try:
    result = unreliable_api_call(success_rate=0.8)
    print(f'API result: {result}')
except Exception as e:
    print(f'API ultimately failed: {e}')