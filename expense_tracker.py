import json
from datetime import datetime

# Global data
data = {
    "transactions": [],
    "budgets": {
        "Food": 500.00,
        "Transport": 200.00,
        "Entertainment": 150.00,
        "Bills": 800.00,
        "Shopping": 300.00,
        "Other": 200.00
    },
    "next_id": 1
}

# Predefined categories
EXPENSE_CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"]
INCOME_CATEGORIES = ["Salary", "Freelance", "Investment", "Gift", "Other"]

def get_timestamp():
    """ Get current timestamp in ISO format"""
    return datetime.now().isoformat()

def get_date():
    """Get current date in YYYY-MM-DD format"""
    return datetime.now().date().isoformat()

def save_data():
    """Save all data to JSON file"""
    try:
        with open("finance_data.json", 'w') as file:
            json.dump(data, file, indent=4)
        print('Data saved!')
    except Exception as e:
        print(f'Error saving data: {e}')

def load_data():
    """Load data from JSON file"""
    global data
    try:
        with open('finance_data.json', 'r') as file:
            data = json.load(file)
        print(f" Loaded {len(data['transactions'])} transactions")
    except FileNotFoundError:
        print('No saved data found. Starting fresh!')
        data = {
            "transactions": [],
            "budgets": {
                "Food": 500.00,
                "Transport": 200.00,
                "Entertainment": 150.00,
                "Bills": 800.00,
                "Shopping": 300.00,
                "Other": 200.00
            },
            "next_id": 1
        }
    except Exception as e:
        print(f'Error loading data: {e}')

def add_transactions():
    """Add a new transaction or expense transaction"""
    print('\n' + '='*50)
    print('Add Transaction')
    print('='*50)

    # Transaction type
    print('\n' + '='*50)
    print('Add Transaction')
    print('='*50)

    # Transaction type
    print('\n1. Income')
    print('2. Expense')
    trans_type = input('\nTransaction type (1-2): ')

    if trans_type == '1':
        transaction_type = 'Income'
        categories = INCOME_CATEGORIES
    elif trans_type == '2':
        transaction_type = 'expense'
        categories = EXPENSE_CATEGORIES
    else:
        print('Invalid type')
        return
    
    # Show categories
    print(f'\nCategories:')
    for i, cat in enumerate(categories, 1):
        print(f'{i}. {cat}')
    
    cat_choice = input(f'\nChoose category (1-{len(categories)}): ')
    try:
        cat_index = int(cat_choice) - 1
        if 0 <= cat_index < len(categories):
            category = categories[cat_index]
        else:
            print('Invalid category')
            return
    except ValueError:
        print('Please enter a number')
        return
    
    # Amount 
    try:
        amount = float(input('\nAmount: $'))
        if amount <= 0:
            print('Amount must be positive')
            return
    except ValueError:
        print('Invalid amount')
        return
    
    # Description
    transaction = {
        "id": data["next_id"],
        "type": transaction_type,
        "category": category,
        "amount": amount,
        "description": input('Description (optional): '),
        "date": get_date(),
        "timestamp": get_timestamp()
    }

    data['transactions'].append(transaction)
    data['next_id'] += 1
    save_data()

    symbol = '+' if transaction_type.lower() == 'income' else '-'
    print(f'\nTransaction added: {symbol}${amount:.2f} for {category}')

def view_all_transactions():
    """Display all transactions"""
    transactions = data['transactions']


    if not transactions:
        print('\n No transactions yet!')
        return
    
    print('\n' + '='*70)
    print(f'All Transactions ({len(transactions)} total)')
    print('='*70)

    # Sort by date (newest first)
    sorted_trans = sorted(transactions, key=lambda x: x['timestamp'], reverse=True)

    for trans in sorted_trans:
        trans_type = trans['type']
        symbol = '+' if trans_type == 'income' else '-'
        color = '🟢' if trans_type == 'income' else '🔴'

        print(f"\n{color} ID: {trans['id']} {trans['date']}")
        print(f" {symbol}${trans['amount']:.2f} - {trans['category']}")
        print(f" {trans['description']}")

def view_by_category():
    """View transaction grouped by category"""
    transactions = data['transactions']

    if not transactions:
        print('\n No transactions yet!')
        return
    
    print('\n' + '='*70)
    print('Transactions by Category')
    print('='*70)

    # Group transactions by category
    category_groups = {}
    for trans in transactions:
        category = trans['category']
        if category not in category_groups:
            category_groups[category] = []
        category_groups[category].append(trans)

    # Display each category with its transactions
    for category, trans in category_groups.items():
        print(f'\nCategory: {category}')
        for t in trans:
            symbol = '+' if t['type'] == 'income' else '-'
            print(f" {symbol}${t['amount']:.2f} - {t['description']}")

