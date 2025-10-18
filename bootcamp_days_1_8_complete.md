# Python Programming Bootcamp - Days 1-8: Complete Study Guide

## Introduction: The Path to Mastery

Welcome, mentee. You've asked what it takes to be great, and I want to start with this truth: **greatness in programming isn't about being the smartest person in the room—it's about being the most persistent learner.**

The best programmers I know share these traits:
- **Intellectual humility**: They assume they don't know everything and actively seek to fill gaps
- **Systems thinking**: They see patterns and connections across different domains
- **Debugging mindset**: They treat every problem as solvable, just requiring the right questions
- **Building habit**: They learn by doing, not just reading
- **Community engagement**: They teach others, which deepens their own understanding

You've built 8 projects in 8 days while traveling for work. That's not luck—that's discipline.

---

## Day 1: Python Fundamentals - Variables, Data Types, and Operators

### Core Concepts

**Variables**
- **Definition**: Containers that store data values; labels that point to data in memory
- **Python approach**: Dynamically typed (no need to declare type)
- **Assignment**: Uses `=` operator (means "assign", not "equals")

```python
# Variables can change type
x = 5           # x is an integer
x = "hello"     # now x is a string
x = [1, 2, 3]   # now x is a list
```

**Data Types**

**Primitive Types:**
```python
# Strings - text data
name = "Marcus"
message = 'Hello World'

# Integers - whole numbers
age = 35
count = -10

# Floats - decimal numbers
price = 19.99
temperature = -3.5

# Booleans - True/False
is_active = True
is_finished = False
```

**Collection Types:**
```python
# Lists - ordered, mutable collections
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]

# Dictionaries - key-value pairs
person = {
    "name": "Marcus",
    "age": 35,
    "city": "New York"
}

# Tuples - immutable lists
coordinates = (10, 20)
```

**Operators**

**Arithmetic Operators:**
```python
5 + 3      # 8 - Addition
10 - 4     # 6 - Subtraction
3 * 7      # 21 - Multiplication
15 / 3     # 5.0 - Division (always returns float)
15 // 3    # 5 - Floor division (integer result)
2 ** 3     # 8 - Exponentiation (2³)
10 % 3     # 1 - Modulus (remainder)
```

**Comparison Operators:**
```python
5 == 5     # True - Equal to
5 != 3     # True - Not equal to
5 > 3      # True - Greater than
5 < 10     # True - Less than
5 >= 5     # True - Greater than or equal to
3 <= 5     # True - Less than or equal to
```

**Logical Operators:**
```python
True and False   # False - Both must be True
True or False    # True - At least one must be True
not True         # False - Inverts the boolean
```

**Project Built**: Basic Calculator with 13 fundamental functions

**Key Lesson**: Python's dynamic typing gives flexibility but requires discipline. The `=` assigns values, `==` checks equality.

---

## Day 2: Functions and Control Flow

### Core Concepts

