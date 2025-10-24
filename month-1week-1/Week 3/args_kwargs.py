"""
*args and **kwargs - Day 15
Flexible function arguments
"""

# Example 1: *args,- variable positional arguments
def sum_all(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total 

print('example 1: *args')
print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))   # 15
print(sum_all(10, 20))          # 30   
print()                         

# Example 2: **kwargs - Variable keyword arguments
def print_info(**info):
    """Print any number of key-value pairs"""
    for key, value in info.items():
        print(f'{key}: {value}')

print('Example 2: **kwargs')
print_info(name ='Marcus', age=35, city='Rosedale')
print()

# Example 3: combining regular args, *args, **kwargs
def complex_function(required, *args, **kwargs):
    """Function with all argument types"""
    print(f'Required: {required}')
    print(f'*args: {args}')
    print(f'**kwargs: {kwargs}')

print('Example 3: Combined arguments')
complex_function('Must have', 1, 2, 3, name='Marcus', role='Developer')
print()

# Example 4: Practical - flexible logger
def log(level, message, *details, **metadata):
    """Flexible logging function"""
    print(f'[{level}] {message}')

    if details:
        print(f'Details: {details}')

        if metadata:
            print('Metadata:')
            for key, value in metadata.items():
                print(f'  {key}: {value}')

print('example 4: flexible logger')
log('Error', 'database connection failed',
    'Timeout after 30s', 'Retrying...',
    server='db.example.com', port=5432, user='admin')
print()

# Example 5: Function wrapper that preserves arguments
def trace(func):
    """Decorator that traces function calls with any arguments"""
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned: {result}')
        return result
    return wrapper
    
@trace
def calculate(x, y, operation='add'):
    """Calculate with flexible operation"""
    if operation == 'add':
        return x + y
    elif operation == 'multiply':
        return x * y
    return 0

print('Example 5: tracing with args/kwargs')
calculate(5, 3)
calculate(5, 3, operation='multiply')
