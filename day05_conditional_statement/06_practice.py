#Q6.Take two numbers as input and print the greater number.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
if num1 > num2:
    print(f"Greater number = {num1}")
elif num2 > num1:
    print(f"Greater number = {num2}")
else:
    print("Both numbers are equal")