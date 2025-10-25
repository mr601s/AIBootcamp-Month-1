"""
Task Manager - Main Application
Day 14 Capstone: Week 2 Complete Application
FIXED VERSION: Added screen clearing for better UX
"""

import os
from task_manager import TaskManager


def clear_screen():
    """
    Clear the terminal screen (cross-platform).
    
    CONCEPTS:
    - os.system() for system commands
    - os.name for platform detection
    - Cross-platform compatibility
    """
    # Windows uses 'cls', Unix/Linux/Mac use 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """Display the main menu with screen clearing."""
    clear_screen()  # Clear screen before showing menu
    print("="*60)
    print("TASK MANAGER".center(60))
    print("Week 2 Capstone Project".center(60))
    print("="*60)
    print()
    print("1. View All Tasks")
    print("2. View Incomplete Tasks")
    print("3. Add New Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. View Statistics")
    print("7. Get Weather Advice")
    print("8. Filter Tasks")
    print("9. Exit")
    print("-"*60)


def view_tasks(manager, tasks=None, title="All Tasks"):
    """Display tasks with improved formatting."""
    clear_screen()  # Clear before showing tasks
    print("="*60)
    print(title.center(60))
    print("="*60)
    
    if tasks is None:
        tasks = manager.tasks
    
    if not tasks:
        print("\nNo tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"\n{i}. {task}")
            if hasattr(task, 'project'):
                print(f"   Project: {task.project}")
            if hasattr(task, 'location'):
                print(f"   Location: {task.location}")
            if hasattr(task, 'items'):
                print(f"   Items: {', '.join(task.items)}")
            print(f"   Created: {task.created_at}")
            if task.completed:
                print(f"   Completed: {task.completed_at}")
    
    print("="*60)


def add_task(manager):
    """Add a new task with improved UX."""
    clear_screen()
    print("-"*60)
    print("ADD NEW TASK".center(60))
    print("-"*60)
    
    # Task type selection
    print("\nTask Type:")
    print("1. Work Task")
    print("2. Personal Task")
    print("3. Shopping Task")
    print("4. General Task")
    
    type_choice = input("Select type (1-4): ").strip()
    
    # Get common fields
    title = input("Task title: ").strip()
    if not title:
        print("❌ Title cannot be empty!")
        input("\nPress ENTER to continue...")
        return
    
    description = input("Description (optional): ").strip()
    
    # Priority selection
    print("\nPriority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    priority_choice = input("Select (1-3, default 2): ").strip() or "2"
    priority_map = {"1": "low", "2": "medium", "3": "high"}
    priority = priority_map.get(priority_choice, "medium")
    
    # Create task based on type
    if type_choice == "1":
        project = input("Project name: ").strip()
        task = manager.add_work_task(title, description, priority, project)
    elif type_choice == "2":
        location = input("Location: ").strip()
        task = manager.add_personal_task(title, description, priority, location)
    elif type_choice == "3":
        items_input = input("Items (comma-separated): ").strip()
        items = [item.strip() for item in items_input.split(",")] if items_input else []
        task = manager.add_shopping_task(title, description, priority, items)
    else:
        task = manager.add_task(title, description, priority)
    
    if task:
        print(f"\n✓ Task '{title}' added successfully!")
    else:
        print("\n❌ Failed to add task")
    
    input("\nPress ENTER to continue...")


def complete_task(manager):
    """Mark a task as complete."""
    tasks = manager.get_incomplete_tasks()
    
    if not tasks:
        clear_screen()
        print("\n✓ No incomplete tasks!")
        input("\nPress ENTER to continue...")
        return
    
    view_tasks(manager, tasks, "Incomplete Tasks")
    
    try:
        choice = int(input("\nSelect task number to complete (0 to cancel): "))
        if choice == 0:
            return
        
        if 1 <= choice <= len(tasks):
            task = tasks[choice - 1]
            task.mark_complete()
            manager.save_tasks()
            print(f"\n✓ Task '{task.title}' marked as complete!")
        else:
            print("\n❌ Invalid task number")
    except ValueError:
        print("\n❌ Please enter a valid number")
    
    input("\nPress ENTER to continue...")


def delete_task(manager):
    """Delete a task."""
    view_tasks(manager)
    
    if not manager.tasks:
        input("\nPress ENTER to continue...")
        return
    
    try:
        choice = int(input("\nSelect task number to delete (0 to cancel): "))
        if choice == 0:
            return
        
        if 1 <= choice <= len(manager.tasks):
            task = manager.tasks[choice - 1]
            title = task.title
            manager.delete_task(task)
            print(f"\n✓ Task '{title}' deleted!")
        else:
            print("\n❌ Invalid task number")
    except ValueError:
        print("\n❌ Please enter a valid number")
    
    input("\nPress ENTER to continue...")


def view_statistics(manager):
    """Display task statistics."""
    clear_screen()
    stats = manager.get_statistics()
    
    print("="*60)
    print("TASK STATISTICS".center(60))
    print("="*60)
    print(f"\nTotal Tasks: {stats['total']}")
    print(f"Completed: {stats['completed']}")
    print(f"Incomplete: {stats['incomplete']}")
    print(f"Completion Rate: {stats['completion_rate']:.1f}%")
    
    print("\n" + "-"*60)
    print("BY PRIORITY:")
    for priority, count in stats['by_priority'].items():
        print(f"  {priority.capitalize()}: {count}")
    
    print("\n" + "-"*60)
    print("BY CATEGORY:")
    for category, count in stats['by_category'].items():
        print(f"  {category}: {count}")
    
    print("="*60)
    input("\nPress ENTER to continue...")


def get_weather_advice(manager):
    """Get weather-based task advice."""
    clear_screen()
    print("="*60)
    print("WEATHER-BASED TASK ADVICE".center(60))
    print("="*60)
    
    city = input("\nEnter your city: ").strip()
    
    if not city:
        print("\n❌ City name cannot be empty!")
        input("\nPress ENTER to continue...")
        return
    
    print(f"\nFetching weather for {city}...")
    advice = manager.get_weather_advice(city)
    
    print("\n" + "="*60)
    print("WEATHER-BASED TASK ADVICE".center(60))
    print("="*60)
    print(advice)
    print("="*60)
    
    input("\nPress ENTER to continue...")


def filter_tasks(manager):
    """Filter tasks by criteria."""
    clear_screen()
    print("="*60)
    print("FILTER TASKS".center(60))
    print("="*60)
    
    print("\nFilter by:")
    print("1. Priority")
    print("2. Category")
    
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
            input("\nPress ENTER to continue...")
    
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
            input("\nPress ENTER to continue...")


def main():
    """Main application loop with improved flow."""
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("\nSelect option (1-9): ").strip()
        
        if choice == "1":
            view_tasks(manager)
            input("\nPress ENTER to continue...")
        elif choice == "2":
            view_tasks(manager, manager.get_incomplete_tasks(), "Incomplete Tasks")
            input("\nPress ENTER to continue...")
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
            clear_screen()
            print("\n✓ Tasks saved. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid option. Please select 1-9.")
            input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()