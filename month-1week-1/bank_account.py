class BankAccount:
    """A simple bank account class"""

    def __init__(self, owner, balance=0):
        """Initialize a new bank account
        
        args:
            owner (str): Account owner's name
            balance (float): starting balance (default 0)
        """
        self.owner = owner
        self.balance = balance
        self.transactions = []  # Track all transactions

        # Record account creation
        self.transactions.append(f'Account created with balance: ${balance:.2f}')
        print(f'✅ Account created for {owner}')
        print(f'💰 Starting balance: ${balance:.2f}')

    def get_balance(self):
        """Return current balance"""
        return self.balance
    
    def display_balance(self):
        """Display formatted balance"""
        print(f'Current balance for {self.owner}: ${self.balance:.2f}')
    
    def deposit(self, amount):
        """Deposit money into account
        
        Args:
            amount (float): Amount to deposit
        """
        if amount <= 0:
            print('❌ Deposit amount must be positive!')
            return False

        self.balance += amount
        self.transactions.append(f'Deposit: +${amount:.2f}')
        print(f'✅ Deposited: ${amount:.2f}')
        print(f'   New balance: ${self.balance:.2f}')
        return True
    
    def withdraw(self, amount):
        """Withdraw money from account
        
        Args:
            amount (float): Amount to withdraw
        """
        if amount <= 0:
            print('❌ Withdrawal amount must be positive!')
            return False
        
        if amount > self.balance:
            print('❌ Insufficient funds for this withdrawal!')
            print(f'   Balance: ${self.balance:.2f}')
            print(f'   Requested: ${amount:.2f}')
            return False
        
        self.balance -= amount
        self.transactions.append(f'Withdrawal: -${amount:.2f}')
        print(f'✅ Withdrew: ${amount:.2f}')
        print(f'   New balance: ${self.balance:.2f}')
        return True
    
    def show_transactions(self):
        """Display transaction history"""
        print(f'\n📜 Transaction History for {self.owner}')
        print('=' * 50)

        if not self.transactions:
            print('No transactions yet.')
            return
        
        for i, transaction in enumerate(self.transactions, 1):
            print(f'{i}. {transaction}')

        print('=' * 50)
        print(f'Current Balance: ${self.balance:.2f}')

    def transfer(self, other_account, amount):
        """Transfer money to another account

        Args:
            other_account (BankAccount): Account to transfer to 
            amount (float): Amount to transfer
        """
        print(f'\n💸 Transfer: {self.owner} → {other_account.owner}')

        if amount <= 0:
            print('❌ Transfer amount must be positive!')
            return False
        
        if amount > self.balance:
            print('❌ Insufficient funds for this transfer!')
            print(f'   Balance: ${self.balance:.2f}')
            print(f'   Requested: ${amount:.2f}')
            return False
        
        #Withdraw from this account
        self.balance -= amount
        self.transactions.append(f'Transfer from {self.owner}: -${amount:.2f}')

        # Deposit to other account
        other_account.balance += amount
        other_account.transactions.append(f'Transfer to {other_account.owner}: -${amount:.2f}')

        print(f'✅ Transferred: ${amount:.2f} to {other_account.owner}')
        print(f'   {self.owner}\'s balance: ${self.balance:.2f}')
        print(f'   {other_account.owner}\'s balance: ${other_account.balance:.2f}')
        return True

    # TEST IT!
if __name__ == "__main__":
    print("="*60)
    print("🏦 COMPLETE BANK ACCOUNT SYSTEM WITH TRANSFERS")
    print("="*60)
    
    # Create accounts
    print("\n--- Creating Accounts ---")
    john = BankAccount("John Doe", 1000)
    alice = BankAccount("Alice Smith", 500)
    bob = BankAccount("Bob Johnson", 0)
    
    # Regular transactions
    print("\n" + "="*60)
    print("--- Regular Transactions ---")
    john.deposit(500)
    alice.withdraw(100)
    bob.deposit(250)
    
    # THE MAGIC: TRANSFERS!
    print("\n" + "="*60)
    print("--- Testing Transfers ---")
    john.transfer(alice, 300)  # John sends Alice $300
    alice.transfer(bob, 150)   # Alice sends Bob $150
    bob.transfer(john, 50)     # Bob sends John $50
    
    # Try insufficient funds transfer
    bob.transfer(john, 1000)   # Should fail
    
    # Final balances
    print("\n" + "="*60)
    print("--- Final Balances ---")
    john.display_balance()
    alice.display_balance()
    bob.display_balance()
    
    # Complete histories
    print("\n" + "="*60)
    print("📊 COMPLETE TRANSACTION HISTORIES")
    print("="*60)
    john.show_transactions()
    alice.show_transactions()
    bob.show_transactions()