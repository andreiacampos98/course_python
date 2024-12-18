print("Welcome to the tip calculator!")

total = float(input("What was the total bill?\n"))

tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
nb_persons = int(input("How many people to split the bill?\n"))
value_to_pay = round((total *(1 + tip/100)) / nb_persons, 2)
print(f"Each person should pay: ${value_to_pay}")