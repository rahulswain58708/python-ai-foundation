#Q1.Create a dictionary with keys: name, age, course and print it.
student = {
    "name":"Rahul",
    "age":18,
    "course":"python"
}
print(student)
#Q2.Access and print:
# the value of name
# the value of age
print(student["name"])
print(student["age"])
#Q3.Use .get() to access a key that does not exist and print the result.
print(student.get("city")) #output:-None
#Q4.Add a new key city to the dictionary and update age
student["city"] = "Delhi"
student["age"] = 19
print(student)
#Q5.Delete the key city from the dictionary.
del student["city"]
print(student)