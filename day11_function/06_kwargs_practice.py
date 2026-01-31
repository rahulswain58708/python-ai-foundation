#Q36: Create a function that accepts student details and prints them nicely.
def student_details(**kwargs):
    print("Student Details")
    print('-----------------')
    for key,value in kwargs.items():
        print(f"{key}:{value}")
student_details(name = "Rahul", course = "Bsc cs",roll_no = 65)
student_details(name= "Amit",course = "Arts",roll_no = 85)
#Q37: Create a function that returns only keys from kwargs.
def key(**kwargs):
    return kwargs.keys()
print(key(Rahul = 18,amit = 65))
#Q38: Create a function that returns only values from kwargs.
def value(**kwargs):
    return kwargs.values()
print(value(Rahul = 18,amit = 65))
#Q39: Create a function that checks if "age" exists in kwargs.
def check_age(**kwargs):
    return "exist" if "age" in kwargs else "Not exist"
print(check_age(name = "Rahul",age = 18))
#Q40: Create a function that prints all key-value pairs line by line.
def key_value(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)
key_value(name = "Rahul",age = 18,id = 1)