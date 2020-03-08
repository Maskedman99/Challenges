# https://dev.to/thepracticaldev/daily-challenge-189-convert-number-into-reversed-array-2bfi

'''
Write a function that takes a random number as input and converts it into an array with the digits of that number appearing in reverse order.
	convertNtA(348597) => [7,9,5,8,4,3]
'''

var = input("Enter the number: ")
var = list(var)
for i in range(len(var)):
	var[i] = int(var[i])
print(var[::-1])
