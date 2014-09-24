#! /usr/bin/python

#Even Fibonacci numbers

prev1 = 1
prev2 = 1
newTerm = 0
FibonacciSum = 0

while newTerm < 4000000:
	newTerm = prev1 + prev2
		
	if newTerm % 2 == 0:
		FibonacciSum += newTerm 

	prev1 = prev2
	prev2 = newTerm

print FibonacciSum
