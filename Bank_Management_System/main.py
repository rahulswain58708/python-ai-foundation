#Bank Management System
# Features:
# Create account
# Deposit / Withdraw
# Check balance
# Account type (Savings / Current)
from current_account import CurrentAccount
from saving_account import SavingAccount

accounts = {}
def createaccount():
    acc_type = input("Enter Account Type(Saving/Current): ").lower()
    acc_name = input("Enter name: ")
    acc_number = int(input("Enter account number: "))
    balance = float(input("Enter initial balance:"))
    if acc_number in accounts:
        print("Account number already exist!")
        return
    elif acc_type == "saving":
        interest_rate = float(input("Enter interest rate: "))
        account = SavingAccount(acc_name,acc_number,balance,interest_rate)
        print("Account Created Sucessfully")
    elif acc_type == "current":
        overdraft_limit = float(input("Enter overdraft limit: "))
        account= CurrentAccount(acc_name,acc_number,balance,overdraft_limit)
        print("Account Created Sucessfully")
    else:
        print("Invalid account type")
        return
    accounts[acc_number] = account
def withdraw_money():
    acc_no = int(input("Enter account number: "))
    amount = float(input("Enter amount to withdraw: "))

    account = accounts.get(acc_no)
    if account:
        if account.withdraw(amount):
            print("Withdrawal successful")
        else:
            print("Insufficient balance / overdraft limit exceeded")
    else:
        print("Account not found")
def deposite_money():
    acc_no = int(input("Enter account number: "))
    amount = float(input("Enter deposit amount: "))

    account = accounts.get(acc_no)
    if account:
        account.deposit(amount)
        print("Deposit Successful")
    else:
        print("Account not found")

def check_balance():
    acc_no = int(input("Enter account number: "))
    account = accounts.get(acc_no)

    if account:
        print("Current Balance:", account.get_balance())
    else:
        print("Account not found")
def show_details():
    acc_no = int(input("Enter account number: "))
    account = accounts.get(acc_no)

    if account:
        print(account.display_details())
    else:
        print("Account not found")
while True:
    print("\n---- BANK MENU ----")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    option = input("Enter one option:")
    if option == '1':
        createaccount()
    elif option == '2':
        deposite_money()
    elif option == '3':
        withdraw_money()
    elif option == '4':
        check_balance()
    elif option == '5':
        show_details()
    elif option == '6':
        print("Thank you for using Bank System")
        break
    else:
        print("Invalid choice, try again")