📞 Contact Manager App (Python CLI)

A simple Contact Manager application built using Python Dictionary.
This project works completely in the terminal (CLI) and helps manage contacts efficiently.

🚀 Project Objective

To build a Python application that allows users to:

Add contacts

View all contacts

Search contacts

Update contacts

Delete contacts

The project is created using pure Python logic with no external libraries.

🧱 Data Structure Used
contacts = {
    "Rahul": 9876543210,
    "Amit": 9123456780
}


Key → Contact Name (unique)

Value → Phone Number

This design demonstrates strong understanding of dictionary (key–value) data structure.

📋 Features

1️⃣ Create Contact

Add a new contact with name and phone number

Prevents duplicate contact names

2️⃣ View All Contacts

Displays all saved contacts

Handles empty contact list safely

3️⃣ Update Contact

Update phone number of an existing contact

4️⃣ Search Contact

Search a contact by name

Displays phone number if found

5️⃣ Delete Contact

Delete a contact safely after checking existence

6️⃣ Exit

Close the application gracefully

🧠 Concepts Used

Python Dictionary

Key existence checking

Looping (for, while)

Conditional statements

CRUD operations (Create, Read, Update, Delete)

User input handling

📂 Project Structure
ContactManager/
│
├── main.py
└── README.md

▶️ How to Run

Clone this repository

Open terminal in the project folder

Run the program:

python main.py

🎯 Learning Outcome

This project helped me:

Gain confidence in Python dictionaries

Understand real-world CRUD operations

Improve logic building skills

Prepare for advanced topics like sets, functions, and file handling

🔜 Future Improvements (Optional)

Case-insensitive search

Prevent duplicate phone numbers

Save contacts to file

Load contacts on startup

Status: Project Completed ✅
Level: Beginner → Intermediate
