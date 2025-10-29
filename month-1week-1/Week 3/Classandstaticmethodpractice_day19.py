class Person:
    population = 0 # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    # Regular instance method (uses self)
    def greet(self):
        return f"Hi, I'm {self.name}"
    
    # Class method (uses cls, not self)
    @classmethod
    def get_population(cls):
        return f'Total people: {cls.population}'
    
    # Class method as factory (alternative constructor)
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth birth_year
        return cls(name, age) # Create instance 
    
    # Static method (no self, no cls)
    @staticmethod
    def is_adult(age):
        return age >= 18
    
# Usage
person1= Person('Alice', 25)
person2 = Person('Bob', 30)

# Instance method
print(person1.greet()) # Hi, I'm Alice

# Class method
print(Person.get_population()) # Total people: 2

# Class method as factory 
person3 = Person.from_birth_year('Charlie', 2000)
print(person3.age)  # 25

# Static method
print(Person.is_adult(20)) # True 
print(Person.is.adult(16)) # False
