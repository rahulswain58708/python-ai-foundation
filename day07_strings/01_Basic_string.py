#string is a sequence of character write inside single or double quotes.string can be letter,number,symbol anything
#inside quotes. String are immutable,cannot change.
#Creating String
s1 = "Rahul"
s2 = "Rohit"
print(s1,s2)
#Multiline string:- Used triple single or double quotes for creating multiline string.
s = """This is a triple 
      Double quotes used for creating multiline string"""
text = '''This is a triple single 
       quotes used for creating
       multiline string'''
print(s)
print(text)
#string indexing:- Each character in a string has position called index.
#Positive index starts from 0 the left.
#Negative index start -1 the right.
name = "Rahul"
print(name[0])#R
print(name[1])#a
print(name[-1])#l
print(name[-2])#u
#string slicing:- slicing allow you to extract portion of a string .
#using this syntax:- String[start:stop:step]
word = "apple"
print(word[0:3]) #app
#string iteration:-you can loop through character one by one .
lang = "Hindi"
for char in lang:
    print(char)
#Strings Are immutable:- Strings are immutable they are cannot change after they created.
#if we need manipulate strings then we can use methods,like concatenation,slicing or formating
# to create new string based on original.
x = "hello"
x = "H" + x[1:]
print(x)
