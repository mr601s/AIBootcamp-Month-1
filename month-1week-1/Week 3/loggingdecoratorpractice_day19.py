from datetime import datetime 

def log_calls(func):
    """Decorator that logs every function call"""

    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{timestamp}] Calling {func.__name__}')
        print(f' Arguments: {args}, {kwargs}')

        result = func(*args, **kwargs)

        print(f' Returned: {result}')
        return result
    return wrapper

@log_calls
def divide(a, b):
    return a / b

@log_calls
def greet(name):
    return f'Hello, {name}!'

# Test
divide(10, 2)
greet('Alice')