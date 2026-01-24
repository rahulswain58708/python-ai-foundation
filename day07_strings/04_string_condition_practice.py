#Q11.Take a string and check:
# Print "Uppercase" if the string is all uppercase
# Otherwise print "Not uppercase"
s = input("Enter a string:")
if s == s.upper():
    print("uppercase")
else:
    print("Not uppercase")
#Q12.Take a string and check whether it is a palindrome.
s1 = input("Enter a string:").lower()
if s1 == s1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#Q13.Take a string and count:
# number of vowels
# number of consonants
s2 = input("Enter a string:")
vowels = "aeiou"
count_constant = 0
count_vowels = 0
for char in s2:
    if char.isalpha():
        if char in vowels:
            count_vowels += 1
        else:
            count_constant += 1
print("vowels:",count_vowels)
print("constant:",count_constant)
#Q14.Take a string and check whether it contains only digits.
s3 = input("Enter a string:")
print(s3.isdigit())