"""
Task Manager Capstone - Main Application
Day 14: Week 2 Capstone Project

DEMONSTRATES ALL WEEK 2 SKILLS:
- OOP (Classes, Inheritance, Polymorphism)
- Modules (Multi-file architecture)
- APIs (Weather integration)
- File I/O (JSON persistence)
"""

from task_manager import TaskManager
from task_types import WorkTask, PersonalTask, ShoppingTask


def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print(" "*15 + "TASK MANAGER")
    print(" "*10 + "Week 2 Capstone Project")
    print("="*60)
    print("\n1. View All Tasks")
    print("2. View Incomplete Tasks")
    print("3. Add New Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. View Statistics")
    print("7. Get Weather Advice")
    print("8. Filter Tasks")
    print("9. Exit")
    print("-"*60)


def view_tasks(manager, task_list=None, title="All Tasks"):
    """Display tasks"""
    if task_list is None:
        task_list = manager.get_all_tasks()
    
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    
    if not task_list:
        print("No tasks found.")
    else:
        for i, task in enumerate(task_list):
            print(f"{i}. {task}")
    
    print(f"{'='*60}")


def add_task(manager):
    """Add a new task"""
    print("\n" + "-"*60)
    print("ADD NEW TASK")
    print("-"*60)
    print("Task Type:")
    print("  1. Work Task")
    print("  2. Personal Task")
    print("  3. Shopping Task")
    print("  4. General Task")
    
    task_type = input("\nSelect type (1-4): ").strip()
    
    title = input("Task title: ").strip()
    if not title:
        print("❌ Title required")
        return
    
    description = input("Description (optional): ").strip()
    
    print("\nPriority:")
    print("  1. Low")
    print("  2. Medium")
    print("  3. High")
    priority_choice = input("Select (1-3, default 2): ").strip() or "2"
    priority_map = {"1": "low", "2": "medium", "3": "high"}
    priority = priority_map.get(priority_choice, "medium")
    
    # Create appropriate task type
    if task_type == "1":
        project = input("Project name: ").strip() or "General"
        task = WorkTask(title, description, priority, project)
    elif task_type == "2":
        location = input("Location: ").strip() or "Home"
        task = PersonalTask(title, description, priority, location)
    elif task_type == "3":
        task = ShoppingTask(title, description, priority)
        items_input = input("Shopping items (comma-separated): ").strip()
        if items_input:
            for item in items_input.split(','):
                task.add_item(item.strip())
    else:
        from task import Task
        task = Task(title, description, priority)
    
    manager.add_task(task)
    print(f"\n✓ Task '{title}' added successfully!")


def complete_task(manager):
    """Mark a task as complete"""
    view_tasks(manager, manager.get_incomplete_tasks(), "Incomplete Tasks")
    
    try:
        index = int(input("\nEnter task number to complete: "))
        if manager.complete_task(index):
            print(f"✓ Task marked as complete!")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Please enter a valid number")


def delete_task(manager):
    """Delete a task"""
    view_tasks(manager)
    
    try:
        index = int(input("\nEnter task number to delete: "))
        if manager.delete_task(index):
            print(f"✓ Task deleted!")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Please enter a valid number")


def view_statistics(manager):
    """Display statistics"""
    stats = manager.get_statistics()
    
    print(f"\n{'='*60}")
    print("TASK STATISTICS")
    print(f"{'='*60}")
    print(f"Total Tasks:         {stats['total']}")
    print(f"Completed:           {stats['completed']}")
    print(f"Incomplete:          {stats['incomplete']}")
    print(f"Completion Rate:     {stats['completion_rate']:.1f}%")
    print(f"\nPriority Breakdown:")
    print(f"  High Priority:     {stats['high_priority']}")
    print(f"  Medium Priority:   {stats['medium_priority']}")
    print(f"  Low Priority:      {stats['low_priority']}")
    print(f"{'='*60}")


def get_weather_advice(manager):
    """Get weather-based task advice"""
    city = input("\nEnter your city: ").strip() or "New York"
    
    print(f"\nFetching weather for {city}...")
    advice = manager.get_weather_advice(city)
    
    print(f"\n{'='*60}")
    print("WEATHER-BASED TASK ADVICE")
    print(f"{'='*60}")
    print(advice)
    print(f"{'='*60}")


def filter_tasks(manager):
    """Filter tasks by category or priority"""
    print("\n" + "-"*60)
    print("FILTER TASKS")
    print("-"*60)
    print("1. By Priority")
    print("2. By Category")
    
    choice = input("\nSelect filter (1-2): ").strip()
    
    if choice == "1":
        print("\n1. High")
        print("2. Medium")
        print("3. Low")
        priority_choice = input("Select priority (1-3): ").strip()
        priority_map = {"1": "high", "2": "medium", "3": "low"}
        priority = priority_map.get(priority_choice)
        
        if priority:
            tasks = manager.get_tasks_by_priority(priority)
            view_tasks(manager, tasks, f"{priority.capitalize()} Priority Tasks")
    
    elif choice == "2":
        print("\n1. Work")
        print("2. Personal")
        print("3. Shopping")
        cat_choice = input("Select category (1-3): ").strip()
        cat_map = {"1": "Work", "2": "Personal", "3": "Shopping"}
        category = cat_map.get(cat_choice)
        
        if category:
            tasks = manager.get_tasks_by_category(category)
            view_tasks(manager, tasks, f"{category} Tasks")


def main():
    """Main application loop"""
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("\nSelect option (1-9): ").strip()
        
        if choice == "1":
            view_tasks(manager)
        elif choice == "2":
            view_tasks(manager, manager.get_incomplete_tasks(), "Incomplete Tasks")
        elif choice == "3":
            add_task(manager)
        elif choice == "4":
            complete_task(manager)
        elif choice == "5":
            delete_task(manager)
        elif choice == "6":
            view_statistics(manager)
        elif choice == "7":
            get_weather_advice(manager)
        elif choice == "8":
            filter_tasks(manager)
        elif choice == "9":
            print("\n✓ Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please select 1-9.")
        
        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()