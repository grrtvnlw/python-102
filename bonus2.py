# number guessing game
# import random module for randint func
from random import randint

# variables for loop counter, guess, and random number
counter = 0
rand_num = randint(0, 10)

# logic 
while counter < 5:
    guess = int(input("Guess a number between 0 and 10: "))
    if guess == rand_num:
        print("You won! :D")
        break
    else:
        print("Wrong. :(")
    counter += 1

# result    
print("Run the program to play again. :)")