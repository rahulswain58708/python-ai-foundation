# Q2️⃣0️⃣ Mini Project – Safe Calculator (Production Level)
# Requirements:
# Menu: + - * / % **
# Handle:
# Wrong input
# Division by zero
# Invalid operation (custom exception)
# Use:
# try
# multiple except
# else
# finally
# 📌 Create: InvalidOperationError
def add_num(n1,n2):
    return f"sum = {n1 + n2}"
def diff_num(n1,n2):
    return f"difference = {n1 - n2}"
def multiply_num(n1,n2):
    return f"multiply = {n1 * n2}"
def div_num(n1,n2):
    return f"division = {n1 / n2}"
def modulus_num(n1,n2):
    return f"modulus = {n1 % n2}"
def expo_num(n1,n2):
    return f"exponential = {n1 ** n2}"
def main():
    class InvalidOperationError(Exception):
        pass
    print("--------Welcome To Simple Calculator--------")
    try:
        n1 = int(input("Enter First Number:- "))
        n2 = int(input("Enter Second Number:- "))
        print("Operators:- + - * / % **")
        operator = input("Enter Operator:- ")
        if operator == "+":
            print(add_num(n1,n2))
        elif operator == "-":
            print(diff_num(n1,n2))
        elif operator == "*":
            print(multiply_num(n1,n2))
        elif operator == "/":
            if n2 == 0:
                raise ZeroDivisionError("Denominator cannot be zero. Please enter a non-zero number.")
            print(div_num(n1,n2))
        elif operator == "%":
            print(modulus_num(n1,n2))
        elif operator == "**":
            print(expo_num(n1,n2))
        else:
            raise InvalidOperationError("Please Enter Valid Operator!")
    except InvalidOperationError as e:
        print("Error:",e)
    except ValueError:
        print("Please Enter Only Number!")
    except ZeroDivisionError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)
    else:
        print("Calculate Succesfully")
    finally:
        print("Program ended")
main()