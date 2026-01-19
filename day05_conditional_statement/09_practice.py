# Take marks as input and print grade:
# ≥ 90 → A
# ≥ 70 → B
# ≥ 40 → C
# else → Fail
marks = float(input("Enter marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")