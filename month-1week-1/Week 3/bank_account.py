"""
Enhanced Bank Account with decorators
"""

from decorators import log_transaction, timer, validate_amount
from datetime import datetime

class BankAccount:
    """
    Bank account with decorator-enhanced operations.
    
    Features:
    - Property-based balance access
    - Automatic transaction logging
    - Performance timing
    - Amount validation
    - Transaction history
    """

    # Class variable to track total accounts
    total_accounts = 0

    def __init__(self, owner, initial_balance=0):
        """Initialize account with owner and optional starting balance"""
        self.owner = owner 
        self._balance = initial_balance # Private variable
        self.transaction_history = [] # List to store transaction records
        self.created_at = datetime.now() # Timestamp of account creation

        # increment total accounts
        BankAccount.total_accounts += 1
        
        # Log account creation
        self._add_to_history('Account created', initial_balance)

        # ========================================
    # PROPERTY DECORATORS
    # ========================================
    
    @property
    def balance(self):
        """Get current balance."""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        """
        Set balance with validation.
        Balance cannot be negative.
        """
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = amount
    
    # ========================================
    # TRANSACTION METHODS WITH DECORATORS
    # ========================================
    
    @log_transaction
    @timer
    @validate_amount
    def deposit(self, amount):
        """Deposit money into account."""
        self._balance += amount
        self._add_to_history("Deposit", amount)
        return f"Deposited ${amount:.2f}"
    
    @log_transaction
    @timer
    @validate_amount
    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount > self._balance:
            raise ValueError(f"Insufficient funds! Balance: ${self._balance:.2f}")
        
        self._balance -= amount
        self._add_to_history("Withdrawal", amount)
        return f"Withdrew ${amount:.2f}"
    
    @log_transaction
    @timer
    def transfer(self, amount, recipient):
        """Transfer money to another account."""
        # Validate amount first
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Transfer amount must be positive")
        
        if amount > self._balance:
            raise ValueError(f"Insufficient funds! Balance: ${self._balance:.2f}")
        
        # Perform transfer
        self._balance -= amount
        recipient._balance += amount
        
        # Record in both histories
        self._add_to_history(f"Transfer to {recipient.owner}", amount)
        recipient._add_to_history(f"Transfer from {self.owner}", amount)
        
        return f"Transferred ${amount:.2f} to {recipient.owner}"
    
    # ========================================
    # CLASS METHODS (Factory patterns)
    # ========================================
    
    @classmethod
    def create_savings_account(cls, owner):
        """Factory method: Create account with $1000 starting balance."""
        return cls(owner, initial_balance=1000)
    
    @classmethod
    def create_checking_account(cls, owner):
        """Factory method: Create account with $500 starting balance."""
        return cls(owner, initial_balance=500)
    
    @classmethod
    def get_total_accounts(cls):
        """Get total number of accounts created."""
        return cls.total_accounts
    
    # ========================================
    # STATIC METHODS (Utilities)
    # ========================================
    
    @staticmethod
    def format_currency(amount):
        """Format amount as currency string."""
        return f"${amount:,.2f}"
    
    @staticmethod
    def calculate_interest(principal, rate, years):
        """Calculate simple interest."""
        return principal * (1 + rate * years)
    
    # ========================================
    # HELPER METHODS
    # ========================================
    
    def _add_to_history(self, transaction_type, amount):
        """Add transaction to history."""
        entry = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': transaction_type,
            'amount': amount,
            'balance_after': self._balance
        }
        self.transaction_history.append(entry)
    
    def get_transaction_history(self):
        """Return formatted transaction history."""
        if not self.transaction_history:
            return "No transactions yet."
        
        history = f"\n{'='*60}\n"
        history += f"Transaction History for {self.owner}\n"
        history += f"{'='*60}\n"
        
        for entry in self.transaction_history:
            history += f"{entry['timestamp']} - {entry['type']}: "
            history += f"${entry['amount']:.2f} (Balance: ${entry['balance_after']:.2f})\n"
        
        return history
    
    def __str__(self):
        """String representation of account."""
        return f"BankAccount(owner='{self.owner}', balance=${self._balance:.2f})"
    
    def __repr__(self):
        """Developer representation of account."""
        return f"BankAccount('{self.owner}', {self._balance})"