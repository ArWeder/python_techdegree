#
#  Number Guessing Game
#  Python Techdegree
#
#  Created by Dulio Denis on 2/7/17.
#  Copyright (c) 2017 ddApps. All rights reserved.
# ------------------------------------------------
#  Guess what number the computer picked.
#  The computer tells you if your guess is too low or high.
# ------------------------------------------------
# v1: basic functionality
import random
# generate a random number between 1 and 10
secret_num = random.randint(1, 10)

# set up the game loop
while True:
    # get a number guess from the player
    guess = int(input("Guess a number between 1 and 10: "))

    # compare guess to the secret number
    if guess == secret_num:
        print("You got it! My number was {}".format(secret_num))
        break
    else:
        print("Try again.")
        # print hit or miss
