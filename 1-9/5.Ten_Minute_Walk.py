# https://dev.to/thepracticaldev/daily-challenge-5-ten-minute-walk-1188

'''
You live in a city where all roads are laid out in a perfect grid.
You have the unfortunate habit of arriving too early or too late to your appointments, so you decide to create a Walk Generating App.
Any time you press the button, it will send you an array of one-letter strings representing directions to walk (eg. [‘n’,’s’,’w’,’e’]).
You always walk only a single block in a direction.
It takes one minute to traverse one city block.
Create a program that will return an array of one-letter strings representing the walk.
The program should accept input for the amount of time the user decides to walk and should bring the user back to their starting location.
'''

var = int(input("Enter the time: "))
if var%2 != 0:
	print("Not Possible")
else:
	print('ns'*int((var/2)))

