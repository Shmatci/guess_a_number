# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:38:42 2021

@author: tamar
"""

import random as rnd



def pick_random_num():
    """pick a random number -
    using a function, computer picks a random number and stores it in a variable to later
    compare with players guessed number."""
    upper_bound = greeting()
    return rnd.randint(1, upper_bound)
    


def take_a_guess():
    """take an int input from user - 
    ask user to put some random int input that you are going to use
    forward, put it in a variable"""
    while True:
        try:
            user_guess = int(input("Please enter your guess: "))
            assert user_guess >=1
            break
        except ValueError:
            print('Whoops!\nThat is not an integer!.Please enter an integer.')
        except AssertionError:
            print("Whoops!\n  You entered a number smaller than 1. Please enter an integer greater than 1!")
        
    return user_guess


def level_difficulty(level):
    hard = 100
    medium = 50
    easy = 20
    if level.lower() == "h":
        upper_bound = hard
    elif level.lower() == "m":
        upper_bound = medium
    else:
        upper_bound = easy
    return upper_bound
    
def greeting():
    print("Hi! You are going to try to guess a number I come up with!")
    print("Choose difficulty level:")
    level = input("Enter h for hard, m for medium or e for easy:")
    upper_bound = level_difficulty(level)
    print(f"I am thinking of a number between 1 and {upper_bound}")
    
    return upper_bound
    
    
    
def play_game():
    """if guessed number is not same as random number, guess again and 
    check until you find solution."""  
     
    
    global guesses
    # Greet user
    guess = take_a_guess()
    # Keep track of guesses
    guesses = guesses + 1
    
    # Provide feedback   
    if guess == random_num:
        print("Congrats, you found the number! \n",
              f"The number of guesses you needed was {guesses}.")            
        return None
    elif guess > random_num:
        print("Your guess is too high, guess again.")
        return play_game()
    else:
        print("Your guess is too low, guess again.")
        return play_game()
    
# Start
guesses = 0
random_num = pick_random_num()
# print("*** this is the number you are looking for: (",random_num,") ***")
play_game()


while True:
    print("Would you like to play again?")
    play_again = input("Enter y for yes or n for no: ")
    if play_again.lower() == "y":
        guesses = 0
        random_num = pick_random_num()
        play_game()
    else:
        print("Thank you for playing!")
        break
 

 




