def my_decorator(func):
    def wrapper (*args, **kwargs): # Accept any arguments
        print(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs) # Pass them to the original function
        print(f'{func.__name__} returned: {result}')
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a + b

@my_decorator
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}!'

# Test them
print(add(5, 3))
print(greet('Alice'))
print(greet('Bob', greeting='Hi'))

