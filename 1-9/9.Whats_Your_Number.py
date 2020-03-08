# https://dev.to/thepracticaldev/daily-challenge-9-what-s-your-number-3707

'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
'''

var = input("Enter 10 integers: ")
var = list(var)

if len(var) != 10:
	print("Invalid Entry")
else:
	print('(',var[0],var[1],var[2],') ',var[3],var[4],var[5],'-',var[6],var[7],var[8],var[9], sep='')
