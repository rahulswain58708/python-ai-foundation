# Take age as input and print:
# If age ≥ 18
# If age ≥ 60 → "Senior Citizen"
# Else → "Adult"
# Else → "Minor"
age = int(input("Enter a age:"))

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")