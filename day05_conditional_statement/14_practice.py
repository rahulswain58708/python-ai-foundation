# Take marks as input.
# If marks ≥ 0
# If marks ≤ 100 → print "Valid marks"
# Else → print "Invalid (above 100)"
# Else → print "Invalid (negative)"
marks = float(input("Enter marks:"))
if marks >= 0:
    if marks <= 100:
        print("Valid marks")
    else:
        print("Invalid (above 100)")
else:
    print("Invalid (negative)")