# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Nov. 09, 2020
# CS1.1 Assignment 1: Bank Account

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
        """Substracts amount from if self.balance is sufficient."""
        if amount > self.balance:
            print(f"Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")

    def get_balance(self):
        """Returns account balance."""
        print("Account Balance: $" + "{:.2f}".format(self.balance))
        return self.balance

    def print_receipt(self):
        """Displays account status."""
        censored_num = censor(self.account_number)
        print(
            f"{self.full_name}\n"
            f"Account No.: {censored_num}\n"
            f"Routing No.: {BankAccount.routing_number}"
        )
        print("Balance: $" + "{:.2f}".format(self.balance))

# acc1 = BankAccount("First Example")
# acc2 = BankAccount("Second Example")
# acc3 = BankAccount("Third Example")

# print("-----------")
# print("Example #1:")
# print("-----------")

# acc1.deposit(1000)
# acc1.get_balance()
# acc1.withdraw(25)
# acc1.get_balance()

# print("-----------")
# print("Example #2:")
# print("-----------")

# acc2.deposit(200)
# acc2.withdraw(220)
# acc2.print_receipt()

# print("-----------")
# print("Example #3:")
# print("-----------")

# acc3.deposit(1000)
# acc3.print_receipt()
