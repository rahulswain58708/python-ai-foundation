#Q18.print the pattern using nested loops.
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
#Q19.Print the following pattern using nested loops:
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()
#Q20.print multiplication table 1 to 5 using nested loop.
for i in range(1,6):
    print(" ")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")