#Q1: Create a class Student with attributes name and age. Create one object and print values.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = Student("Rahul",18)
print(s1.name)
print(s1.age)
#Q2: Create a class Car with a method start() that prints "Car Started".
class Car:
    def start(self):
        print("Car Started")
tesla = Car()
tesla.start()
#Q3: Create a class Mobile with constructor that stores brand and price.
class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
m1 = Mobile("Nokia",1200)
m2 = Mobile("Samsung",1500)
print(m1.brand)
print(m1.price)
print(m2.brand)
print(m2.price)
#Q4: Create two objects of same class and show that values are different.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Hello {self.name} I am {self.age} years old.")
p1 = Person("Rahul",19)
p2 = Person("Amit",25)
p1.show()
p2.show()
#Q5: Create class Person with method introduce() that prints name.
class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f"Hello {self.name}")
p1 = Person("Akash")
p1.introduce()
#Q6: Create class Laptop and store ram, storage, price.
class Laptop:
    def __init__(self,ram,storage,price):
        self.ram = ram
        self.storage = storage
        self.price = price
l1 = Laptop("16GB",512,55000)
print(l1.ram)
print(l1.storage)
print(l1.price)
#Q7: Create a class Animal and call its method using object.
class Animal:
    def sound(self):
        print("Bow")
dog = Animal()
dog.sound()
#Q8: Create class Book and print book title using object.
class Book:
    def __init__(self,title):
        self.title = title
b1 = Book("Pysimplify")
print(b1.title)
#Q9: Create class Employee with name and salary.
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
e1 = Employee("Sankar",15000)
print(e1.name)
print(e1.salary)
#Q10: Create class School and print school name using class variable.
class School:
    school_name = "Chandra Sekhar Nodal High School"
s1 = School()
print(s1.school_name)