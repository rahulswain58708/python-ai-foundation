# 🛡️ Python Exception Handling  
### Part of My AI Engineer Journey 🚀  
**Author:** Rahul Swain  

---

## 📌 About This Repository

This repository contains my structured learning and hands-on practice on **Python Exception Handling**, completed as part of my journey to becoming an AI/ML Engineer.

The goal of this module was not just to learn syntax, but to understand how to write **safe, stable, and production-ready Python code**.

---

## 🎯 Learning Objectives

In this module, I focused on:

- Understanding runtime errors in Python
- Using `try`, `except`, `else`, and `finally`
- Handling specific vs generic exceptions
- Creating and using custom exceptions
- Implementing API-style input validation
- Building a mini project with full exception flow

---

## 📂 Project Structure

Exception_Handling/
│
├── 01_basic_practice.py
├── 02_intermediate_practice.py
├── 03_advance_practice.py
├── safe_calculator.py


---

## 🧠 Concepts Covered

### ✅ Basic Exception Handling
- `try` and `except`
- Handling:
  - `ZeroDivisionError`
  - `ValueError`
  - `IndexError`
  - `FileNotFoundError`

---

### ✅ Intermediate Concepts
- Multiple `except` blocks
- Using `else`
- Using `finally`
- Catching errors with `Exception as e`

---

### ✅ Custom Exceptions
- Creating user-defined exception classes
- Using the `raise` keyword
- Logical validation errors
- Multiple custom exception handling

Example:

```python
class InvalidMarksError(Exception):
    pass


✅ API-Style Validation

Input type validation

Logical condition validation

Defensive programming

Raising meaningful error messages

🧮 Mini Project – Safe Calculator

A production-style calculator that:

Supports operators: + - * / % **

Uses custom exception for invalid operations

Handles:

Invalid number input

Division by zero

Invalid operator

Implements:

try

Multiple except

else

finally

This project demonstrates structured error handling similar to real backend or AI systems.

🧩 Key Takeaways

Exception handling improves system stability.

Validation prevents crashes in real-world applications.

Custom exceptions improve code clarity.

Defensive coding is essential for AI and backend development.

📈 Status

✔ Basic – Completed
✔ Intermediate – Completed
✔ Advanced – Completed
✔ Mini Project – Completed

Exception Handling Module: ✅ Completed

🚀 Next Step in My AI Engineer Journey

NumPy

Data handling

Machine learning fundamentals

Advanced Python concepts

📎 Connect With Me

I am documenting my journey toward becoming an AI Engineer and building impactful technology.

Follow my progress as I continue learning and building.
