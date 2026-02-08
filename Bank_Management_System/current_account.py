from account import Account
class CurrentAccount(Account):
    def __init__(self, name, account_number, balance,overdraft_limit):
        super().__init__(name, account_number, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            return True
        else:
            return False
    