def calculate_totals():
    """Calculate and display financial summary"""
    transactions = data['transactions']

    if not transactions:
        print('\n No transactions to calculate')
        return
    
    # Calculate totals
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = total_income - total_expense

    print('\n' + '='*50)
    print('Financial Summary')
    print('='*50)
    print(f'Total Income: +${total_income:.2f}')
    print(f'Total Expense: -${total_expense:.2f}')
    print(f'Balance: ${balance:.2f}')

    if balance >= 0:
        print('Status: 🟢 Positive Balance')
    else:
        print('Status: 🔴 Negative Balance')

    # Expense breakdown
    if total_expense > 0:
        print(f'\n Expense Breakdown:')

        # Group expenses by category
        expense_by_cat = {}
        for trans in transactions:
            if trans['type'] == 'expense':
                cat = trans['category']
                expense_by_cat[cat] = expense_by_cat.get(cat, 0) + trans['amount']

        # Sort by amount (highest first)
        for cat, amount in sorted(expense_by_cat.items(), key=lambda x: x[1], reverse=True):
            percent = (amount / total_expense) * 100
            budget = data['budgets'].get(cat, 0)
            budget_status = f' / Budget: ${budget:.2f}' if budget > 0 else ''
            print(f' - {cat}: ${amount:.2f} ({percent:.1f}%) {budget_status}')

def set_budgets():
    """Set monthly budgets for expense categories"""
    print('\n' + '='*50)
    print('Set Monthly Budgets')
    print('='*50)

    print('\nCurrent budgets:')
    for category, amount in data['budgets'].items():
        print(f' - {category}: ${amount:.2f}')

    print('\nUpdate budgets (press enter to keep current):')

    for category in EXPENSE_CATEGORIES:
        current = data['budgets'].get(category, 0)
        new_budget = input(f'{category} (current: ${current:.2f}): $')

        if new_budget.strip():
            try:
                amount = float(new_budget)
                if amount < 0:
                    print('Budget must be non-negative')
                else:
                    data['budgets'][category] = amount
            except ValueError:
                print('Invalid amount, skipping...')

    save_data()
    print('\nBudgets updated!')

def view_budgets_status():
    """Compare budget vs actual spending"""
    transactions = data['transactions']
    budgets = data['budgets']

    print('\n' + '='*70)
    print('Budget vs Actual Spending')
    print('='*70)

    # Calculate spending by category
    spending = {}
    for trans in transactions:
        if trans['type'] == 'expense':
            cat = trans['category']
            spending[cat] = spending.get(cat, 0) + trans['amount']

    # Compare each category
    total_budget = 0
    total_spent = 0

    for category in EXPENSE_CATEGORIES:
        budget = budgets.get(category, 0)
        spent = spending.get(category, 0)
        remaining = budget - spent

        total_budget += budget
        total_spent += spent

        print(f'\n {category}')
        print(f'  Budget: ${budget:.2f}')
        print(f'  Spent: ${spent:.2f}')
        if remaining >= 0:
            percentage = (spent / budget * 100) if budget > 0 else 0
            if percentage > 90:
                print(' Warning: Nearly over budget!')
            print(f'  Remaining: ${remaining:.2f} ({percentage:.1f}% used)')

    # Total summary
    print('\n' + '='*70)
    print(f'Total Budget: ${total_budget:.2f}')
    print(f'Total Spent: ${total_spent:.2f}')

    if total_spent <= total_budget:
        print(f' Within budget by ${total_budget - total_spent:.2f}')
    else:
        print(f' Over budget by ${total_spent - total_budget:.2f}')

def search_transactions():
    """Search transactions by keyword"""
    transactions = data['transactions']

    if not transactions:
        print('\n No transactions yet!')
        return
    
    keyword = input('\nEnter keyword to search: ').lower()
    if not keyword.strip():
        print('Keyword cannot be empty')
        return
    
    matched = [t for t in transactions if keyword in t['description'].lower()]

    if not matched:
        print(f'\n No transactions found matching "{keyword}"')
        return
    
    print(f'\n{len(matched)} transactions found matching "{keyword}":')

def delete_transaction():
    """Delete a transaction by ID"""
    transactions = data['transactions']

    if not transactions:
        print('\n No transactions to delete!')
        return
    
    # Show recent transactions
    print('\nRecent transactions:')
    for trans in transactions[-5:]:
        print(f" - {trans['description']}: ${trans['amount']:.2f}")

    # Select transaction to delete
    trans_id = input('\nEnter transaction ID to delete: ')
    for i, trans in enumerate(transactions):
        if str(trans['id']) == trans_id:
            del transactions[i]
            print(f'\nTransaction {trans_id} deleted.')
            save_data()
            return

    print(f'\nTransaction {trans_id} not found.')

def main():
    """Main program loop"""
    load_data()
    while True:
        print('\n' + '='*50)
        print('Personal Finance Tracker')
        print('='*50)
        print('1. Add Transaction')
        print('2. View All Transactions')
        print('3. View Transactions by Category')
        print('4. Financial Summary')
        print('5. Set Monthly Budgets')
        print('6. View Budget Status')
        print('7. Search Transactions')
        print('8. Delete Transaction')
        print('9. Exit')

        choice = input('\nChoose an option (1-9): ')

        if choice == '1':
            add_transactions()
        elif choice == '2':
            view_all_transactions()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            calculate_totals()
        elif choice == '5':
            set_budgets()
        elif choice == '6':
            view_budgets_status()
        elif choice == '7':
            search_transactions()
        elif choice == '8':
            delete_transaction()
        elif choice == '9':
            print('Exiting... Goodbye!')
            break
        else:
            print('Invalid choice, please try again.')
            

if __name__ == "__main__":
    main()
