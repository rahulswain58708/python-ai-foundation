#Q16.From a dictionary of students and marks, create two new dictionaries:
# Pass → total marks ≥ 40 per subject average OR percentage ≥ 40
# Fail → below that
students = {
    "s1": [35, 48, 65, 85],
    "s2": [48, 95, 91, 31],
    "s3": [15, 18, 20, 25],
    "s4": [55, 65, 75, 80]
}
pass_student = {}
fail_student = {}
for student,marks in students.items():
    total = 0
    no_of_sub = len(marks)
    for mark in marks:
        total += mark
    percentage = (total / (no_of_sub*100)) * 100
    if percentage >= 40:
        pass_student[student] = percentage
    else:
        fail_student[student] = percentage
print(f"pass student = {pass_student}")
print(f"fail student = {fail_student}")
#Q17.Search for a student name in a dictionary and print:
# "Found" if exists
# "Not Found" otherwise
# Rules:
# Use loop or in
# Clean logic
profile = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 90
}

name = input("Enter student name:")

if name in profile:
    print("Found")
else:
    print("Not Found")
# Q18.Count how many students scored above 75 marks.
s = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 90,
    "Rohit": 65
}
count = 0
for mark in s.values():
    if mark > 75:
        count += 1
print(f"count = {count}")
