#!/usr/bin/env python3

# Created by: Sarah
# Created on: Mar 29, 2022
# This program asks the user to  guess a number. It then generates a
# random number. If the random number is equal to the number guess, you win.
# If not, you lose. 
import random


def main():
    # declare variables
    random_number = random.randint(0, 9)
    # get number guessed from user
    number_guess = int(input("Enter a number between 0 and 9: "))
    print("")

    # check if number_guess is the same as random_number
    if random_number == number_guess:
        print("Your guess is correct!")
    else:
        print("Incorrect, the correct number is: {}".format(random_number))


if __name__ == "__main__":
    main()
