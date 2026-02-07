# Q1. __str__
# Create class Book
# Attributes: title, author
# When printing object, output:
# Book: Python by Rahul
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
b1 = Book("pysimplify","Rahul")
print(b1)
#Q2 – __len__
# Create class Playlist
# Attribute: songs (list of song names)
# Implement __len__ so that:
# len(playlist)
class Playlist:
    def __init__(self,songs):
        self.songs = songs
    def __len__(self):
        return len(self.songs)
playlist = Playlist(["Ranjhaa","Kar har maidan","Ore priya"])
print(len(playlist))
#Q3 – __add__
# Create class Number
# Attribute: value
# Implement __add__ so that you can add two objects using +
class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value
n1 = Number(50)
n2 = Number(50)
print(n1 + n2)
#Q4 – __eq__
# Create class Student
# Attributes: name, marks
# Two students should be considered equal if their marks are same.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __eq__(self, value):
        return self.marks == value.marks
s1 = Student("Rahul",85)
s2 = Student("Akash",84)
print(s1 == s2)
#Q5 – __gt__ (Greater Than)
# Create class Car
# Attributes: brand, speed
# Compare two cars using > based on speed.
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def __gt__(self,other):
        return self.speed > other.speed
c1 = Car("Tesla",56)
c2 = Car("Suzuki",45)
print(c1 > c2)
# Q6 – __getitem__
# Create class Library
# Attribute: books (list of book names)
# Allow accessing books using indexing:
# lib[0]
# lib[1]
class Library:
    def __init__(self,books):
        self.books = books
    def __getitem__(self,index):
        return self.books[index]
lib = Library(["c programming","think python","pysimplify"])
print(lib[0])
print(lib[1])
#Q7. Create class Vector
# Attributes: x, y
# Multiply vector with a number:
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self,other):
        return self.x * other , self.y * other
v = Vector(5,6)
print(v * 3)
# Q8 – __contains__
# Create class Team
# Attribute: players (list of player names)
class Team:
    def __init__(self,players):
        self.players = players
    def __contains__(self,other):
        return other in self.players
t1 = Team(["Virat","Rohit","msd","surya","kl Rahul"])
print("Ruturaj" in t1)