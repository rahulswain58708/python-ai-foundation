#Q17.From a list of numbers, print only those numbers which appear more than once.
nums = [1, 2, 3, 2, 4, 1, 5]
s = set()
for num in nums:
    if nums.count(num) > 1:
        s.add(num)
print(s)
#Q18.Given a list, check if it contains any duplicate.
l = [1,2,3,4]
s = set(l)
if len(l) > len(s):
    print("Duplicate found")
else:
    print("Duplicate Not found")
#Q19.Find students who attended both Day-1 and Day-2 class.
day1 = {"Rahul", "Amit", "Sneha"}
day2 = {"Sneha", "Amit", "Rohit"}
print(f"Both_attend_student = {day1.intersection(day2)}")
#Q20.Find students who attended only one day (either Day-1 or Day-2, but not both).
print(f"attend_only_one_class = {day1.symmetric_difference(day2)}")