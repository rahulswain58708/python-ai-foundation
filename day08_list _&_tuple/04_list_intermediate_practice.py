#Q11.Print all elements of a list using a for loop.
fruits = ["apple","banana","orange","mango"]
for fruit in fruits:
    print(fruit)
#Q12.Take a list of numbers and calculate the sum of all elements
nums = [10,15,20,25,30]
total = 0
for num in nums: 
    total += num
print(total)
#Q13.Take a list of numbers and count how many even numbers it contains.
numbers = [2,3,4,8,13,9,12,15]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print(f"even_numbers = {count}")