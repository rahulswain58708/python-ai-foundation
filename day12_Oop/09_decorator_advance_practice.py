#Q6 – check_positive
# Create a decorator named check_positive.
# Requirement:
# The decorated function will receive one number.
# If the number is negative, print:
# Invalid
# and do NOT call the function.
# If the number is 0 or positive, call the function normally.
def check_positive(func):
    def wrapper(n):
        if n < 0:
            print("Invalid")
        else:
            func(n)
    return wrapper
@check_positive
def numbers(num):
    print(f"{num} is positive✅")
numbers(5)
numbers(-7)
#Q7 – multiply_result
# Create a decorator named multiply_result.
# Requirement:
# The decorated function returns a number.
# The decorator should multiply the return value by 2 and return it.
def multiply_result(func):
    def wrapper(*args,**kwargs):
        return_num = func(*args,**kwargs)
        return return_num * 2
    return wrapper

@multiply_result
def get_num(num):
    return num
print(get_num(5))
# Q8 – type_checker
# Create a decorator named type_checker.
# Requirement:
# The decorated function should accept one argument.
# If the argument is not an integer, print:
# Invalid type
# and do NOT call the function.
# If the argument is an integer, call the function normally.
def type_checker(func):
    def wrapper(n):
        if type(n) != int:
            print("Invalid type")
        else:
            func(n)
    return wrapper

@type_checker
def get_Value(num):
    print(f"Number is {num}")
get_Value("Rahul")
get_Value(5)
