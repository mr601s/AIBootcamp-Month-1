"""
Demo of Enhanced Banking System v2
Shows all decorator features in action
"""

from bank_account import BankAccount


def main():
    print("=" * 60)
    print("ENHANCED BANKING SYSTEM v2.0")
    print("Powered by Python Decorators!")
    print("=" * 60)
    
    # Create accounts using different methods
    print("\n--- Creating Accounts ---")
    
    # Regular constructor
    alice = BankAccount("Alice", 1000)
    print(f"Created: {alice}")
    
    # Using class method factory
    bob = BankAccount.create_savings_account("Bob")
    print(f"Created: {bob}")
    
    charlie = BankAccount.create_checking_account("Charlie")
    print(f"Created: {charlie}")
    
    # Show total accounts (class method)
    print(f"\nTotal accounts: {BankAccount.get_total_accounts()}")
    
    # Test deposits (with decorators!)
    print("\n--- Testing Deposits ---")
    alice.deposit(500)
    bob.deposit(250)
    
    # Test withdrawals
    print("\n--- Testing Withdrawals ---")
    alice.withdraw(300)
    
    # Test transfers
    print("\n--- Testing Transfers ---")
    alice.transfer(200, bob)
    
    # Test property access
    print("\n--- Testing Property Access ---")
    print(f"Alice's balance: {BankAccount.format_currency(alice.balance)}")
    print(f"Bob's balance: {BankAccount.format_currency(bob.balance)}")
    
    # Test static methods
    print("\n--- Testing Static Methods ---")
    interest = BankAccount.calculate_interest(1000, 0.05, 5)
    print(f"$1000 at 5% for 5 years: {BankAccount.format_currency(interest)}")
    
    # Show transaction history
    print("\n--- Transaction History ---")
    print(alice.get_transaction_history())
    print(bob.get_transaction_history())
    
    # Test validation (this should error)
    print("\n--- Testing Validation ---")
    try:
        alice.deposit(-100)
    except ValueError as e:
        print(f"✅ Validation caught error: {e}")
    
    try:
        alice.withdraw(10000)
    except ValueError as e:
        print(f"✅ Insufficient funds caught: {e}")
    
    print("\n" + "=" * 60)
    print("Demo Complete! Check transactions.log for full log.")
    print("=" * 60)


if __name__ == "__main__":
    main()