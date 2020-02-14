# https://dev.to/thepracticaldev/daily-challenge-184-form-the-minimum-41e7

'''
Given an array of integers, implement a function that will return the lowest possible number that can be formed from these digits.
You cannot use the same number more than once, even if it appears in the array multiple times.
minValue({1, 3, 1}) ==> return 13
minValue({5, 7, 5, 9, 7}) ==> return 579
'''

var = input("Enter the numbers: ")
var = list(set(var))
var.sort()
var = ''.join(var)

print(var)

