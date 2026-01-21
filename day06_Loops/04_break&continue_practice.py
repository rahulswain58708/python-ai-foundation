#Q15.print numbers from 1 to 20 but stop loop when the number become 13.
for i in range(1,21):
    print(i)
    if i == 13:
        break
#Q16.Print numbers from 1 to 20, but skip numbers divisible by 3.
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)
#Q17.Take a number n as input and print numbers from 1 to n, but skip even numbers.
n = int(input("Enter a number:"))
for i in range(1,n+1):
    if i % 2 == 0:
        continue
    print(i)