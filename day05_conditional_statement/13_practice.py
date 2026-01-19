# Take age and country as input.
# If age ≥ 18
# If country is "India" → print "Eligible"
# Else → print "Not eligible (country)"
# Else → print "Underage"
age = int(input("Enter a age:"))
country = input("Enter your country:").lower()
if age >= 18:
    if country == "india":
        print("Eligible")
    else:
        print("Not eligible")
else:
    print("Underage")