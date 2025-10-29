import time

def timer(func):
    """Decorator that measures how long a function takes to run."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        duration = end_time - start_time
        print(f'{func.__name__} took {duration:.4f} seconds')

        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2) # simulate slow operation
    return 'Done!'

@timer 
def calculate_sum(n):
    total = sum(range(n))
    return total 

# Test them 
slow_function()
# Output slow_function took 2.0001 seconds 

result = calculate_sum(1000000)
print(result)
