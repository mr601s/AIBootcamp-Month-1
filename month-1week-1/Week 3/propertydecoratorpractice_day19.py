class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance # Note the underscore (convention for 'private')

        @property
        def balance(self):
            """Getter - access like an attribute"""
            return self._balance
        
        @balance.setter
        def balance(self, amount):
            """Setter - validate before setting."""
            if amount < 0:
                raise ValueError('Balance cannot be negative!')
            self._balance = amount

# Usage
account = BankAccount('Alice', 1000)

# Access like an attribute (no parentheses!)
print(account.balance) #1000

# Set like an attribute
account.balance = 1500 # Uses setter
print(account.balance) # 1500

# Validation works!
try:
    account.balance = -100 # will raise error 
except ValueError as e:
    print(f'Error: {e}')
