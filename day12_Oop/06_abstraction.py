# Create a program that demonstrates Abstraction using an abstract base class.
# 📌 Requirements:
# Create an abstract class named Payment
# Abstract method: pay(amount)
# Create two child classes:
# CreditCard
# UPI
# Each child class must:
# Implement pay(amount)
# Print:
# "Paid <amount> using Credit Card"
# "Paid <amount> using UPI"
# Create objects of both child classes.
# Call pay(500) for CreditCard
# Call pay(300) for UPI
# ❌ Do NOT create object of Payment
from abc import ABC,abstractmethod
class Payment(ABC):
    def pay(self,amount):
        pass
class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")
class Upi(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Upi")
c = CreditCard()
u = Upi()
c.pay(450)
u.pay(999)
