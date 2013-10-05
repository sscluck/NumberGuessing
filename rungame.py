# Authors: Sally, Stephanie
# Script that runs a number guessing game
#
# Asks the user to enter a lower and upper bound, then prompts the user
# to enter a series of guesses, helping them along they way by telling
# them to guess higher or lower, terminating when they have guessed
# the number and returns the number of tries it took them.

from workshop import *

# Ask the user for the range
(lower_bound, upper_bound) = setBounds()

# Run the game
playGame(lower_bound, upper_bound)