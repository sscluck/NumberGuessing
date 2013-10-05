from random import *
import unittest

class MyTest(unittest.TestCase):
	def test_guess(self):
		return None

def getInt(prompt):
	# Given: a string as a prompt for the user
	# Returns: the integer inputted by user
	# 	Prompts the user to re-enter input if non-integer
	isInteger = False

	# Keep prompting user until input is int
	while (not isInteger):
		input_str = raw_input(prompt)

		try:
			input_num = int(input_str)
			isInteger = True
		except:
			print 'Please enter an integer.'

	return input_num

def setBounds():
	# Prompts user for bounds
	# Returns bounds as tuple: (lower_bound, upper_bound)

	isValid = False

	while (not isValid):
		lower_bound = getInt('Enter a lower bound:')
		upper_bound = getInt('Enter an upper bound:')

		if (lower_bound <= upper_bound)
			isValid = True

		else
			print 'Invalid bounds'

	return (lower_bound, upper_bound)

def playGame(lower_bound, upper_bound):
	# Given: range for guesses
	# Generate random number and prompts the user through guesses until guess is
	# 	random number

	number = randint(lower_bound, upper_bound)
	guess = number+1

	tries = 0
	while (guess != number):
		guess = getInt('Enter your guess:')
		
		if (guess < lower_bound) or (guess > upper_bound):
			print 'Out of bounds :('
			continue

		if (guess > number):
			print 'Go lower'

		elif (guess < number):
			print 'Go higher'


		tries += 1

	assert(guess == number)

	print 'Yay! It took you ', tries, ' tries to guess the number.'



