# Rock Paper Scissors ASCII Art

# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random

game_images=[rock, paper, scissors]

choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 0 and choice <= 2:
    print(game_images[choice])
print("Computer choice:\n")
computer_choice=random.randint(0,2)
print(game_images[computer_choice])


if choice < 0 and choice > 2:
    print("You typed an invalid number. You lose!")
elif computer_choice==2 and choice==0:
    print("You win!")
elif choice==2 and computer_choice==0:
    print("You lose!")
elif computer_choice > choice:
    print("You lose!")
elif computer_choice==choice:
    print("It is a draw!")



# #################
# if (choice==0):
#     print(rock)
#     print("Computer choice:\n")
#     if(computer_choice==0):
#         print(rock)
#         print("Repeat")
#     elif(computer_choice==1):
#         print(paper)
#         print("You lose")

#     elif(computer_choice==2):
#         print(scissors)
#         print("You win")
# elif(choice==1):
#     print(paper)
#     if(computer_choice==0):
#         print(rock)
#         print("You win")
#     elif(computer_choice==1):
#         print(paper)
#         print("Repeat")

#     elif(computer_choice==2):
#         print(scissors)
#         print("You lost")
# elif(choice==2):
#     print(scissors)
#     if(computer_choice==0):
#         print(rock)
#         print("You lost")
#     elif(computer_choice==1):
#         print(paper)
#         print("You win")
#     elif(computer_choice==2):
#         print(scissors)
#         print("Repeat")