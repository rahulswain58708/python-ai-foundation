# Take username and password as input.
# If username is "admin"
# If password is "1234" → print "Login successful"
# Else → print "Wrong password"
# Else → print "Invalid username"
username = input("Enter username:")
password = input("Enter Password:")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid username")