#Decorator is a function that takes another function add extra behavior with out changing original function
# Q1.Create decorator simple_logger
# Print before function:
# Function started
# and after function:
# Function ended
def simple_logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper
@simple_logger
def say_hi():
    print("Hii")
say_hi()
#Q2.Create a decorator named uppercase_output.
def uppercase_output(func):
    def wrapper():
        value = func()
        return value.upper()
    return wrapper
@uppercase_output
def greet():
    return "hello rahul"
print(greet())
# Q3 – double_run
# Create a decorator named double_run.
# Requirement:
# The decorated function should execute two times when called.
def double_run(func):
    def wrapper():
        func()
        func()
    return wrapper
@double_run
def greet():
    print("Hello Rahul")
greet()
# Q4 – star_wrapper
# Create a decorator named star_wrapper.
# Requirement:
# Before the function runs, print:
# ********
# After the function runs, print:
# ********
def star_wrapper(func):
    def wrapper():
        print("********")
        func()
        print("********")
    return wrapper
@star_wrapper
def say_hello():
    print("hello")
say_hello()
# Q5 – hello_decorator
# Create a decorator named hello_decorator.
# Requirement:
# Before the function runs, print:
# Hello User
def hello_decorator(func):
    def wrapper():
        print("Hello User")
        func()
    return wrapper
@hello_decorator
def greet():
    print("Welcome🎉")
greet()