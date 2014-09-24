#! /usr/bin/python

#Sum Square Difference

sumSquares = 0
squareOfSum = 0
difference = 0

for i in xrange(1, 101):
	sumSquares += i**2

for i in xrange(1, 101):
	squareOfSum += i
squareOfSum = squareOfSum**2

difference = squareOfSum - sumSquares

print "Sum of Squares = ", sumSquares
print "Square of Sum = ", squareOfSum
print "Difference = ", difference