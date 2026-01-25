#List:- A list is a collection of multiple values stored in one variable.
#list are ordered.
#list are mutable
#list store different datatypes
#Example
numbers = [1,2,3,4]
names = ["Rahul","Aman","Akash","Amit"]
mixed = [1,"AI",3.5,True]
#Acess List element
nums = [10,20,30,40]
print(nums[0]) #output:- 10
print(nums[1]) #output:- 20
print(nums[2]) #output:- 30
print(nums[-1]) #output:- 40
#List slicing
print(nums[0:3]) #[10,20,30]
print(nums[1:4]) #[20,30,40]
print(nums[2:]) #[30,40]
#list are mutable
nums[1] = 2
print(nums)
#looping through a list
fruits = ["apple","banana","orange","mango"]
for fruit in fruits:
    print(fruit)
#common List method
numbers = [1,2,3]
numbers.append(4)
numbers.insert(4,5)
numbers.remove(2)
numbers.pop()
numbers.sort()
numbers.sort(reverse=True)
print(len(numbers))
print(3 in numbers)
print(numbers)
#Tuple:- tuple is a collection of multiple value but tuple are immutable (cannot change) and tuple writing inside parantheses ().
#creating a tuple
t = (10,20,30)
print(t)
#Accessing Tuple element
print(t[0])
#slicing tuple element
print(t[0:2])