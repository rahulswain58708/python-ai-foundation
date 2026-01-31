#Q1: Create a function that prints your name
def print_name(name):
    print(name)
print_name("Rahul")
#Q2: Create a function that adds two numbers and returns the result.
def add_nums(a,b):
    return a + b
print(add_nums(5,15))
print(add_nums(-5,25))
#Q3: Create a function that subtracts two numbers and returns the result.
def sub_nums(a,b):
    return a - b
print(sub_nums(15,5))
print(sub_nums(28,8))
#Q4: Create a function that multiplies two numbers and returns the result.
def multiplies_nums(a,b):
    return a * b
print(multiplies_nums(5,10))
print(multiplies_nums(5,25))
#Q5: Create a function that divides two numbers and returns the result.
def div_nums(a,b):
    if b == 0:
        return "cannot divide by zero."
    else:
        return a / b
print(div_nums(5,2))
print(div_nums(0,2))
#Q6: Create a function that checks Even or Odd
# Return "Even" or "Odd".
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(5))
print(check_even_odd(10))
#Q7: Create a function that finds square of a number and returns it.
def square(num):
    return num**2
print(square(5))
print(square(9))
#Q8: Create a function that finds cube of a number and returns it.
def find_cube(num):
    return num**3
print(find_cube(5))
print(find_cube(25))
#Q9: Create a function that finds area of a rectangle.
def find_area(l, w):
    return l * w
print(find_area(5,2))
#Q10: Create a function that converts Celsius to Fahrenheit
# F = (C * 9/5) + 32
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit(35))