"""
Task Types Module - Specialized Task Classes
Day 14 Capstone: Demonstrates Inheritance and Polymorphism
"""

from task import Task

class WorkTask(Task):
    """
    Work-related task with project tracking.
    
    Inheritance concept:
    - Extends Task class
    - Adds work-specific features
    """

    def __init__(self, title, description='', priority='medium', project='General'):
        """
        Initialize work task.
        
        Concepts:
        - super() to call parent constructor
        = Additional attributes for child class
        """

        super().__init__(title, description, priority)
        self.project = project
        self.category = 'Work'

    def __str__(self):
        """Override string representation"""
        base = super().__str__()
        return f'{base} [Project: {self.project}]'
    
class PersonalTask(Task):
    """Personal/Life task with location"""

    def __init__(self, title, description='', priority='medium', location='home'):
        super().__init__(title, description, priority)
        self.location = location
        self.category = 'Personal'

    def to_dict(self):
        data = super().to_dict()
        data['location'] = self.location
        data['category'] = self.category
        return data 
    
    def __str__(self):
        base = super().__str__()
        return f'{base} [@{self.location}]'
    
class ShoppingTask(Task):
    """Shopping task with item list"""

    def __init__(self, title, description='', priority='medium'):
        super().__init__(title, description, priority)
        self.items = []
        self.category = 'Shopping'

    def add_item(self, item):
        """Add item to shopping list"""
        self.items.append(item)

    def to_dict(self):
        data = super().to_dict()
        data['items'] = self.items
        data['category'] = self.category
        return data
    
    def __str__(self):
        base = super().__str__()
        item_count = len(self.items)
        return f'{base} [{item_count} items]'
    
if __name__ == '__main__':
    # Test Inheritances
    work = WorkTask('finish report', 'Q4 analysis', 'high', 'analytics')
    personal = PersonalTask('doctor appointment', priority='high', location='Clinic')
    shopping = ShoppingTask('grocery Shopping', priority='medium')
    shopping.add_item('milk')
    shopping.add_item('Bread')

    print(work)
    print(personal)
    print(shopping)
