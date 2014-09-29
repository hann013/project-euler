#! /usr/bin/python
#10001st prime

import math

counter = 1
isPrime = False
primesList = [2]
number = 3

while counter < 10001:
    for prime in primesList:
        if number % prime == 0:
            isPrime = False
            break
        else:
            isPrime = True

    if isPrime == True:
        primesList.append(number)
        counter += 1
        isPrime = False

    number += 1

print counter
print number-1

    #[check if number is prime by dividing by all prime factors before number]
    #[if number is prime, add number to primesList, counter += 1]
    #number += 1



