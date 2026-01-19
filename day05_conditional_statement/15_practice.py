# Take total purchase amount as input.
# If amount ≥ 500
# If amount ≥ 1000 → print "20% discount"
# Else → print "10% discount"
# Else → print "No discount"
purchase_amount = int(input("Enter total purchase amount:"))
if purchase_amount >= 500:
    if purchase_amount >= 1000:
        print("20% discount")
    else:
        print("10% discount")
else:
    print("No discount")