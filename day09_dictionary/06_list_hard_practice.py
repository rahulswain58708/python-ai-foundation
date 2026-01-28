#Q16.Remove duplicate elements from a list while keeping the original order.
nums = [1,2,3,10,20,30,2,3]
new_li = []
for num in nums:
   if num not in new_li:
      new_li.append(num)
print(new_li)
#Q17.Reverse a list without using:
# reverse()
# slicing ([::-1])
li = [1,2,3,4]
reverse_li = []
for i in range(len(li)-1,-1,-1):
    reverse_li.append(li[i])
print(reverse_li)
#Q18.Merge two lists into a single list.
# Use loop logic
# Do not use + operator (logic practice)
li_1 = [1,2,3]
li_2 = [4,5,6]
for num in li_2:
   li_1.append(num)
print(li_1)
