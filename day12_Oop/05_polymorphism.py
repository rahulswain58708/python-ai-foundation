#Polymorphism means one method behave different in different situation.
# Task:
# Create a program that shows Method Overriding (Polymorphism).
# Requirements:
# Create a class Vehicle
# Method: start() → prints "Vehicle is starting"
# Create a class Car that inherits Vehicle
# Override start() → prints "Car is starting"
# Create an object of Car
# Call start() using the object
# Output should show child class behavior
class Vehicle:
    def start(self):
        print("Vehicle is starting..")
class Car(Vehicle):
    def start(self):
        print("Car is starting..")

my_car = Car()
my_car.start()

#Task:- Create a program that shows Polymorphism using multiple child classes.
# Requirements:
# Create a class Shape
# Method: draw() → prints "Drawing a shape"
# Create a class Circle that inherits Shape
# Override draw() → prints "Drawing a circle"
# Create a class Rectangle that inherits Shape
# Override draw() → prints "Drawing a rectangle"
# Create objects of Circle and Rectangle
# Call draw() for both objects
# Output should show different behavior for same method name
class Shape:
    def draw(self):
        print("Drawing a shape")
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")
s1 = Circle()
s2 = Rectangle()
s1.draw()
s2.draw()
