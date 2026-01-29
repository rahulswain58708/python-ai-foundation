#Q14.Remove duplicate characters from a string using a set.
ch = "programming"
s  = set(ch)
print(f"after_remove_duplicate = {s}")
#Q15.Count how many unique words are present in a sentence.
# Task:
# Take a sentence (string)
text = input("Enter a text:").lower()
# Split it into words
word = text.split()
# Use a set to find unique words
st = set(word)
unique_element = len(st)
# Print the count
print(f"unique word = {unique_element}")
#Q16.Given two lists, find:
# 1.Common elements
# 2.Unique elements (elements that are not common)
l1 = [1,2,3,4,5,6,7,8]
l2 = [5,6,7,8,9,10]
s1 = set(l1)
s2 = set(l2)
print(f"common_element = {s1.intersection(s2)}")
print(f"unique_element = {s1.symmetric_difference(s2)}")