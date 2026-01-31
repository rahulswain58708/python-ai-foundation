#Q31: Create a function that adds any number of values.
def adds_number(*args):
    total = 0
    for num in args:
        total += num
    return total
print(adds_number(1,2,3,4,5))
print(adds_number(5,25,65))
#Q32: Create a function that returns maximum from given numbers.
def max_num(*args):
    return max(args)
print(max_num(1,2,3,4))
print(max_num(-10,90,50,-50))
#Q33: Create a function that returns minimum from given numbers.
def min_num(*args):
    return min(args)
print(min_num(-10,10,-50,5,60))
print(min_num(5,75,85,-9,-45))
#Q34: Create a function that calculates average of numbers.
def calculate_avg(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)
print(calculate_avg(4,5,6))
print(calculate_avg(95,65,85))
#Q35: Create a function that counts how many numbers were passed.
def count_nums(*args):
    count = 0
    for num in args:
        count += 1
    return count
print(count_nums(15,56,25,8,7))