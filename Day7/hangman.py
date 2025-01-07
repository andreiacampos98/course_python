import random
word_list=['andreia', 'car', 'game', 'spoon', 'electric']

def has_won(word_to_guess, word_done):
    if str(word_done) == word_to_guess:
        print("You won")
        return True
    else:
        print("continue")
        return False


#I can use random.choice(word_list)
word_to_guess=word_list[random.randint(0,len(word_list) - 1)]

print(word_to_guess)
print("Word to guess: ")
i=0
string=[]
while i < len(word_to_guess):
    string.append("_")
    i=i+1
print(string)

while not has_won(word_to_guess, string):
    Letter=input("Guess a letter: ").lower()

    #for letter in word_to_guess:

    i=0
    while i < len(word_to_guess):
        if Letter==word_to_guess[i]:
            print("Right")
            string[i]=word_to_guess[i]
        else:
            print("Wrong")
        i=i+1

    print(string)
    
# if Letter in word_to_guess:
#     print("Yes!")