#Q6.Take a number n as input and print numbers from 1 to n.
n = int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)
# #Q7.Take a number as input and print its multiplication table from 1 to 10 using a loop.
num = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
# #Q8.Take a number n as input and calculate the sum of numbers from 1 to n using a loop.
number = int(input("Enter a number:"))
total = 0
for i in range(1,number+1):
    total += i
print(total)
#Q9.Take a number as input and calculate its factorial using a loop.
x = int(input("Enter a number:"))
fact = 1
for i in range(1,x+1):
    fact *= i
print(fact)

#Q10.Count how many numbers between 1 and 50 are divisible by 5 using a loop.
count = 0
for i in range(1,51):
    if i % 5 == 0:
        count += 1
print(count)
