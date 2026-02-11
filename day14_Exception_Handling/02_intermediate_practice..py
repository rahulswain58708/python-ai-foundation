# Q6️⃣ Multiple Except Blocks
# Write a program that:
# Takes two numbers
# Handles ZeroDivisionError and ValueError separately

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Cannot Divide By Zero!")
except ValueError:
    print("Please Enter Only Number!")
# Q7️⃣ Using Else Block
# Write a program that:
# Divides two numbers
# Prints "Success" only if no error occurs
try:
    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter another number: "))
    print(first_number/second_number)
except ZeroDivisionError:
    print("Canot Divide By Zero!")
except ValueError:
    print("Please Enter Only Number!")
else:
    print("Success")
# Q8️⃣ Finally Block
# Write a program that:
# Opens a file
# Uses finally to print "Program Ended"
try:
    with open("data.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("Program Ended")
# Q9️⃣ Raise ValueError
# Take age as input:
# If age < 18 → raise ValueError
# Handle it using try–except
try:
    age = int(input("Enter youre age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above")
except ValueError as e:
    print("Error:",e)
else:
    print(f"Age is {age}")
# Q🔟 Password Validation
# Write a program that:
# Takes password input
# Raises error if length < 6
try:
    password = input("Enter Your Password:- ")
    if len(password) < 6:
        raise ValueError("Enter strong password length more than 6!")
except ValueError as e:
    print("Error:",e)
else:
    print(f"Password = {password}")