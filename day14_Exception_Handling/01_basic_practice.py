# Q1️⃣ Divide Two Numbers Safely
# Write a program that:
# Takes two numbers from user
# Handles ZeroDivisionError

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Cannot Divide by zero!")

# Q2️⃣ Handle Invalid Input
# Take an integer from user.
# If user enters text → handle ValueError

try:
    nums = int(input("Enter a number: "))
    print(nums)
except ValueError:
    print("Please Enter Only Number")

# Q3️⃣ Simple Try–Except
# Write a program that:
# Tries to print an element at index 5 from a list of 3 items
# Handles IndexError

try:
    fruits = ["Apple","Banana","Orange"]
    print(fruits[5])
except IndexError:
    print("Please Acess a Valid Index ")

# Q4️⃣ File Open Error
# Open a file named data.txt
# If file not found → handle FileNotFoundError
try:
    with open("data.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File Not Found")
else:
    print("File Read Sucessfully!")

# Q5️⃣ Catch All Errors
# Write a program that:
# Takes two inputs
# Performs division
# Uses Exception as e to catch any error
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x/y)
except Exception as e:
    print("Error:",e)