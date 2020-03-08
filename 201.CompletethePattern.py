# https://dev.to/thepracticaldev/daily-challenge-201-complete-the-pattern-13nb

'''
Implement a function pattern, which returns the following pattern for up to n number of rows.
If n < 1 then it should return " " i.e. empty string. There are no whitespaces in the pattern.

	Pattern:
	1
	22
	333
	....
	.....
	nnnnnn

	pattern(5):
	1
	22
	333
	4444
	55555

	pattern(11):
	1
	22
	333
	4444
	55555
	666666
	7777777
	88888888
	999999999
	10101010101010101010
	1111111111111111111111

	pattern(4)
	pattern(8)
	pattern(0.5)
'''

var = float(input("Enter the number: "))

def pattern(var):
	if var < 1:
		print("")
	else:
		var = int(var)
		for i in range(var+1):
			for j in range(i):
				print(i,end = '')
			print('\n',end='')

pattern(var)
