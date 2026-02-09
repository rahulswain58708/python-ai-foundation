# 🔴 Q15. Menu-Based Notes Application (File Handling)
# Question
# Create a menu-driven Python program that allows the user to manage notes using file handling.
# 📋 Menu Options
# 1. Add Note
# 2. View Notes
# 3. Exit
# 📌 Requirements
# 1️⃣ Add Note
# Take note text from the user
# Save it in a file named notes.txt
# Use append mode
# Each note should be saved on a new line
# 2️⃣ View Notes
# Read all notes from notes.txt
# Print them on the screen
# If file does not exist, show a proper message
# 3️⃣ Exit
# Stop the program safely
# 📌 Conditions
# Use while loop for menu
# Use with statement
# Use os.path.exists() to check file existence
# Do not use file pointer (seek, tell)
# Program should not crash
import os

def add_note():
    note = input("Enter note text:-")
    with open("notes.txt","a") as file:
        file.write(note + "\n")
        print("Notes added sucessfully✅")
def view_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt","r") as file:
            print("📒 Your Notes:",file.read())
    else:
        print("File Not Found ❌")
def menu():
    while True:
        print("--------Welcome to note application--------")
        print("1.Add note")
        print("2.View notes")
        print("3.Exit")
        option = input("Enter one option:- ")
        if option == '1':
            add_note()
        elif option == '2':
            view_notes()
        elif option == '3':
            print("Thanks for using note application 🤗")
            break
        else:
            print("Invalid option  try again ❌")
menu()
