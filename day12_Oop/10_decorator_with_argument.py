#Q9 – repeat_n_times(n)
# Create a decorator with argument named repeat_n_times(n).
# Requirement:
# The decorator should take a number n.
# The decorated function should run n times when called.


import functools #step1:- import functools for taking argument with decorator
def repeat_n_times(num): #step2:- create a repeat_n_times(num) decorator.
    def decorator_with_argument(func):#step3:- Create a decorator decorator_with_argument(func) that take a function.
        @functools.wraps(func) #step4:-use functools module
        def wrapper():
            for i in range(num): #step5:- start loop from 0 to num-1 store inside i.
                func()         #step6:- call function i times
        return wrapper         #step7:- return wrapper
    return decorator_with_argument #step8:- return decorator with argument


@repeat_n_times(3) #step-9:- repeat_n_times(3) decorator paas 3 argument.
def greet(): # step10:- create a greet name function
    print("Hello World!") #step11:- print Hello World!
greet()
#step12:- When we call greet() function go to wrapper functionr.