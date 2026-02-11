# Q1️⃣6️⃣ File Reading System (Real-World Safe Code)
# Task:
# Write a program that:
# Opens a file data.txt
# Reads content
# Handles file not found
# Uses finally to close file or print message
# 📌 Hint: with open() + finally
try:
    with open("data.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("Please Open Valid File")
finally:
    print("Program ended")
# Q1️⃣7️⃣ Student Marks Validator (Custom Exception)
# Rules:
# Marks must be between 0 and 100
# If marks < 0 or > 100 → raise custom exception
# 📌 Create: InvalidMarksError


class InvalidMarksError(Exception):
    pass
try:
    marks = int(input("Enter Marks:- "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Please Enter Valid Marks between 0 to 100 !")
except InvalidMarksError as e:
    print("Error:",e)
except ValueError:
    print("Please Enter Only Number !")
except Exception as e:
    print("Error:",e)
else:
    print(f"Marks = {marks}")


# Q1️⃣8️⃣ API Input Simulation (AI Style Validation)
# Rules:
# Input must be integer
# Input must be greater than 0
# Use raise
# Use custom exception
# 📌 Create: InvalidAPIInputError
class InvalidAPIInputError(Exception):
    pass

try:
    num = int(input("Enter a number:- "))
    if num <= 0:
        raise InvalidAPIInputError("Please Enter Positive Number !")
except InvalidAPIInputError as e:
    print("Error:",e)
except ValueError:
    print("Please Enter Only Number")
except Exception as e:
    print("Error",e)
else:
    print(f"Number is {num}")
        
# Q1️⃣9️⃣ Multiple Custom Exceptions (Advanced Control)
# Rules:
# Take age input
# If age < 18 → LowAgeError
# If age > 60 → HighAgeError
# Els → print “Age accepted”

class LowAgeError(Exception):
    pass
class HighAgeError(Exception):
    pass
try:
    age = int(input("Enter your age:- "))
    if age < 18:
        raise LowAgeError("Please Enter Age Greater Than 18!")
    elif age > 60:
        raise HighAgeError("Please Enter Age Less Than 60!")
    else:
        print("Age accepted")
except LowAgeError as e:
    print("Error:",e)
except HighAgeError as e:
    print("Error:",e)
except ValueError:
    print("Please Enter Only Number!")
except Exception as e:
    print("Error:",e)

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