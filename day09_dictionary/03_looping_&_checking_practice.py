#Q6.Print all keys of a dictionary using a loop.
person = {"name":"Amit",
          "age":35,
          "work":"Amazon"}
for keys in person:
    print(keys)
#Q7 .Print all values of a dictionary using a loop.
for values in person.values():
    print(values)
#Q8.Print key and value together in this format:
for key,value in person.items():
    print(key,":",value)
#Q9.Check whether the key "marks" exists in the dictionary.
if "marks" in person:
    print("marks existed.")
else:
    print("marks not existed")
# Q10.Count how many keys are present in the dictionary.
count = 0
for keys in person:
    count += 1
print(f"Total keys = {count}")