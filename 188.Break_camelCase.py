# https://dev.to/thepracticaldev/daily-challenge-188-break-camelcase-3ppf

'''
Write a function that will turn a camelCase word into a regular one by adding spaces and lower-casing the words.
	ccbreaker("camelCasing") == "camel casing"
	ccbreaker("garbageTruck") == "garbage truck"
'''

def ccbreaker(a):
	if a.isupper() == True:
		print(' '+a.lower(), end= '')
	else:
		print(a, end='')

var = input("Enter the camelCase: ")
var = list(var)
for i in var:
	ccbreaker(i)
