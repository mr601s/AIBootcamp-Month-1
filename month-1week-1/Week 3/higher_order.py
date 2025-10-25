"""
Higher-Order Functions - day 15
Functions that work with other functions
"""

# Example 1: functions as argument
def apply_operation(x, y, operation):
    """Apply any operation to two numbers"""
    return operation (x,y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print('Using functions as arguments:')
print(apply_operation(5, 3, add))   # 8
print(apply_operation(5, 3, multiply))  # 15

# Example 2: returning a function
def create_multiplier(n):
    """Create a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier

times_2 = create_multiplier(2)
times_10 = create_multiplier(10) 

print('\nUsing returned functions:')
print(times_2(5))  # 10
print(times_10(5)) # 50

# Example 3: function factory
def create_greeter(greeting):
    """Create customized greeting functions"""
    def greet(name):
        return f'{greeting}, {name}!'
    return greet

say_hello = create_greeter('Hello')
say_hi = create_greeter('Hi')
say_hey = create_greeter('Hey')

print*('\nCustom greeters:')
print(say_hello('Marcus'))  # Hello Marcus
print(say_hi('Marcus'))  # Hi, Marcus!
print(say_hey('Marcus'))  # Hey Marcus! 

# Example 4: Practical - discount calculator factory 
def create_discount_calculator(discount_percent):
    """Create discount calculators for different rates"""
    def calculate(price):
        discount = price * (discount_percent / 100)
        return price - discount
    return calculate

student_discount = create_discount_calculator(20)
senior_discount = create_discount_calculator(30)
member_discount = create_discount_calculator(15)

print('\nDiscount Calculations:')
print(f'$100 with student discount: ${student_discount(100):.2f}')  # 80.00
print(f'$100 with senior discount: ${senior_discount(100):.2f}')    # 70.00
print(f'$100 with member discount: ${member_discount(100):.2f}')    # 85.00
