#! /usr/bin/python

#10001st prime

import math

number = input("Enter a number: ")

def PrimeOrNot(number):
	isPrime = True
	primes = []
	primesCounter = 0
	while primesCounter < 6:
		for f in range (2, math.trunc(math.sqrt(number))+1):
			if number % f == 0:
				isPrime = False
			else:
				isPrime = True

		if isPrime == True:
			primes.append(number)
			primesCounter += 1

		number += 2

	print primesCounter
	print primes

PrimeOrNot(number)



