# Take name, age, and field as input and print a formatted output using f-string.
# Example output:
# My name is Rahul, I am 18 years old and I am learning AI
name = input("Enter your name:")
age = int(input("Enter your age:"))
field = input("Enter filed:")
print(f"My name is {name}, I am {age} years old and I am learning {field}")
# Take marks (out of 100) as input and print:
# Marks obtained: <marks>
marks = float(input("Enter marks out of 100:"))
print(f"Marks obtained: {marks}")