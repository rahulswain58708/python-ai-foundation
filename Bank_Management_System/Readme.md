# 🏦 Bank Management System (Python – OOP Project)

A simple **Bank Management System** built using **Python Object-Oriented Programming (OOP)** concepts.  
This project demonstrates how real-world banking operations can be implemented using classes, inheritance, and polymorphism.

---

## 🚀 Features

- Create new bank accounts
- Two account types:
  - **Saving Account**
  - **Current Account**
- Deposit money
- Withdraw money
  - Saving Account → normal balance rules
  - Current Account → overdraft facility
- Check account balance
- Display account details
- Menu-driven console application

---

## 🧠 OOP Concepts Used

This project is built to practice and demonstrate core OOP concepts:

- **Class & Object**
- **Encapsulation** (protected balance)
- **Inheritance**
  - `SavingAccount` inherits from `Account`
  - `CurrentAccount` inherits from `Account`
- **Method Overriding**
  - `withdraw()` behaves differently for saving and current accounts
- **Polymorphism**
  - Same method call, different behavior based on account type
- **Multi-file project structure**

---

## 📂 Project Structure

Bank_Management_System/
│
├── account.py # Base Account class
├── saving_account.py # SavingAccount class
├── current_account.py # CurrentAccount class
├── main.py # Menu-driven main program
└── README.md

---

## ⚙️ How to Run the Project

1. Make sure Python is installed (Python 3 recommended)
2. Clone or download this repository
3. Open a terminal in the project folder
4. Run the program:

```bash
python main.py

🧪 Example Operations

Create a Saving or Current account

Deposit money into an account

Withdraw money (with overdraft support for current accounts)

Check balance and view account details

🎯 Learning Outcome

By building this project, I learned:

How to design a real-world system using OOP

How inheritance and polymorphism work in practice

How to structure a Python project using multiple files

How to debug and fix logical errors in a project

🔮 Future Improvements

Add file handling to save and load account data

Add transaction history

Add password/PIN security

Build a GUI version using Tkinter

Connect with a database (advanced)

👨‍💻 Author

Rahul Swain
B.Sc. Computer Science Student
Learning  AI Engineering
