# Q6. User Input to File
# Question
# Write a Python program that:
# Takes user name and age as input
# Stores them in a file named user.txt
# 📌 Output Format in File
# Name: Rahul
# Age: 18
name = input("Enter user name:- ")
age = int(input("Enter your age:- "))
with open("user.txt","w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
print("Details Stored in User.txt File Sucessfully")
# Q7. Read Using with Statement
# Question
# Write a Python program that:
# Opens the file user.txt
# Reads its content
# Prints the content on the screen
# Uses only with statement
# 📌 Conditions
# Use read mode
# Do not use close()
# Output should show exactly what is inside the file
with open("user.txt","r") as file:
    print(file.read())
# Q8. File Exists Check
# Question
# Write a Python program that:
# Checks whether the file user.txt exists or not
# If the file exists → print
# File Found
# If the file does not exist → print
# File Not Found
# 📌 Conditions
# Use the os module
# Do not open the file
# Only check existence
import os 
if os.path.exists("user.txt"):
    print("File Found")
else:
    print("File Not Found")

# Q9. Multiple Lines Write
# Question
# Write a Python program that:
# Stores 5 programming languages in a file named languages.txt
# Each language should be on a new line
# 📌 Conditions
# Use write mode
# Use best practice for file handling
# You can choose any 5 languages
programming_languages = ["C Programming\n","Java\n","C++\n","Python\n","JavaScript\n"]
with open("languages.txt","w") as file:
    file.writelines(programming_languages)
# Q10. Copy File Content
# Question
# Write a Python program that:
# Reads data from languages.txt
# Copies the same data into a new file named backup.txt
# 📌 Conditions
# Use read mode for languages.txt
# Use write mode for backup.txt
# Use best practice (with statement)
with open("languages.txt","r") as file:
    data = file.read()
with open("backup.txt","w") as file:
    file.write(data)