class Account:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
        return True
    def get_balance(self):
        return self._balance
    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False
    def display_details(self):
        return f"Name:{self.name}\nAccount_number:{self.account_number}\nBalance = {self.get_balance()}"
