# Take a number as input and check:
# If the number is divisible by both 3 and 5 → print "Divisible by both"
# Else if divisible by only 3 → print "Divisible by 3"
# Else if divisible by only 5 → print "Divisible by 5"
# Else → print "Not divisible by 3 or 5"
num = int(input("Enter a number:"))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 3 or 5")