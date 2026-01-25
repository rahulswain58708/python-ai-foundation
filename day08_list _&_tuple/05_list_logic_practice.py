#Q14.Take a list of numbers and find the largest number
nums = [int(x) for x in input("Enter numbers:").split()]
largest_num = nums[0]
for num in nums:
    if num > largest_num:
        largest_num = num
print(f"Largest number = {largest_num}")
#Q15.Create a new list that contains only numbers greater than 10 from an existing list.
numbers = [1,2,5,8,12,13,25,9,55,82]
li = []
for num in numbers:
    if num > 10:
        li.append(num)
print(li)