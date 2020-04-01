# number guessing game
# import random module for randint func
from random import randint

# variables for loop counter, guess, and random number
counter = 0
guess = ''
randNum = randint(1, 10)

#logic 
while counter < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == randNum:
        print("You won!")
        break
    if guess != randNum:
        print("Wrong.")
    counter += 1
print("Run the program to play again")