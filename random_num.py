"""
Write a Python 3 program that randomly selects a number from 1-100, and then prompts the user for guesses. After each incorrect guess, the program helps the user by directing them to guess higher or lower. When the user guesses the correct number, the program will display the number of guesses the user made and ask them if they would like to play again.
"""
import random
from random import randint

num = randint(1, 100)

print("Welcome to the number guessing game!")
seed_val = input("Enter random seed: ")
random.seed(seed_val)

def guess():
    global num
    while True:
        num_guess = int(input("Please enter a guess: "))
        if (num_guess < num):
            print("higher")
        elif(num_guess > num):
            print("lower")
        else:
            print("Congratulations. You guessed it!")
            ask = input("Would you like to play again (yes/no)? ")
            if (ask == "yes"):
                num = randint(1, 100)
                guess()
            else:
                return 
guess()

    

