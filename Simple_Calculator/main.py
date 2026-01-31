#Simple Calculator
def show_menu():
    print("--------------Welcome to simple calculator--------------")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("6.Power")
    print("7.Exit")
def add_numbers(a,b):
    return f"Result = {a + b}"
def subtract_numbers(a,b):
    return f"Result = {a - b}"
def multiply_numbers(a,b):
    return f"Result = {a * b}"
def divide_numbers(a,b):
    if b == 0:
        return "Can not divide by zero❌"
    else:
        return f"Result = {a / b}"
def modulus_numbers(a,b):
    return f"Result = {a % b}"
def power(a,b):
    return f"Result = {a ** b}"
def get_two_input():
            n1 = int(input("Enter First Number:- "))
            n2 = int(input("Enter Second Number:- "))
            return n1,n2
def main():
    while True:
        show_menu()
        option = input("Enter one option (1-7):")
        
        if option == "1":
            n1,n2 = get_two_input()
            print(add_numbers(n1,n2))
        elif option == "2":
            n1,n2 = get_two_input()
            print(subtract_numbers(n1,n2))
        elif option == "3":
            n1,n2 = get_two_input()
            print(multiply_numbers(n1,n2))
        elif option == "4":
            n1,n2 = get_two_input()
            print(divide_numbers(n1,n2))
        elif option == "5":
            n1,n2 = get_two_input()
            print(modulus_numbers(n1,n2))
        elif option == "6":
            n1,n2 = get_two_input()
            print(power(n1,n2))
        elif option == "7":
            print("Thanks for calculating good bye🤗")
            break
        else:
            print("Invalid input ❌")
main()