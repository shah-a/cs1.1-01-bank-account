# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Nov. 09, 2020
# CS 1.1 Assignment 1: Bank Account

from random import sample

# population = range(10_000_000, 100_000_000)
# output = sample(population, 6)
# print(output)

class Account:
    routing_number = 123_456_789
    def __init__(self, full_name, account_number, balance=0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def get_balance(self):
        pass

    def haram(self):
        pass

    def print_receipt(self):
        censored_acc_number = censor(self.account_number)
        print(
            f"{self.full_name}\n"
            f"Account No.: {censored_acc_number}\n"
            f"testing\n"
            f"testing"
        )

def censor(numbers):
    numbers = str(numbers)
    numbers = "****" + numbers[-4:]
    return numbers


my_acc = Account("Ali Shah", 44444888, 5)
my_acc.print_receipt()
