import os
import random
from datetime import datetime

class BankAccount:
    def __init__(self, name, account_type, balance=0):
        """Constructor to initialize the bank account with name, account type, and balance."""
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.account_id = random.randint(1000, 9999)  # Generate a random account ID
        self.transaction_file = f"{self.name}_{self.account_type}_{self.account_id}_transactions.txt"
        
        # Create a new transaction file for the user
        try:
            with open(self.transaction_file, 'w') as file:
                file.write(f"Account Created: {datetime.now()}\n")
                file.write(f"Account ID: {self.account_id}\n")
                file.write(f"Account Type: {self.account_type}\n")
                file.write(f"Initial Balance: {self.balance}\n")
                file.write("-" * 50 + "\n")
        except Exception as e:
            print(f"Error creating transaction file: {e}")
        
    def deposit(self, amount):
        """Deposit money into the account and record the transaction."""
        if amount > 0:
            self.balance += amount
            self._record_transaction(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")
        
    def withdraw(self, amount):
        """Withdraw money from the account if balance is sufficient and record the transaction."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self._record_transaction(f"Withdrew: ${amount}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")
    
    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance
    
    def get_user_id(self):
        """Return the account ID."""
        return self.account_id
    
    def get_user_name(self):
        """Return the user's name."""
        return self.name
    
    def get_account_type(self):
        """Return the account type."""
        return self.account_type
    
    def get_transaction_history(self):
        """Read the transaction history from the transaction file."""
        try:
            with open(self.transaction_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("Transaction file not found.")
            return ""
        except Exception as e:
            print(f"Error reading transaction file: {e}")
            return ""
    
    def _record_transaction(self, transaction_details):
        """Helper method to record a transaction in the transaction file."""
        try:
            with open(self.transaction_file, 'a') as file:
                file.write(f"{datetime.now()} - {transaction_details}\n")
        except Exception as e:
            print(f"Error recording transaction: {e}")


# Testing the BankAccount class

# Create a new bank account
account1 = BankAccount("Alice", "chequing", 500)

# Perform some operations
account1.deposit(200)
account1.withdraw(100)

# Display account details
print("Account Balance:", account1.get_balance())
print("Account ID:", account1.get_user_id())
print("Account Name:", account1.get_user_name())
print("Account Type:", account1.get_account_type())

# Print transaction history
print("Transaction History:")
print(account1.get_transaction_history())

# Create another account
account2 = BankAccount("Bob", "savings", 1000)

# Perform some operations
account2.deposit(500)
account2.withdraw(200)

# Display account details for the second account
print("\nAccount Balance:", account2.get_balance())
print("Account ID:", account2.get_user_id())
print("Account Name:", account2.get_user_name())
print("Account Type:", account2.get_account_type())

# Print second account transaction history
print("Transaction History for Bob:")
print(account2.get_transaction_history())
