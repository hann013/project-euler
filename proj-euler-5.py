#! /usr/bin/python

#Smallest Multiple Evenly Divisible by Numbers 1-20

i = 11
number = 2520

while i <= 20:
	if number % i == 0:
		i += 1
	else:
		i = 11
		number += 2520

print number

# i = 11
# number = 20

# while i <= 20:
# 	if number % i == 0:
# 		i += 1
# 	else:
# 		i = 11
# 		number += 20

# print number
