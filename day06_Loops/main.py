#For Loop
#the for loop is used when we know how many times we want to repeat task.
#Example:- print numbers 1 to 10.
for i in range(1,11):
    print(i)
#Example:- print a message 3 times
for i in range(3):
    print("Hello, Rahul")
#range() function generate sequence of number
for i in range(2,11,2):
    print(i)
    #While Loop
# The while loop runs as long as condition is True
i = 1
while i <= 5:
    print(i)
    i += 1
#Nested Loop
#Loop inside another loop.
for i in range(1,5):
    for j in range(1,5):
        print(i,j)
# inner loop runs completely for every single outer loop.