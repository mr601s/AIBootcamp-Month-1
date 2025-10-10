# Day 3: Calculator with History and Continuous Operation

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract second number from first"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide first number by second"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def get_number(prompt):
    """
    Get a valid number from user with error handling
    Keeps asking until valid number is entered
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def perform_calculation(num1, operation, num2):
    """
    Perform the calculation based on operation
    Returns tuple: (result, calculation_string)
    """
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        return None, "Invalid operation"
    
    # Create readable calculation string
    calc_string = f"{num1} {operation} {num2} = {result}"
    return result, calc_string


def basic_calculator():
    """
    Basic calculator - single calculation then exits
    This is your starting point
    """
    print("="*50)
    print("BASIC CALCULATOR")
    print("="*50)

    # Get inputs
    num1 = get_number("Enter first number: ")
    operation = input("Enter operation (+, -, *, /): ")
    num2 = get_number("Enter second number: ")

    # Perform calculation
    result, calc_string = perform_calculation(num1, operation, num2)

    # Display result
    print(f"\n{calc_string}\n")


def continuous_calculator():
    """
    Calculator that keeps running until user quits
    Introduces while loop and program flow control
    """
    print("="*50)
    print("CONTINUOUS CALCULATOR")
    print("="*50)
    print("Type 'quit' at any time to exit\n")

    while True:  # Infinite loop - runs until we break
        # Get first number
        user_input = input("Enter first number (or 'quit'): ")
        if user_input.lower() == 'quit':
            print("\nThank you for using the calculator!")
            break  # Exit the loop
        
        try:
            num1 = float(user_input)
        except ValueError:
            print("❌ Invalid number! Try again.\n")
            continue  # Skip rest of loop, start over
        
        # Get operation
        operation = input("Enter operation (+, -, *, /): ")
        if operation not in ['+', '-', '*', '/']:
            print("❌ Invalid operation! Use +, -, *, or /\n")
            continue
        
        # Get second number
        num2 = get_number("Enter second number: ")

        # Perform calculation
        result, calc_string = perform_calculation(num1, operation, num2)

        # Display result
        print(f"\n✓ {calc_string}\n")
        print("-"*50 + "\n")

def professional_calculator():
    """
    Production-ready calculator with all features
    """
    print("="*60)
    print("PROFESSIONAL CALCULATOR v1.0")
    print("="*60)
    print("\n📱 COMMANDS:")
    print("  calc     - Start new calculation")
    print("  history  - View calculation history")
    print("  stats    - View session statistics")
    print("  clear    - Clear history")
    print("  help     - Show this menu")
    print("  quit     - Exit calculator")
    print("="*60 + "\n")
    
    history = []
    
    while True:
        command = input("Enter command or number: ").strip().lower()
        
        # QUIT COMMAND
        if command == 'quit':
            print(f"\n✓ Session complete! You performed {len(history)} calculations.")
            if len(history) > 0:
                print("\n📊 Final Statistics:")
                display_statistics(history)
                print("\n📝 Final History:")
                for i, calc in enumerate(history, 1):
                    print(f"  {i}. {calc}")
            print("\nThank you for using Professional Calculator!\n")
            break
        
        # HELP COMMAND
        elif command == 'help':
            print("\n" + "="*60)
            print("HELP MENU")
            print("="*60)
            print("\n📱 COMMANDS:")
            print("  calc     - Start new calculation")
            print("  history  - View calculation history")
            print("  stats    - View session statistics")
            print("  clear    - Clear history")
            print("  help     - Show this menu")
            print("  quit     - Exit calculator")
            print("\n💡 TIP: You can also start by typing a number directly!")
            print("="*60 + "\n")
            continue
        
        # HISTORY COMMAND
        elif command == 'history':
            if len(history) == 0:
                print("\n📝 No calculations yet!\n")
            else:
                print("\n" + "="*60)
                print("CALCULATION HISTORY")
                print("="*60)
                for i, calc in enumerate(history, 1):
                    print(f"  {i}. {calc}")
                print("="*60 + "\n")
            continue
        
        # STATS COMMAND
        elif command == 'stats':
            display_statistics(history)
            continue
        
        # CLEAR COMMAND
        elif command == 'clear':
            if len(history) > 0:
                confirm = input(f"⚠️  Clear {len(history)} calculations? (yes/no): ").lower()
                if confirm == 'yes':
                    history.clear()
                    print("\n✓ History cleared!\n")
                else:
                    print("\n✓ Clear cancelled.\n")
            else:
                print("\n📝 History is already empty!\n")
            continue
        
        # CALCULATE (calc command or direct number entry)
        elif command == 'calc' or command.replace('.', '').replace('-', '').replace('+', '').isdigit():
            # If user typed a number directly, use it
            if command != 'calc':
                try:
                    num1 = float(command)
                except ValueError:
                    print("❌ Invalid command! Type 'help' for menu.\n")
                    continue
            else:
                num1 = get_number("Enter first number: ")
            
            # Get operation
            operation = input("Enter operation (+, -, *, /): ").strip()
            if operation not in ['+', '-', '*', '/']:
                print("❌ Invalid operation! Use +, -, *, or /\n")
                continue
            
            # Get second number
            num2 = get_number("Enter second number: ")
            
            # Perform calculation
            result, calc_string = perform_calculation(num1, operation, num2)
            
            # Handle division by zero
            if isinstance(result, str):
                print(f"\n❌ {result}\n")
                continue
            
            # Add to history
            history.append(calc_string)
            
            # Display result
            print("\n" + "="*60)
            print(f"✓ {calc_string}")
            print("="*60)
            print(f"📝 Saved to history (#{len(history)})\n")
        
        else:
            print("❌ Unknown command! Type 'help' for menu.\n")

def calculate_statistics(history):
    """
    Calculate statistics from history
    Returns dict with stats or none if no data
    """
    if len(history) == 0:
        return None
    
    # Extract just the results from history strings
    # Example: "10.0 +5.0 = 15.0" -> 15.0
    results = []
    for calc in history:
        try:
            # Split by '=' and get the part after it
            result_str = calc.split('=')[-1].strip()
            result = float(result_str)
            results.append(result)
        except:
            continue

    if len(results) == 0:
        return None
    
    return {
        "total_calculations": len(history),
        "average_result": sum(results) / len(results),
        "highest_result": max(results),
        "lowest_result": min(results),
        "sum_of_results": sum(results)
    }

def display_statistics(history):
    """ Display session statistics"""
    stats = calculate_statistics(history)
    
    if stats is None:
        print("\n No calculations to analyze yet!\n")
        return
    
    print("\n" + "="*60)
    print("SESSION STATISTICS")
    print("="*60)
    print(f" Total Calculations: {stats['total_calculations']}")
    print(f" Average Result: {stats['average_result']}")
    print(f" Highest Result: {stats['highest_result']}")
    print(f" Lowest Result: {stats['lowest_result']}")
    print(f" Sum of Results: {stats['sum_of_results']}")
    print("="*60 + "\n")


# Test the continuous version
if __name__ == "__main__":
    professional_calculator()  # Changed from calculator_with_history()