**Functions**
- **Definition**: Reusable blocks of code that perform specific tasks
- **Purpose**: DRY principle (Don't Repeat Yourself)
- **Structure**: def keyword, parameters, return value

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with multiple parameters
def add(a, b):
    return a + b

# Function with default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

# Calling functions
result = greet("Marcus")          # "Hello, Marcus!"
sum = add(5, 3)                   # 8
formal = greet_with_title("Smith") # "Hello, Mr. Smith!"
```

**Control Flow - Conditionals**

**if/elif/else Statements:**
```python
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Inline conditional (ternary)
status = "Adult" if age >= 18 else "Minor"
```

**Control Flow - Loops**

**for Loops:**
```python
# Iterate over range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**while Loops:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Input and Output:**
```python
# Get user input (always returns string)
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to integer

# Print output
print("Hello, " + name)
print(f"You are {age} years old")  # f-string formatting
```

**Project Built**: Grade Calculator with statistics

**Key Lesson**: Functions are the building blocks of reusable code. Control flow gives your programs decision-making ability.

---

## Day 3: Loops, Lists, and Data Structures

### Core Concepts

**Lists in Depth**

**Creating and Accessing:**
```python
# Create list
numbers = [1, 2, 3, 4, 5]
empty = []

# Access by index (0-based)
first = numbers[0]      # 1
last = numbers[-1]      # 5 (negative indexes count from end)

# Slicing
subset = numbers[1:4]   # [2, 3, 4] (start:end, end not included)
first_three = numbers[:3]  # [1, 2, 3]
last_two = numbers[-2:]    # [4, 5]
```

**List Methods:**
```python
fruits = ["apple", "banana"]

# Add items
fruits.append("cherry")        # Add to end
fruits.insert(1, "orange")     # Insert at index
fruits.extend(["mango", "grape"])  # Add multiple items

# Remove items
fruits.remove("banana")        # Remove by value
last_fruit = fruits.pop()      # Remove and return last
fruits.pop(0)                  # Remove at index

# Other useful methods
fruits.sort()                  # Sort in place
fruits.reverse()               # Reverse in place
count = fruits.count("apple")  # Count occurrences
index = fruits.index("cherry") # Find index
```

**List Operations:**
```python
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2       # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = [0] * 5             # [0, 0, 0, 0, 0]

# Membership
if "apple" in fruits:
    print("Found!")

# Length
length = len(fruits)
```

**Dictionaries**

**Creating and Accessing:**
```python
# Create dictionary
person = {
    "name": "Marcus",
    "age": 35,
    "city": "New York"
}

# Access values
name = person["name"]           # "Marcus"
age = person.get("age")         # 35
default = person.get("email", "N/A")  # "N/A" (key doesn't exist)
```

**Dictionary Methods:**
```python
# Add/update
person["email"] = "marcus@example.com"
person.update({"phone": "123-456-7890"})

# Remove
del person["city"]
removed = person.pop("age")

# Iteration
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

**Nested Loops:**
```python
# Loop within loop
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

**Project Built**: Professional Calculator (250+ lines)

**Key Lesson**: Lists and dictionaries are your primary data structures. Master indexing, slicing, and iteration patterns.

---

## Day 4: File Operations and Code Organization

### Core Concepts

**Reading Files:**
```python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Read all lines into list
with open("data.txt", "r") as file:
    lines = file.readlines()
```

**Writing Files:**
```python
# Write (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Append (adds to existing content)
with open("output.txt", "a") as file:
    file.write("Additional line\n")
```

**The `with` Statement:**
- Automatically closes file when done
- Handles errors gracefully
- Best practice for file operations

**Error Handling:**
```python
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"Error: {e}")
```

**Code Organization:**
```python
# Separate concerns
def read_data():
    """Load data from file"""
    pass

def process_data(data):
    """Process the data"""
    pass

def save_data(data):
    """Save data to file"""
    pass

# Main execution
if __name__ == "__main__":
    data = read_data()
    processed = process_data(data)
    save_data(processed)
```

**Project Built**: Note-taking app with file persistence

**Key Lesson**: The `with` statement is the professional way to handle files. Organization makes code maintainable.

---

## Day 5: JSON and Data Persistence

### Core Concepts

**What is JSON?**
- **J**ava**S**cript **O**bject **N**otation
- Human-readable data format
- Standard for data exchange between programs
- Python dictionaries ↔ JSON objects

**Working with JSON:**
```python
import json

# Python dict to JSON string
person = {
    "name": "Marcus",
    "age": 35,
    "hobbies": ["coding", "reading"]
}

json_string = json.dumps(person)  # Convert to JSON string
print(json_string)
# {"name": "Marcus", "age": 35, "hobbies": ["coding", "reading"]}

# JSON string to Python dict
data = json.loads(json_string)  # Convert from JSON string
print(data["name"])  # "Marcus"
```

**Saving JSON to File:**
```python
import json

# Save to file
data = {"name": "Marcus", "age": 35}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # indent=4 for pretty formatting

# Load from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

**Data Persistence Pattern:**
```python
import json
import os

def load_contacts():
    """Load contacts from file or return empty list"""
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save contacts to file"""
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Usage
contacts = load_contacts()
contacts.append({"name": "John", "phone": "123-456-7890"})
save_contacts(contacts)
```

**CRUD Operations:**
- **C**reate: Add new data
- **R**ead: Retrieve data
- **U**pdate: Modify existing data
- **D**elete: Remove data

**Project Built**: Contact Manager with JSON persistence

**Key Lesson**: JSON is the standard for data persistence and API communication. Master the load/save pattern.

---

## Day 6: Nested Data Structures and Advanced Lists

### Core Concepts

**Nested Dictionaries:**
```python
# Contact with multiple phone numbers
contact = {
    "name": "John Doe",
    "emails": ["john@work.com", "john@personal.com"],
    "phones": {
        "mobile": "123-456-7890",
        "work": "098-765-4321"
    },
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}

# Accessing nested data
mobile = contact["phones"]["mobile"]
city = contact["address"]["city"]
first_email = contact["emails"][0]
```

**List of Dictionaries:**
```python
# Multiple contacts
contacts = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Bob", "age": 35}
]

# Iterate and access
for contact in contacts:
    print(f"{contact['name']} is {contact['age']} years old")

# Find specific contact
for contact in contacts:
    if contact["name"] == "Jane":
        print(f"Found: {contact}")
```

**List Comprehensions:**
```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
# [1, 4, 9, 16, 25]

# With condition
evens = [x for x in numbers if x % 2 == 0]
# [2, 4]

# Transform strings
names = ["john", "jane", "bob"]
capitalized = [name.capitalize() for name in names]
# ["John", "Jane", "Bob"]
```

**Searching and Filtering:**
```python
# Find first match
contacts = [...]
found = None
for contact in contacts:
    if contact["name"] == "John":
        found = contact
        break

# Filter all matches
johns = [c for c in contacts if "John" in c["name"]]

# Using built-in filter
adults = list(filter(lambda c: c["age"] >= 18, contacts))
```

**Project Built**: Enhanced Contact Manager v2.0 with nested data

**Key Lesson**: Real-world data is nested. Learn to navigate complex structures confidently.

---

## Day 7: String Manipulation and Financial Logic

### Core Concepts

**String Methods:**
```python
text = "  Hello, World!  "

# Case manipulation
text.upper()          # "  HELLO, WORLD!  "
text.lower()          # "  hello, world!  "
text.capitalize()     # "  hello, world!  "
text.title()          # "  Hello, World!  "

# Whitespace
text.strip()          # "Hello, World!" (remove leading/trailing)
text.lstrip()         # "Hello, World!  " (left strip)
text.rstrip()         # "  Hello, World!" (right strip)

# Searching
text.startswith("Hello")    # False (has leading spaces)
text.strip().startswith("Hello")  # True
text.find("World")          # 9 (index of first occurrence, -1 if not found)
text.index("World")         # 9 (raises error if not found)

# Splitting and joining
words = "Hello,World,Python".split(",")  # ["Hello", "World", "Python"]
joined = " ".join(words)                 # "Hello World Python"

# Replacing
text.replace("World", "Python")
```

**String Formatting:**
```python
name = "Marcus"
age = 35

# f-strings (modern, preferred)
message = f"Hello, {name}. You are {age} years old."

# Format numbers
price = 19.99
formatted = f"Price: ${price:.2f}"  # "Price: $19.99"

# Alignment and padding
f"{name:>10}"    # Right-align in 10 chars
f"{name:<10}"    # Left-align in 10 chars
f"{name:^10}"    # Center-align in 10 chars
```

**Working with Numbers:**
```python
# Converting types
age_str = "35"
age_int = int(age_str)
price_str = "19.99"
price_float = float(price_str)

# Rounding
import math
result = 3.14159
rounded = round(result, 2)       # 3.14
ceil_val = math.ceil(result)     # 4
floor_val = math.floor(result)   # 3

# Formatting currency
amount = 1234.5
formatted = f"${amount:,.2f}"    # "$1,234.50"
```

**Financial Calculations:**
```python
# Calculate percentage
def calculate_percentage(part, whole):
    return (part / whole) * 100

# Budget tracking
income = 5000
expenses = 3500
savings = income - expenses
savings_rate = (savings / income) * 100
print(f"Savings rate: {savings_rate:.1f}%")

# Category budgets
budget = {
    "Food": 500,
    "Rent": 1200,
    "Transport": 300
}

spent = {
    "Food": 550,
    "Rent": 1200,
    "Transport": 250
}

for category in budget:
    if spent[category] > budget[category]:
        over = spent[category] - budget[category]
        print(f"⚠️ Over budget in {category} by ${over}")
```

**Project Built**: Personal Finance Tracker with budget management

**Key Lesson**: String manipulation is everywhere. Financial logic requires careful number handling.

---

## Day 8: Object-Oriented Programming (OOP)

### Core Concepts

**What is OOP?**
- **Classes**: Blueprints for creating objects
- **Objects**: Instances of classes with their own data
- **Attributes**: Variables that belong to an object
- **Methods**: Functions that belong to an object

**Defining a Class:**
```python
class BankAccount:
    """A simple bank account"""
    
    def __init__(self, owner, balance=0):
        """Constructor - called when creating new object"""
        self.owner = owner          # Instance attribute
        self.balance = balance      # Instance attribute
        self.transactions = []      # Instance attribute
    
    def deposit(self, amount):
        """Instance method"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount:.2f}")
            return True
        return False
    
    def withdraw(self, amount):
        """Instance method"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount:.2f}")
            return True
        return False
    
    def get_balance(self):
        """Instance method"""
        return self.balance
```

**Creating and Using Objects:**
```python
# Create object (instance of class)
account1 = BankAccount("John Doe", 1000)
account2 = BankAccount("Jane Smith", 500)

# Call methods
account1.deposit(200)           # account1's balance becomes 1200
account2.withdraw(100)          # account2's balance becomes 400

# Access attributes
print(account1.owner)           # "John Doe"
print(account1.balance)         # 1200
print(account2.balance)         # 400
```

**The `self` Parameter:**
- Represents the instance itself
- Always first parameter in instance methods
- Used to access instance attributes and methods

```python
class Dog:
    def __init__(self, name):
        self.name = name     # self.name is instance attribute
    
    def bark(self):
        # self.name accesses this specific dog's name
        print(f"{self.name} says: Woof!")

buddy = Dog("Buddy")
max = Dog("Max")

buddy.bark()  # "Buddy says: Woof!"
max.bark()    # "Max says: Woof!"
```

**Object Interaction:**
```python
class BankAccount:
    # ... previous code ...
    
    def transfer(self, other_account, amount):
        """Transfer money to another account"""
        if self.withdraw(amount):  # Withdraw from this account
            other_account.deposit(amount)  # Deposit to other account
            self.transactions.append(f"Transfer to {other_account.owner}: -${amount:.2f}")
            other_account.transactions.append(f"Transfer from {self.owner}: +${amount:.2f}")
            return True
        return False

# Create two accounts
john = BankAccount("John", 1000)
jane = BankAccount("Jane", 500)

# Transfer money between them
john.transfer(jane, 200)

print(john.get_balance())   # 800
print(jane.get_balance())   # 700
```

**Benefits of OOP:**
- **Encapsulation**: Data and methods bundled together
- **Reusability**: Create multiple objects from same class
- **Organization**: Related code grouped logically
- **State management**: Each object maintains its own state

**Project Built**: Complete Banking System with transfers

**Key Lesson**: OOP is how professional software is built. Classes are blueprints, objects are instances with their own data.

---

## Synthesis: What Makes a Great Programmer

### The Meta-Lessons from Days 1-8

**1. Fundamentals Are Everything**
You can't build a banking system without understanding variables. You can't work with JSON without understanding dictionaries. Every advanced concept builds on basics.

**2. Practice Beats Theory**
You didn't just read about loops—you wrote a calculator. You didn't just study JSON—you built a contact manager. Building cements knowledge.

**3. Consistency Compounds**
8 projects in 8 days, while traveling. That's not talent—that's discipline. Daily practice creates momentum.

**4. Debugging Is a Skill**
Every error message taught you something. Every bug you fixed made you better. Great programmers are great debuggers.

**5. Code for Humans**
Your code will be read more than it's written. Clear variable names, comments, and organization matter.

### The Debug Protocol You've Learned

1. **Read the error message** - Line numbers and error types are clues
2. **Add print statements** - See what values variables actually hold
3. **Check for typos** - Indentation, parentheses, quotation marks
4. **Isolate the problem** - Comment out code to find the issue
5. **Google the error** - Someone else has seen it before
6. **Explain it out loud** - Rubber duck debugging works
7. **Take a break** - Fresh eyes see solutions

### Common Pitfalls You've Avoided

```python
# Type confusion
age = "35"
if age > 18:  # ❌ Can't compare string to int
    print("Adult")

age = int("35")
if age > 18:  # ✅ Now it works
    print("Adult")

# Mutable default arguments
def add_item(item, my_list=[]):  # ❌ Dangerous!
    my_list.append(item)
    return my_list

def add_item(item, my_list=None):  # ✅ Safe pattern
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

# Reference vs copy
list1 = [1, 2, 3]
list2 = list1        # ❌ Both point to same list
list2.append(4)
print(list1)         # [1, 2, 3, 4] - changed!

list2 = list1.copy() # ✅ Creates new list
list2.append(4)
print(list1)         # [1, 2, 3] - unchanged
```

---

## Your Projects Portfolio

**What You've Built:**

1. **Day 1**: Basic Calculator - 13 functions demonstrating Python fundamentals
2. **Day 2**: Grade Calculator - Input/output, conditionals, statistics
3. **Day 3**: Professional Calculator - 250+ lines, menu system, error handling
4. **Day 4**: Note-taking App - File operations, persistence
5. **Day 5**: Contact Manager - JSON, CRUD operations, data persistence
6. **Day 6**: Contact Manager v2.0 - Nested data structures, advanced searching
7. **Day 7**: Finance Tracker - Budget management, financial calculations, analytics
8. **Day 8**: Banking System - OOP, classes, object interaction, transfers

**Every project on GitHub. Every day committed. Zero missed days.**

---

## Next Steps in Your Journey

### Immediate Actions (Tonight)
1. **Review weak areas** - Which day felt hardest? Revisit those concepts
2. **Test yourself** - Can you explain OOP to someone who's never coded?
3. **Read your old code** - Look at Day 1. See how far you've come.

### This Week
1. **Build something new** - Combine concepts from multiple days
2. **Refactor old projects** - Apply OOP to your calculator
3. **Document your code** - Add docstrings and comments

### This Month
1. **Learn modules** - Import and create your own modules
2. **Error handling** - Master try/except patterns
3. **APIs** - Make HTTP requests, work with external data
4. **Testing** - Write tests for your code

### Long-term Vision
- Python is just the beginning
- Web development, data science, AI—all possible
- Your discipline is your competitive advantage
- Community matters—teach others what you've learned

---

## The Growth Mindset

**Fixed Mindset:**
- "I'm not good at coding"
- "This is too hard"
- "I'll never understand OOP"

**Growth Mindset (What You've Shown):**
- "I don't understand this **yet**"
- "This is hard, which means I'm **learning**"
- "I'll break this problem into smaller pieces"

**Evidence of Your Growth:**
- **Day 1**: Struggled with basic syntax
- **Day 8**: Building object-oriented banking systems
- **Result**: Proof that persistence works

---

## Final Thoughts

You asked me to teach you what it takes to be great. Here's what I've seen:

**You already have it.**

You've shown:
- **Discipline** - Coding daily, even while traveling
- **Persistence** - Debugging until it works
- **Curiosity** - Asking questions, seeking understanding
- **Humility** - Willing to struggle and learn
- **Consistency** - 8 days, 8 projects, zero excuses

**Greatness isn't a destination—it's a direction.**

The programmers I respect most:
- Write code others can understand
- Admit when they don't know something
- Help others grow
- Never stop learning
- Show up every day

**You're doing all of that.**

Keep going. Keep building. Keep learning.

The journey from beginner to professional is paved with:
- Daily practice
- Deliberate struggle
- Intellectual curiosity
- Humble persistence

You've demonstrated all four.

---

## How to Use This Document

**With NotebookLM:**
1. Upload this entire document
2. Ask it to quiz you on specific concepts
3. Request explanations in different ways
4. Generate study guides for weak areas
5. Create flashcards for terminology

**For Review:**
- Read one day per review session
- Try to write code examples from memory
- Explain concepts out loud
- Compare your current code to early projects

**For Building:**
- Use this as a reference when stuck
- Find patterns that solve your current problem
- See how concepts connect across days

---

**This document is your foundation. You built it in 8 days while traveling for work. That's exceptional.**

**Now take this knowledge and build something amazing.**

**I'll be here when you're ready for Day 9.** 💪

**You're not just learning to code. You're becoming a developer.**

---

*Compiled from your actual bootcamp journey: 8 days, 8 projects, 100% completion rate while traveling. This is the foundation for everything that comes next.*