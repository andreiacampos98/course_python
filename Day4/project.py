print("Welcome to Treasure island.\nYour mission is to find the treasure.")
direction=input("Do you want to go to Left or Right?")
if(direction == 'left'):
    way=input("Do you want to swim or wait?").lower()
    if (way == 'wait'):
        door=input("Which door do you prefer: red, yellow or blue").lower()
        if(door=='yellow'):
            print("You win!")
        print("Game Over")
    print("Game Over")
print("Game Over")