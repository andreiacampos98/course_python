heigh=int(input("What is your heigh in cm?\n"))

if heigh >= 120:
    print("You can ride the ...")
    age = int(input("How old are you?\n"))
    if age <= 12:
        bill=5
        print("You can ride the ...")
    elif age <= 18:
        bill=7
        print("You can ride the ...")
    elif age >= 45 and age <=55:
        bill=0
    else:
        bill=12
        print("You can ride the ...")
    wants_photo=input("Do you want a photo?\n Type y if yes or n if no.\n")
    if wants_photo =='y':
        bill +=3
    print(f'Your bill is {bill}')
else:
    print("Sorry you have to grow taller before you can ride.")


