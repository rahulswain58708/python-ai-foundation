#Q11: Create a function that takes three numbers and returns the largest.
def find_largest(n1,n2,n3):
   if n1 >= n2 and n1 >= n3:
      return n1
   elif n2 >= n1 and n2 >= n3:
      return n2
   else:
      return n3
print(find_largest(1,2,3))
print(find_largest(2,2,2))
print(find_largest(3,2,1))
print(find_largest(1,4,2))
print(find_largest(2,2,3))
#Q12: Create a function that returns sum of all elements in a list
def sum_all(numbers):
   return sum(numbers)
l = [10,20,30,40,50]
print(sum_all(l))
#Q13: Create a function that returns average of numbers
def average(numbers):
   total = sum(numbers)
   avg = total / len(numbers)
   return avg
nums = [10,50,40]
print(average(nums))
#Q14: Create a function that checks whether a number is
# Positive, Negative or Zero
def check_number(n):
    if n > 0:
       return "Positive"
    elif n < 0:
       return "Negative"
    else:
       return "Zero"
print(check_number(5))
print(check_number(-10))
print(check_number(0))
#Q15: Create a function that returns factorial of a number using loop
def factorial(n):
    if n < 0:
       return "Factorial not defined for negative numbers"
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factorial(5))
print(factorial(-4))
#Q16: Create a function that counts digits in a number
def count_digit(n):
    return len(str(abs(n)))
print(count_digit(12345))
#Q17: Create a function that reverses a number
def reverse_number(nums):
   sign = -1 if nums < 0 else 1
   return sign * int(str(abs(nums))[::-1])
print(reverse_number(1234))
print(reverse_number(-1234))
#Q18: Create a function that checks whether a number is Palindrome
def check_palindrome(nums):
   return "Palindrome" if abs(nums) == int(str(abs(nums))[::-1]) else "Not Palindrome"
print(check_palindrome(121))
print(check_palindrome(123))
print(check_palindrome(-121))
#Q19: Create a function that checks whether a number is Prime
# Return True or False.
def check_prime(num):
    if num <= 1:
       return False
    for i in range(2,num):
        if num % i == 0:
           return False
    return True
print(check_prime(5))
print(check_prime(4))
print(check_prime(-1))
# Q20: Create a function that returns multiplication table of a number
def multi_table(num):
    return [num * i for i in range(1,11)]
print(multi_table(5))
print(multi_table(4))
