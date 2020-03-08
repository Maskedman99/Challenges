# https://dev.to/thepracticaldev/daily-challenge-1-string-peeler-4nep

'''
Your goal is to create a function that removes the first and last letters of a string.
Strings with two characters or less are considered invalid.
You can choose to have your function return null or simply ignore.
'''

var = input("Enter the String: ")
print(var[1:-1])


# This also works
'''
var = list(var)
var.pop()
var.pop(0)
var = ''.join(var)
print(var)
'''
