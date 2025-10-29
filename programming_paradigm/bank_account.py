# Python script to define a BankAccount class with deposit, withdraw, and display_balance methods.

# Define the BankAccount class
class BankAccount:
    def __init__(self, account_balance=0):
        self.balance = account_balance

    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return self.balance