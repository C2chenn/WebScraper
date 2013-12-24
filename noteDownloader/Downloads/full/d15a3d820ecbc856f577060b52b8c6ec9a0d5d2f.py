#!/usr/bin/python
#
# File: OnesAndZeros.py
# Author: Keith Schwarz (htiek@cs.stanford.edu)
#
# A program to find a multiple of a natural number n whose digits are just ones
# and zeros.
import sys

# Get the number n
n = int(sys.argv[1]);

# Using the pigeonhole principle, figure out a multiple of n made of just
# zeros and ones.
#
# The trick is to generate the numbers 1, 11, 111, 1111, ..., until we have
# generated n + 1 numbers.  Two of them must have the same remainder modulo
# n, and their difference consists of just 1s and 0s.
#
# This dictionary stores, for each remainder, how many 1s were in the number
# that has that remainder.
remainders = dict()

# A utility function that given a positive number of 1s, returns the
# number with that many 1s.
def countToOnes(c):
	result = 1
	for i in range(1, c):
		result = 10 * result + 1
		
	return result

# ones is the actual number that's a string of ones.  count is how
# many digits it has.
ones = 1
count = 1;

while True:
	# If we know this remainder, we're done.
    if (ones % n in remainders):
    	# Get the actual value and the quotient.
        value = ones - countToOnes(remainders[ones % n])
        quotient = value / n

		# Output that value
        print "One option is " + str(value) + " = " + str(quotient) + " x " + str(n)
        break
    
    # Update that this remainder has been found.
    remainders[ones % n] = count
    ones = 10 * ones + 1
    count = count + 1
