import random
from wordlist import word_list
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def has_won(word_to_guess, word_done):
    word_done_as_string = ''.join(word_done)
    if word_done_as_string == word_to_guess:
        print("You won")
        return True
    else:
        return False

def has_die(nb_times_die):
    if nb_times_die > 5:
        print("You lose! Try again")
        return True
    return False


def init():
    word_to_guess=word_list[random.randint(0,len(word_list) - 1)]

    lose=0
    i=0
    string=[]
    while i < len(word_to_guess):
        string.append("_")
        i=i+1

    while not has_won(word_to_guess, string):
        word_done_as_string = ''.join(string)
        print("Word to guess: ", word_done_as_string)
        Letter=input("Guess a letter: ").lower()

        if Letter not in word_to_guess:
            lose += 1
        
        i=0
        while i < len(word_to_guess):
            if Letter==word_to_guess[i]:
                string[i]=word_to_guess[i]
            i=i+1
        print(HANGMANPICS[lose])
        if has_die(lose):
                return 
init()