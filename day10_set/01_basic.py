#Q1.Create a set of 5 numbers and print it.
s = {1,2,3,4,5}
print(s)
#Q2.Create a list with duplicate values and convert it into a set, then print the set.
lst = [10,20,20,10,30,40,40]
st = set(lst)
print(st)
#Q3.Check whether a number exists in a set.
nums = {5,15,25,35,45}
if 10 in nums:
    print("exist")
else:
    print("Not exist")
#Q4. Add a new element to a set.
nums.add(10)
print(nums)
#Q5.Remove an element from a set using both methods:
nums.remove(25)
nums.discard(35)
print(nums)