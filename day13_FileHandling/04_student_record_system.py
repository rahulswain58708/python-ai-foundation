# Q13. Student Record System (File-Based)
# Question
# Write a Python program that:
# Takes student name and marks from the user
# Saves them into a file named students.txt
# Allows adding multiple students using a loop
# 📌 File Format (example)
# Name: Rahul, Marks: 85
# Name: Amit, Marks: 78
# Name: Sita, Marks: 92
# 📌 Conditions
# Use append mode (do NOT overwrite old data)
# Use with statement
# Use a loop to add multiple records
# Stop the loop when user says no
# 🔍 Hint (Not Solution)
# Use while True
# Take input for name & marks
# Write one student per line
# Ask user: “Add another student? (yes/no)”
while True:
    print("--------------Welcome to Student Record System--------------")
    student_name = input("Enter student name:- ")
    marks = float(input("Enter Student marks(0-100):- "))
    with open("students.txt","a") as file:
        file.write(f"Name: {student_name}, Marks: {marks}\n")
    choice = input("Add another student(yes/no):- ").lower()
    if choice == "no":
        break
    elif choice == "yes":
        continue
    else:
        print("Invalid Choice Enter yes or no❌")
        break