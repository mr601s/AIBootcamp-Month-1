"""
File Handler Module
Day 14 Capstone: Demonstrates JSON persistence
"""

import json
import os


class FileHandler:
    """
    Handles loading and saving tasks to JSON.
    
    FILE I/O CONCEPTS:
    - JSON serialization/deserialization
    - File operations
    - Error handling
    """
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save_tasks(self, tasks):
        """
        Save task list to JSON file.
        
        CONCEPTS:
        - Converting objects to dictionaries
        - JSON serialization
        - File writing
        """
        try:
            # Convert all tasks to dictionaries
            task_dicts = [task.to_dict() for task in tasks]
            
            # Write to file
            with open(self.filename, 'w') as f:
                json.dump(task_dicts, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def load_tasks(self):
        """
        Load tasks from JSON file.
        
        Returns:
            List of task dictionaries (not Task objects)
            This allows TaskManager to recreate appropriate Task types
        """
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []
    
    def file_exists(self):
        """Check if data file exists"""
        return os.path.exists(self.filename)


if __name__ == "__main__":
    # Test file handler
    from task import Task
    
    handler = FileHandler("test_tasks.json")
    
    # Create test tasks
    tasks = [
        Task("Test Task 1", "Description 1", "high"),
        Task("Test Task 2", "Description 2", "low")
    ]
    
    print("Testing File Handler...")
    print("="*60)
    
    # Save
    print("\nSaving tasks...")
    if handler.save_tasks(tasks):
        print("✓ Tasks saved successfully")
    
    # Load
    print("\nLoading tasks...")
    loaded = handler.load_tasks()
    print(f"✓ Loaded {len(loaded)} tasks")
    
    for task_data in loaded:
        print(f"  - {task_data['title']} [{task_data['priority']}]")
    
    # Cleanup
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")
        print("\n✓ Test file cleaned up")