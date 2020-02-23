# https://dev.to/thepracticaldev/daily-challenge-7-factorial-decomposition-176o

'''
The aim of this [challenge] is to decompose n!(factorial n) into its prime factors. Prime numbers should be in increasing order.
When the exponent of a prime number is 1, don't print the exponent.
	n = 22; decomp(22) -> "219 * 39 * 54 * 73 * 112 * 13 * 17 * 19"
	n = 25; decomp(25) -> "222 * 310 * 56 * 73 * 112 * 13 * 17 * 19 * 23"
	n = 12; decomp(12) -> "210 * 35 * 52 * 7 * 11"
12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.
'''

import math

var = int(input("Enter the number: "))
fac = math.factorial(var)

def prime(x):
	for i in range(3,x-1,2):
		if x%i == 0:
			return False
	return True

def decomp(x,fac):
	for i in range(fac):
		if fac % x**i != 0:
			return i-1

print('2^' + str(decomp(2,fac)), end='')
for i in range(3,var+1,2):
	if prime(i) == True:
		e = decomp(i,fac)
		if e != 1:
			print(' * ' + str(i) + '^' + str(e), end='')
		else:
			print(' * ' + str(i), end='')
	else:
		continue

print('\n')

