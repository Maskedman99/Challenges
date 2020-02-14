# https://dev.to/thepracticaldev/daily-challenge-185-house-numbers-sum-252p

'''
A boy is walking home from school.
To make the walk more enjoyable, he decides to add up the numbers of the houses he passes during his walk.
Unfortunately, the numbers won't appear to him in any specific order, since he's regularly taking turns.
At some point during the walk, the boy encounters a house marked number 0.
This surprises him so much that he stops adding the numbers after that house to the total.
For the given array of house numbers, determine the sum that the boy will get.
There will always be at least one number 0 house on the path.
inputArray = [5, 1, 2, 3, 0, 1, 5, 0, 2] => 11
inputArray = [1, 4, 34, 124, 2, 0, 14, 51] => 165
'''

var = input("Enter elements seperated with space: ")
var = var.split('0')
var = var[0]
var = var.split(' ')
var = var[:-1]
sum = 0
for i in range(len(var)):
	sum += int(var[i])

print(sum)
