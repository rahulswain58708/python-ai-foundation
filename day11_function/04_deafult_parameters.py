#Q26: Create a function greet_user(name="Guest") that prints greeting.
def greet_user(name="Guest"):
    print(f"Hello {name}!")
greet_user()
greet_user("Rahul")
#Q27: Create a function power(base, exponent=2) that returns base raised to exponent.
def power(base,exponent=2):
    return base ** exponent
print(power(5))
print(power(2,3))
#Q28: Create a function discount(price, percent=10) that returns final price after discount.
def discount(price,percent=10):
    discount_amount = (price * percent) / 100
    final_price = price - discount_amount
    return final_price
print(discount(100))
print(discount(150,20))
#Q29: Create a function country_name(name, country="India") that prints name with country.
def country_name(name,country="India"):
    print(f"Name:{name}|Country:{country}")
country_name("Rahul")
country_name("Elon Musk","American")
#Q30: Create a function interest(p, r=5, t=2) that calculates simple interest.
def interest(p, r=5, t=2):
    simple_interest = (p * r * t) / 100
    return simple_interest
print(interest(15))
print(interest(25,8,5))