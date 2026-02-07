#Inheritance:- Inheriance allow us to define a class inherit all method and properties from another class.
#parent class => Base class
#child class => derived class
#Q. Create a program using Single Inheritance:
# Step 1
# Create a class Person
# Variable: name
# Method: show_name() → prints name
# Step 2
# Create a class Student that inherits Person
# Variable: marks
# Use super() inside constructor
# Method: show_details() → prints name and marks
class Person:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print("Name:",self.name)
class Student(Person):
    def __init__(self, name,mark):
        super().__init__(name)
        self.mark = mark
    def show_details(self):
        self.show_name()
        print(f"Mark:{self.mark}")
s1 = Student("Rahul",450)
s1.show_details()
