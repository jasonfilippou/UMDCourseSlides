from sys import argv
import time

# Constants
DEFAULT_TERMS = 10000000  # One million squared
DEFAULT_DIFF = 8
EXIT_FAILURE = -1
EXIT_SUCCESS = 0
BOTTOM_END = 4

"""
A simple script that searches for the differences between the units 
and tenths digits of all squares of integers between BOTTOM_END and 
BOTTOM_END + DEFAULT_TERMS - 1.
"""


def main():
	try:
		# Parse command line arguments. If none, go to default constants (1,000,000, 8)
		terms = int(argv[1]) if len(argv) > 1 else DEFAULT_TERMS 
		desired_diff = int(argv[2]) if len(argv) > 2 else DEFAULT_DIFF
	except ValueError as ve:  # If there are any errors, report them to the output.
		print("We received a :" + str(ve))
		return EXIT_FAILURE
	if terms <= 3:
		print("Provided number of terms={:d}. We need a number equal to at least 4.".format(terms))
		return EXIT_FAILURE
	if (desired_diff < 0) or (desired_diff > 9):
		print("We need a difference between 0 and 9 inclusive.")
		return EXIT_FAILURE

	for i in range(BOTTOM_END, terms):  # For all perfect squares from BOTTOM_END ^ 2 all the way to (terms)^2...

		square = i**2

		units = square % 10 			# Mod 10 (% 10) gives us the last digit of any given integer

		tens = (square // 10) % 10  	# n Div 10 (n // 10) gives us the floor division of n by 10 (e.g 256 // 10) = 25.
										# Then, do a mod 10 again to get the final digit, which is the original tenths digit.

		if abs(units - tens) == desired_diff:
			print('SUCCESS: square={:d}, units={:d}, tens={:d}'.format(i**2, units, tens))
			return EXIT_SUCCESS
		else:
			print('FAILURE: square={:d}, units={:d}, tens={:d}'.format(i ** 2, units, tens))

		# time.sleep(0.5) 	# Wait a bit for the output to be readable.

	# end for...

	print("Did not find any such perfect squares!")
	return EXIT_FAILURE


if __name__ == "__main__":
	main()
