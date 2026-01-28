#Q19.find the key with the highest value.
data = {
    "python": 5,
    "java": 3,
    "ai": 7,
    "ml": 4
}
highest_key = ""
highest_value = -1
for key,value in data.items():
    if value > highest_value:
        highest_value = value
        highest_key = key
print(highest_key)
#Q20.Create a dictionary from user input where:
# key = subject name
# value = marks
# Then calculate:
# total marks
# average marks
student = {}
total = 0
no_of_sub = int(input("Enter How many subjects:"))
for i in range(1,no_of_sub+1):
    sub = input(f"Enter subject {i} name:")
    marks = float(input(f"Enter subject {i} mark:"))
    student[sub] = marks
    total += marks
average_mark = total/no_of_sub
print(student)
print(f"Total Marks = {total}")
print(f"Average Marks = {average_mark}")
#Q21.Reverse dict key become value & value become key
d = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 90
}
m = {}
for key,value in d.items():
    m[value] = key
print(m)
