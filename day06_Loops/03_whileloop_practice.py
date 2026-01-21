#Q11.print numbers 1 to 10 using while loops.
i = 1
while i <= 10:
    print(i)
    i += 1
#Q12.Print numbers from 10 to 1 using a while loop.
a = 10
while a >= 1:
    print(a)
    a -= 1
#Q13.Keep asking the user to enter a number until they enter 0.
n = int(input("Enter a number"))
while n != 0:
    n = int(input("Enter a number"))
#Q14.Keep taking numbers from the user and calculate the total sum until the user enters 0.
x = int(input("Enter a number:"))
total = 0
while x != 0:
    total += x
    print(f"sum = {total}")
    x = int(input("Enter a number:"))