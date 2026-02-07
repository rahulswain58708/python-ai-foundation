# Encapsulation is the process of protecting data inside a class.
# We cannot access class properties directly.
# We use getter and setter methods to access and modify the data.

# Task: Create a class UserAccount that follows Encapsulation.
# Requirements:
# Create a private variable __password
# Create a setter method set_password(password)
# It should store the password
# Create a getter method get_password()
# It should return the password
# Create an object and:
# Set the password using setter
# Print the password using getter
# Do NOT access __password directly

class UserAccount:
    def set_password(self,password):
        self.__password = password
    def get_password(self):
        return self.__password
user1 = UserAccount()
user1.set_password("Rahul@2580")
print("Password =",user1.get_password())

# Task:
# Create a class Employee that follows Encapsulation.
# Requirements:
# Create a private variable __salary
# Create a setter method set_salary(amount)
# Store the salary
# Create a getter method get_salary()
# Return the salary
# Create an object of Employee
# Set salary using setter
# Print salary using getter
# ❌ Do NOT access __salary directly

class Employee:
    def set_salary(self,amount):
        self.__salary = amount
    def get_salary(self):
        return self.__salary
e1 = Employee()
e1.set_salary(5000)
print(e1.get_salary())
