#Q6.Take a string and count how many times the letter 'a' appears in it.
s = input("Enter a string:").lower()
print(s.count('a'))
#Q7.Take a string and replace the word "Java" with "Python".
s1 = input("Enter a string:").lower()
print(s1.replace("java","python"))
# Q8.Take a string and remove extra spaces from the start and end.
s2 = input("Enter a string:")
print(s2.strip())
#Q9.Take a string and check whether it starts with "Hello".
s3 = input("Enter a string:").lower()
print(s3.startswith("hello"))
#Q10.Take a string and print it's Reverse.
s4 = input("Enter a string:")
print(s4[::-1])