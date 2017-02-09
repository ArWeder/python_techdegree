#
#  Hangman
#  Python Techdegree
#
#  Created by Dulio Denis on 2/9/17.
#  Copyright (c) 2017 ddApps. All rights reserved.
# ------------------------------------------------
#  Guess what word the computer picked.
#
import random

# make a list of words
words = [
#    'apple',
#    'banana',
    'orange',
#    'coconut',
#    'strawberry',
    'lime',
#    'grapefruit',
    'lemon',
#    'kumquat',
#    'pineapple',
#    'blueberry',
    'melon'
]

# set-up the game loop:
while True:
    # Allow ending early
    start = input("Press enter/return to start, or enter Q to quit: ")
    if start.lower() == 'q':
        break

    # pick a random word
    secret_word = random.choice(words)

    # have both a good and bad guess letter list
    bad_guesses = []
    good_guesses = []

    # limit the number of guesses to 7
    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        # draw guessed letters, spaces and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print('') # print a blank line to act as a carriage return
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('') # another blank line just for formatting

        # take a guess and lowercase it right away
        guess = input("Guess a letter: ").lower()

        # validate its a legitimate guess
        if (len(guess)) != 1:
            print("You can only guess a single letter")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter.")
            continue
        elif not guess.isalpha():
            print("You can only guess letters.")
            continue

        # determine whether it was a good or bad guess
        if guess in secret_word:
            good_guesses.append(guess)
            # print out win
            print("Checking win: len(good_guesses = {})".format(len(good_guesses)))

            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        # print out loss
        print("You didn't guess it. My secret word was {}".format(secret_word))
