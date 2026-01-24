#Q1.Take a string as input and print its length.
s = input("Enter a string:")
print(len(s))
#Q2.Take a string as input and print:
# the first character
# the last character
s1 = input("Enter a string:")
print("first character:",s1[0])
print("last character:",s1[-1])
#Q3.Take a string as input and print:
# the string in uppercase
# the string in lowercase
s2 = input("Enter a string:")
print(f"uppercase: {s2.upper()}")
print(f"lowercase: {s2.lower()}")
#Q4.Take a string and check whether the word "AI" exists in it.
s3 = input("Enter a string:").upper()
print("AI" in s3)
#Q5.Take a string as input and print each character on a new line using a loop.
s4 = input("Enter a string:")
for char in s4:
    print(char)