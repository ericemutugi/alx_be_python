# Python script to define a BankAccount class with deposit, withdraw, and display_balance methods.

# Define the BankAccount class
class BankAccount:
    def _init_ (self, account_balance=0):
        self.account_balance = account_balance

# Implement deposit, withdraw, and display_balance methods
    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        return self.account_balance