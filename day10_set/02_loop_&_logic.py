#Q6.Print all elements of a set using a loop.
s = {1,2,3,4,5}
for item in s:
    print(item)
#Q7.Count how many elements are present in a set without using len().
count = 0
for num in s:
    count += 1
print(f"count = {count}")
#Q8.Find the maximum value in a set without using max().
nums = {10,20,40,50}
max_num = -1
for n in nums:
    if n > max_num:
        max_num = n
print(f"max_number = {max_num}")
#Q9.Find the minimum value in a set without using min().
mini_num = 100000000000000
numbers = {10,20,80,40}
for i in numbers:
    if i < mini_num:
        mini_num = i
print(mini_num)
#Q10.Create a new set that contains only even numbers from an existing set.
s1 = {4,9,5,2,3,6,7}
even_set = set()
for j in s1:
    if j % 2 == 0:
        even_set.add(j)
print(even_set)
