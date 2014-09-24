#! /usr/bin/python

#Largest Palindrome Product of Two 3-digit Numbers

num1 = 100
num2 = 100
tempNum = ""
biggestPalinProduct = 100000

while num1 < 1000: 
	if num1*num2 >= biggestPalinProduct:
		tempNum = str(num1*num2)
		if tempNum[0:] == tempNum[::-1]:
			biggestPalinProduct = num1*num2

	if num2 == 999:
		num1 +=1
		num2 = 100
	else:
		num2 += 1

print "Biggest palindrome number: ", biggestPalinProduct
