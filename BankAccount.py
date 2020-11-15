# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Nov. 09, 2020
# CS 1.1 Assignment 1: Bank Account

from random import randint

def censor(numbers):
    """A helper function to censor numbers by adding asterisks."""
    numbers = str(numbers)
    numbers = "****" + numbers[-4:]
    return numbers

class BankAccount:
    """Class for bank account objects."""

    routing_number = 123_456_789

    def __init__(self, full_name):
        """Constructor for account instances. Default balance = 0."""
        self.full_name = full_name
        self.account_number = randint(10_000_000, 99_999_999)
        self.balance = 0

    def deposit(self, amount):
        """Adds amount to self.balance."""
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount):
        """Substracts amount from self.balance."""
        if amount > self.balance:
            self.balance -= (amount + 10)
            print(f"Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")

    def get_balance(self):
        """Returns account balance."""
        print("Account Balance: $" + "{:.2f}".format(self.balance))
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_receipt(self):
        """Displays account status."""
        censored_num = censor(self.account_number)
        print(
            f"{self.full_name}\n"
            f"Account No.: {censored_num}\n"
            f"Routing No.: {BankAccount.routing_number}"
        )
        print("Balance: $" + "{:.2f}".format(self.balance))
