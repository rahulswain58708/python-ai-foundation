#Q11 Given two sets:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Find and print:
# Union
print(a.union(b))
# Intersection
print(a.intersection(b))
# Difference (a − b)
print(a.difference(b))
# Symmetric Difference
print(a.symmetric_difference(b))
#Q12.Check whether one set is a subset of another.
print(a.issubset(b)) #subset mean all elements of a present in b
#Q13.Check whether two sets are disjoint.
#disjoin mean no common element
print(a.isdisjoint(b)) #output is False because 3 and 4 are common element. 