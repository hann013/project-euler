#! /usr/bin/python

#Largest Prime Factor of 600851475143

def LargestPrimeFactor (number):
	i = 2
	while i < number:
		while number % i == 0:
			number = number / i
		i = i + 1
	print (number)

LargestPrimeFactor(600851475143)
