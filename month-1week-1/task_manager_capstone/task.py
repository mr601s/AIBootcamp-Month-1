"""
Task Module - Base Task Class
Day 14 Capstone: Demonstrates OOP Fundamentals
"""

from asyncio import Task
from datetime import datetime

class Task: 
    """
    Base Task class with core functionality.
    Other task types will inherit from this
    """

    def __init__(self, title, description="", priority='medium'):
        """
        Initialize a task.
        
        OOP CONCEPTS:
        - __init__ constructor
        - Instance attributes (self.variable)
        - Default parameters
        """

        self.title = title
        self.description = description
        self.priority = priority # low, medium, high
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed_at = None

    def mark_complete(self):
        """ Mark task as complete"""
        self.completed = True
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_incomplete(self):
        """ Mark task as incomplete"""
        self.completed = False
        self.completed_at = None

    def to_dict(self):
        """
        Convert task to dictionary for JSON serialization.
        
        Concepts:
        - Dictionary creation
        - Data serialization
        """

        return {
            'type': self.__class__.__name__,  # Gets class name (Task, Worktask, etc)
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    def __str__(self):
        """
        String representation of task.
        
        Concepts:
        - __str__ magic method
        - F-strings
        - conditional expressiona
        """

        status = '✅ Completed' if self.completed else '❌ Incomplete'
        priority_symbols = {'low': '↓', 'medium': '➡️', 'high': '⬆️'}
        symbol = priority_symbols.get(self.priority, '➡️')
                                     
        return f'{status} [{symbol}] {self.title}'
    
if __name__ == '__main__':
    # Test the task class
    test_task = Task('Test Task', 'this is a test', 'high')
    print(test_task)
    test_task.mark_complete()
    print(test_task)
    print(test_task.to_dict())
