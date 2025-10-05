import random
import re
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#function to set the difficulty
def set_difficulty():
    difficulty = input("Enter your difficulty(easy/hard): ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#function to check the answer
def check_answer(guess, number, turns):
    if guess == number:
        print("Congratulations! You guessed the number!")
        return
    elif guess < number:
        print("Too low!")
        turns = turns - 1
        print(f"You have {turns} attempts left.")
        return turns
    else:
        print("Too high!")
        turns = turns - 1
        print(f"You have {turns} attempts left.")
        return turns
    if turns == 0:
        print("You have lost the game!")
        return
#function to check the guess
def numguess():
    logo = ''' _      _     _      ____  _____ ____    _____ _     _____ ____  ____  _  _      _____   _____ ____  _      _____
/ \  /|/ \ /\/ \__/|/  _ \/  __//  __\  /  __// \ /\/  __// ___\/ ___\/ \/ \  /|/  __/  /  __//  _ \/ \__/|/  __/
| |\ ||| | ||| |\/||| | //|  \  |  \/|  | |  _| | |||  \  |    \|    \| || |\ ||| |  _  | |  _| / \|| |\/|||  \  
| | \||| \_/|| |  ||| |_\\|  /_ |    /  | |_//| \_/||  /_ \___ |\___ || || | \||| |_//  | |_//| |-||| |  |||  /_ 
\_/  \|\____/\_/  \|\____/\____\\_/\_\  \____\\____/\____\\____/\____/\_/\_/  \|\____\  \____\\_/ \|\_/  \|\____\
                                                                                                                 '''
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it.")
    print("Good luck!")
    turns = set_difficulty()
    number = random.randint(1, 100)
    print(number)
    print(f"You have {turns} attempts left.")
    guess = 0
    while guess != number:
        guess = int(input("Enter your guess: "))
        turns = check_answer(guess, number, turns) 
        if turns == 0:
            print("You ran out of attempts! You have lost the game!")
            return

numguess()