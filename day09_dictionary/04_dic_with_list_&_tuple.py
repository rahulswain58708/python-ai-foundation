#Q11.Create a dictionary where:
# key = student name
# value = list of marks
# Print the total marks of the student.

student = {
    "Rahul":[20,25,30,55]
}
total = sum(student.get("Rahul"))
print("sum =",total)
#Q12.From the same dictionary, print average marks.
average_ = total/len(student.get("Rahul"))
print("average = ",average_)
#Q13.Create a dictionary where:
# key = roll number
# value = tuple (name, age)
# Print student details using tuple unpacking.
d = {
    1:("Rahul",18)
}
t = d[1]
name,age = t
print(f"Name:{name},age:{age}")
#Q14.Loop through a dictionary and print only keys whose value is a list.
person = {
    "name":"Rahul",
    "age":18,
    "goal":"Ai engineer",
    "marks":[10,20,30]
}
for keys,values in person.items():
    if isinstance(values,list):
        print(keys)
