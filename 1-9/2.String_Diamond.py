# https://dev.to/thepracticaldev/daily-challenge-2-string-diamond-21n2

'''
Your task is to return a string that displays a diamond shape on the screen using asterisk (“*”) characters.
The shape that the print method will return should resemble a diamond.
A number provided as input will represent the number of asterisks printed on the middle line.
The line above and below will be centered and will have two less asterisks than the middle line. 
This reduction will continue for each line until a line with a single asterisk is printed at the top and bottom of the figure.
Return null if input is an even number or a negative number.
Note: JS and Python students must implement diamond() method and return None (Py) or null(JS) for invalid input.
'''

def diamond(var):
	if var%2 == 0 or var < 0:
		return None
	else:
		for i in range(1,var, 2):
			for j in range(int((var-i)/2)):
                                print(' ',end='')
			for j in range(i):
				print('*',end='')
			print('\n')
		for i in range(var, 0, -2):
			for j in range(int((var-i)/2)):
				print(' ',end='')
			for j in range(i):
				print('*',end='')
			print('\n')

var = input("Enter the number: ")
diamond(int(var))
