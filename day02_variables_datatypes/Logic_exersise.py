# Store:
# price = "199" (string)
# quantity = 3
# Convert price to integer and calculate total cost.
price = "199"
quantity = 3
total = int(price) * quantity
print("total cost:",total)
# Take age as input and check:
# print the data type before conversion
# convert it into integer
# print the data type after conversion
age = input("Enter age:")
print("before:",type(age))
age_int = int(age)
print("after:",type(age_int))
# Store marks as float, convert it to integer, and explain the result in a comment.
mark = 75.5
mark_int = int(mark)
print(mark_int) #after conversion int mark is 75 