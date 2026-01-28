#Dictionary:- dictionary store data in key:value pairs.
#dict are mutable
#dict are ordered(python 3.7+)
#key are unique
#value can be anything
#Creating dict
empty_dic = {}
person = {"name":"Rahul","age":18,"marks":[10,50,25]}
print(person)
#Acessing value
print(person["name"]) #Rahul
print(person["age"]) #18
#if key does not exist give error
#safe way (get)
#if key does not exist give "None".
print(person.get("city")) #None
print(person.get("marks")) #[10, 50, 25]
#Adding/Update
person["city"] = "Delhi"
person["age"] = 19
#python check if key exist then update not exist create this key.
print(person)
#Removing items
person.pop("city")
del person["marks"]
# person.clear() empty dict
print(person)
#Looping Through Dictionary
student = {"name":"Rahul","class":"+3 first year","course":"computer science"}
for key in student:
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key,value)
#check key exist
if "course" in student:
    print("course exist")
#Nested dictionary
students = {
    1:{"name":"Rahul","age":18,"course":"python"},
    2:{"name":"amit","age":19,"course":"computer science"}
}
print(students)
# dictionary methods
print(students.keys())
print(students.values())
print(students.items())
#Mutability
data = {"a": 10}
data["a"] = 5
print(data)