#Prime Number Finder
#Goal:- User Enter Starting Number And Ending Number Find Prime number Between Starting Number To Ending Number
start_num = int(input("Enter Start Number:-"))
end_num = int(input("Enter End Number:-"))
prime_count = 0
print(f"-------------Prime Numbers Between {start_num} and {end_num}:---------------")
for num in range(start_num,end_num+1):
    if num>1:
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            prime_count += 1
print(f"Total prime numbers found: {prime_count}")

