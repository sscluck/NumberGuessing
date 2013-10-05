"""
The MIT License (MIT)

Copyright (c) 2013 Sally and Stephanie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# Authors: Sally, Stephanie
# Version 0

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

	isGuessed = False

	tries = 0
	while (not isGuessed):
		guess = getInt('Enter your guess:')
		
		if (guess < lower_bound) or (guess > upper_bound):
			print 'Out of bounds :('
			continue

		if (guess > number):
			print 'Go lower'

		elif (guess < number):
			print 'Go higher'

		else:
			isGuessed = True


		tries += 1

	assert(guess == number)

	print 'Yay! It took you ', tries, ' tries to guess the number.'



