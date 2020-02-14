# https://dev.to/thepracticaldev/daily-challenge-3-vowel-counter-34ni

'''
Write a function that returns the number (count) of vowels in a given string.
Letters considered as vowels are: a, i, e, o, and u.
The function should be able to take all types of characters as input, including lower case letters, upper case letters, symbols, and numbers.
'''

def vowel(var):
	if var in 'aeiouAEIOU' :
		return 1
	return 0

var = input("Enter the string: ")
var = list(var)
c = 0;

for i in range(len(var)):
	c += vowel(var[i])
print(c)

