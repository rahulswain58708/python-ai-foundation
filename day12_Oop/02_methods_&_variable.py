#Q11: Create a class with instance variable and class variable.
class Student:
    college = "Pattamundei Degree College"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Hii iam {self.name} and {self.age} years old student of {Student.college}")
s1 = Student("Rahul",18)
s1.show()
#Q12: Create method that returns square of a number.
class Mathmatics:
    @staticmethod
    def square(n):
        return n**2
#Q13: Create method that accepts two numbers and prints sum.
    @staticmethod
    def add(a,b):
        return a+b
print(Mathmatics.square(5))
print(Mathmatics.add(2,18))
#Q14: Create class Bank with deposit() and withdraw() methods.
class Bank:
    bankbalance = 0
    @classmethod
    def deposite(cls,amount):
        cls.bankbalance += amount
        return f"Total Balance = {cls.bankbalance}"
    @classmethod
    def withdraw(cls,amount):
        if amount > cls.bankbalance:
            return "Insufficent Balance"
        else:
            cls.bankbalance -= amount
            return f"Available Balance = {cls.bankbalance}"
print(Bank.deposite(50))
print(Bank.withdraw(20))
#Q15: Create method that checks even or odd.
class CheckEvenOdd:
    @staticmethod
    def check(n):
        return "Even" if n%2 == 0 else "Odd"
print(CheckEvenOdd.check(5))
print(CheckEvenOdd.check(8))
#Q16: Create class Student with display() method.
class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def display(self):
        print(f"Student_Name:{self.name}|Marks = {self.mark}")
s1 = Student("Akash",19)
s1.display()
#Q17: Create static method that prints "Welcome".
class Welcome:
    @staticmethod
    def print_welcome():
        print("Welcome")
Welcome.print_welcome()
#Q18: Create class method that prints school name.
class School:
    school_name = "ABC School"
    @classmethod
    def print_name(cls):
        print(cls.school_name)
School.print_name()
#Q19: Create class Calculator with add, subtract, multiply.
class Calculator:
    @staticmethod
    def add(a,b):
        print(f"add = {a+b}")
    @staticmethod
    def sub(a,b):
        print(f"Substract = {a-b}")
    @staticmethod
    def multiply(a,b):
        print(f"multiply = {a*b}")
Calculator.add(5,5)
Calculator.sub(10,5)
Calculator.multiply(7,3)
#Q20: Create object and call all methods.
cal = Calculator()
cal.add(8,2)
cal.sub(9,1)
cal.multiply(9,5)
