#Q21: Create a lambda function that takes a number and returns its square.
square = lambda n:n**2
print(square(5))
print(square(10))
print(square(2))
#Q22: Create a lambda function that returns "Even" if a number is even, else "Odd".
find_even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print(find_even_odd(5))
print(find_even_odd(8))
#Q23: Create a lambda function that takes two numbers and returns their sum.
total = lambda n1,n2: n1 + n2
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(total(a,b))
#Q24: Create a lambda function that returns the greater number between two numbers.
greater_number = lambda x,y: x if x > y else y
print(greater_number(5,4))
print(greater_number(15,25))
#Q25: Given a list of numbers, use lambda with filter() to return only even numbers.
nums = [1,2,3,4,5,6,7,8]
even_nums = lambda num: num % 2 == 0
result = filter(even_nums,nums)
print(list(result))