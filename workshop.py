from random import *

isInteger = False

while (not isInteger):
	lower_bound_str = raw_input('Enter lower bound:')
	upper_bound_str = raw_input('Enter upper bound:')

	try:
		lower_bound = int(lower_bound_str)
		upper_bound = int(upper_bound_str)
		isInteger = True
	except:
		print 'Please enter an integer.'



number = randint(lower_bound, upper_bound)
guess = number+1


tries = 0
while (guess != number):
	isInteger = False

	while (not isInteger):
		guess_str = raw_input('Enter your guess:')

		try:
			guess = int(guess_str)
			isInteger = True
		except:
			print 'Please enter an integer.'

	if (guess < lower_bound) or (guess > upper_bound):
		print 'Out of bounds :('
		continue

	if (guess > number):
		print 'Go lower'

	elif (guess < number):
		print 'Go higher'


	tries += 1

print 'Yay! It took you ', tries, ' tries to guess the number.'



