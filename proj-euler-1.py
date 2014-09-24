#! /usr/bin/python

#Multiples of 3 and 5

multiplesSum = 0

for i in range (1000):
	if i % 3 == 0 or i % 5 == 0:
		multiplesSum += i
print multiplesSum