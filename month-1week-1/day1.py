# Function 1: Greet someone by name 
def greet(name):
    """Take a name and return a greeting"""
    return f"Hello, {name}! Welcome to your coding journey."

# Function 2: Square a number
def square(n):
    """Takes a number and returns its square"""
    return n * n

# Function 3: Check if a number is even
def is_even(n):
    """Takes a number and returns True if even, False if odd"""
    if n % 2 == 0:
        return True
    else:
        return False
    
# Function 4: Find the maximum of three numbers
def max_of_three(a, b, c):
    """Takes three numbers and returns the target one"""
    if a >= b and a>= c:
        return a 
    elif b >= a and b >= c:
        return b
    else:
        return c
    
#Function 5: Reverse a string
def reverse_string(s):
    """Takes a string and return it reversed"""
    return s[::-1]

# Enhance Function 1: Smart Greet
def smart_greet(name):
    """
    Greet with intelligence:
    - Empty name = "Hello, stranger!"
    - "World" = "Hello, World! (Classic!)"
    - Otherwise = normal greeting
    """
    if name == "":
        return "Hello, stranger!"
    elif name.lower() == "world":
        return "Hello, World! (Classic!)"
    else:
        return f"Hello, {name}! Welcome to your coding journey."
    
# New Function: Is Prime Number
def is_prime(n):
    """
    check if a number is prime.
    Prime = only divisible by 1 and itsself
    """
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

# New Function: Factorial
def factorial(n):
    """
    Calculate factorial: n! = n * (n+1) * (n-2) * . . . * 1
    Example: 5! = 5 * 4 * 3 * 2* 1 = 120
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

# New Function: Temperature Converter
def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    Formula: F = (C * 9/5) + 32
    """
    return (celsius * 9/5) + 32

# Test your functions (this is what makes them actually work)
if __name__ == "__main__":
    # Test greet
    print(greet('Alex'))

    # Test square
    print(f"Square of 5 is: {square(5)}")

    # Test is even
    print(f"is 4 even? {is_even(4)}")
    print(f"is 7 even? {is_even(7)}")

    # Test one_of_three
    print(f"Max of 10, 25, 15 is: {max_of_three(10, 25, 15)}")

    # Test reverse_string
    print(f"'hello' reversed is: {reverse_string('hello')}")

    # Test smart_greet
    print("\n--- Smart Greet Tests ---")
    print(smart_greet("Alice"))
    print(smart_greet(""))
    print(smart_greet("World"))

    # Test temperature converter
    print("\n--- Temperature Tests ---")
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"37°C = {celsius_to_fahrenheit(37)}°F")
    
    # Test is_prime
    print("\n--- Prime Tests ---")
    print(f"Is 7 prime? {is_prime(7)}")
    print(f"Is 10 prime? {is_prime(10)}")
    print(f"Is 13 prime? {is_prime(13)}")
    
    # Test factorial
    print("\n--- Factorial Tests ---")
    print(f"5! = {factorial(5)}")
    print(f"0! = {factorial(0)}")
    print(f"7! = {factorial(7)}")
    