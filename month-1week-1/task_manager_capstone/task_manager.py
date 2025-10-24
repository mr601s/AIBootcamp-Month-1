"""
Task Manager Module
Day 14 Capstone: Demonstrates OOP management and polymorphism
"""

from task import Task
from task_types import WorkTask, PersonalTask, ShoppingTask
from file_handler import FileHandler
from weather_service import WeatherService


class TaskManager:
    """
    Manages all tasks with CRUD operations.
    
    DEMONSTRATES:
    - Managing collections of objects
    - Polymorphism (working with different task types)
    - Integration of multiple modules
    """
    
    def __init__(self):
        self.tasks = []
        self.file_handler = FileHandler()
        self.weather_service = WeatherService()
        self.load_tasks()
    
    def add_task(self, task):
        """Add a task to the manager"""
        self.tasks.append(task)
        self.save_tasks()
        return True
    
    def get_all_tasks(self):
        """Get all tasks"""
        return self.tasks
    
    def get_incomplete_tasks(self):
        """Get only incomplete tasks"""
        return [t for t in self.tasks if not t.completed]
    
    def get_completed_tasks(self):
        """Get only completed tasks"""
        return [t for t in self.tasks if t.completed]
    
    def get_tasks_by_priority(self, priority):
        """Get tasks by priority level"""
        return [t for t in self.tasks if t.priority == priority]
    
    def get_tasks_by_category(self, category):
        """Get tasks by category (Work, Personal, Shopping)"""
        return [t for t in self.tasks 
                if hasattr(t, 'category') and t.category == category]
    
    def complete_task(self, index):
        """Mark a task as complete"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, index):
        """Delete a task"""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            return True
        return False
    
    def save_tasks(self):
        """Save all tasks to file"""
        return self.file_handler.save_tasks(self.tasks)
    
    def load_tasks(self):
        """
        Load tasks from file and reconstruct proper Task objects.
        
        DEMONSTRATES:
        - Polymorphism in action
        - Dynamic object creation based on data
        """
        task_dicts = self.file_handler.load_tasks()
        
        for task_data in task_dicts:
            task_type = task_data.get('type', 'Task')
            
            # Recreate appropriate task type based on saved data
            if task_type == 'WorkTask':
                task = WorkTask(
                    task_data['title'],
                    task_data['description'],
                    task_data['priority'],
                    task_data.get('project', 'General')
                )
            elif task_type == 'PersonalTask':
                task = PersonalTask(
                    task_data['title'],
                    task_data['description'],
                    task_data['priority'],
                    task_data.get('location', 'Home')
                )
            elif task_type == 'ShoppingTask':
                task = ShoppingTask(
                    task_data['title'],
                    task_data['description'],
                    task_data['priority']
                )
                task.items = task_data.get('items', [])
            else:
                task = Task(
                    task_data['title'],
                    task_data['description'],
                    task_data['priority']
                )
            
            # Restore completion status
            if task_data['completed']:
                task.completed = True
                task.completed_at = task_data['completed_at']
            
            # Restore creation time
            task.created_at = task_data['created_at']
            
            self.tasks.append(task)
    
    def get_weather_advice(self, city):
        """Get weather-based task advice"""
        return self.weather_service.get_weather_advice(city)
    
    def get_statistics(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = len(self.get_completed_tasks())
        incomplete = len(self.get_incomplete_tasks())
        
        high = len(self.get_tasks_by_priority('high'))
        medium = len(self.get_tasks_by_priority('medium'))
        low = len(self.get_tasks_by_priority('low'))
        
        return {
            'total': total,
            'completed': completed,
            'incomplete': incomplete,
            'completion_rate': (completed / total * 100) if total > 0 else 0,
            'high_priority': high,
            'medium_priority': medium,
            'low_priority': low
        }


if __name__ == "__main__":
    # Test TaskManager
    manager = TaskManager()
    
    # Add test tasks
    manager.add_task(WorkTask("Write documentation", priority="high", project="Documentation"))
    manager.add_task(PersonalTask("Buy groceries", priority="medium", location="Store"))
    
    print("Testing Task Manager...")
    print("="*60)
    print(f"\nTotal tasks: {len(manager.get_all_tasks())}")
    
    print("\nAll tasks:")
    for i, task in enumerate(manager.get_all_tasks()):
        print(f"  {i}. {task}")
    
    print("\nStatistics:")
    stats = manager.get_statistics()
    print(f"  Total: {stats['total']}")
    print(f"  Completed: {stats['completed']}")
    print(f"  Incomplete: {stats['incomplete']}")
    print(f"  High Priority: {stats['high_priority']}")