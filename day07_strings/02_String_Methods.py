#String Methods and Function:-Python provide variety of string method and built-in Function.
#common string method
#changing case
text = "hello world"
print(text.upper()) #output:- HELLO WORLD
print(text.lower()) #output:- hello world
print(text.capitalize()) #output:- Hello world
print(text.title()) #output:- Hello World
print(text.swapcase()) #small letter -> <- capital letter output:-HELLO WORLD
#Remove White Space
s = " Hello Python "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
#Finding & Replace
#find method search substring with in a main string and return index of first occurrence,if not found return -1.
print(s.find('H'))
#Replace
sentence = "Rahul is a good boy"
print(sentence.replace("good","bad"))
#spliting and joining
#split:- split method in python break string into list of substring based on specific separator,if no separator given
#by default split white space.
fruits = "apple,banana,orange"
x = fruits.split(",")
new_text = "-".join(x)
print(new_text)
#check properties in string
s1 = "Python123"
print(s1.isalpha())
print(s1.isdigit())
print(s1.isspace())
print(s1.isalnum())
