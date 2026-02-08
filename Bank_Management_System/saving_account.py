from account import Account
class SavingAccount(Account):
    def __init__(self,name,account_number,balance,interest_rate):
        super().__init__(name,account_number,balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = (self.get_balance() * self.interest_rate) / 100
        return interest
