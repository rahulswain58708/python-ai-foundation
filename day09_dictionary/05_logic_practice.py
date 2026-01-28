#Q15.Given a dictionary of students and marks, find the student with the highest marks
# (do NOT use max()).
students = {
    "s1":[35,48,65,85],
    "s2":[48,95,91,31],
    "s3":[55,98,89,76]
}
highest_mark = 0
top_student = ""
for student,marks in students.items():
    total = 0
    for mark in marks:
        total += mark
    if total > highest_mark:
        highest_mark = total
        top_student = student
print(f"Top_Student:{top_student}|Highest_mark = {highest_mark}")
