#Q41. Function to calculate square
def square(x):
    return x ** 2
#Q42. Function to calculate cube using square function
def cube(n):
    return square(n) * n
print(cube(3))
print(cube(2))
#Q43. Function banao jo factorial calculate kare using multiplication function
def multiply(a,b):
    return a * b
def factorial(x):
    result = 1
    for i in range(1,x+1):
        result = multiply(result,i)
    return result
print(factorial(5))
#Q44. Function to check even/odd using helper function
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
def num(x):
    return check_even_odd(x)
print(num(50))
#Q45. Function to calculate area of rectangle using multiply function
def calculate_area_rectangle(l,w):
    return l * w
def rectangle(l,w):
    return calculate_area_rectangle(l,w)
print(rectangle(5,8))