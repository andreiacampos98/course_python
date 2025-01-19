print("Welcome to Python Pizza Deliveries")
size=input("What size pizza do you want? s, m or l\n")
pepperoni=input("Do you want pepperoni on your pizza? y or n\n")
extra_cheese=input("DO you want extra cheese? y or n\n")

if size == "s":
    price=15
    if pepperoni=="y":
        price +=2
elif size== "m":
    price=20
    if pepperoni=="y":
        price +=3
elif size=="l":
    price=25
    if pepperoni=="y":
        price +=3
else:
     print("You type a size that doesn't exist")

if extra_cheese=="y":
        price +=1

print(f'The price is {price}')