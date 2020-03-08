# https://dev.to/thepracticaldev/daily-challenge-194-spread-number-cdm

'''
Implement a function that will create an array and fill it with numbers ranging from 1 to n.
The numbers will always be positive.
	spreadNumber(1) => [1]
	spreadNumber(2) => [1, 2]
	spreadNumber(5) => [1, 2, 3, 4, 5]
'''

var = int(input("Enter the number: "))
l = list(range(1,var+1))
print(l)
