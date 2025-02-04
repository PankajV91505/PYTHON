age = input("How old are you? ")
age = int(age)
day ="wednesday"

price = 12 if age >= 18 else 8 
 
 
if day == "wednesday":
    price = price-2
    # price -= 2
print(f"Your ticket price is {price}$")
