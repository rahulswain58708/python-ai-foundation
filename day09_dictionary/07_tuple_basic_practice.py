#Q19.Create a tuple of 5 elements and print it.
t = (1,2,3,4,5)
print(t)
#Q20.From the tuple, print:
# the first element
# the last element
print(t[0])
print(t[-1])
#Q21.Try to change an element in the tuple and observe what happens.
# t[0] = 10
# print(t) TypeError: 'tuple' object does not support item assignment
# We cannot change a tuple because tuples are immutable and store fixed data.

# Q22. Tuple ↔ List Conversion (Very Important)
# Question:
# Convert a tuple into a list
# Modify the list
# Convert it back into a tuple
# Print the final tuple
nums = (1,2,3,4)
li_nums = list(nums)
li_nums.append(5)
li_tuple = tuple(li_nums)
print(li_tuple)

#Q23.Given a list of numbers:
# Find the minimum value
# Find the maximum value
# Store both values inside a tuple
# Print the tuple
numbers = [10,20,35,40,50,25,30]
min_num = numbers[0]
max_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
result = (min_num,max_num)
print(result)