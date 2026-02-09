#File Handling means creating ,opening, reading, writing or closing files using python.
# Q1. Create & Write
# Write a program that:
# Creates a file named intro.txt
# Writes the line:
# Learning Python File Handling
with open("intro.txt","w") as file:
    file.write("Learning Python File Handling\n")
# Q2. Read File
# Question
# Write a Python program that:
# Opens the file intro.txt
# Reads its content
# Prints the content on the screen
with open("intro.txt","r") as file:
    print(file.read())
# Q3. Append Data
# Question
# Write a Python program that:
# Opens the file intro.txt
# Appends the line
# This is my first file program
# Keeps the old content safe (do NOT overwrite)
with open("intro.txt","a") as file:
    file.write("This is my first file program")
# Q4. Read Line by Line
# Question
# Write a Python program that:
# Opens the file intro.txt
# Reads the file line by line
# Prints each line separately
with open("intro.txt","r") as file:
    for line in file:
        print(line.strip())
# Q5. Count Lines
# Question
# Write a Python program that:
# Opens the file intro.txt
# Counts how many lines are present in the file
# Prints the total number of lines
with open("intro.txt",'r') as file:
    count = 0
    for line in file:
        count +=1
    print(f"total number of lines = {count}")