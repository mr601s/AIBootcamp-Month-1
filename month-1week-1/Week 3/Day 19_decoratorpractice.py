# This is a decorator function
def my_decorator(func):
    """A decorator that prints before and after calling the function."""

    def wrapper():
        print('before the function runs')
        result = func() # Call the original function
        print('after the function runs')
        return result 
    
    return wrapper 

# This is a regular function
def say_hello():
    print('Hello!')
    return 'Done'

# Now let's decorate it
decorated_hello = my_decorator(say_hello)
decorated_hello()


def my_decorator(func):
    def wrapper()
        print('Before the function runs')
        result = func()
        print('After the function runs')
        return result 
    return wrapper 

# instead of: decorated_hello = my_decorator(say_hello)
# We can use @:

@my_decorator
def say_hello():
    print('Hello')
    print('done)')

