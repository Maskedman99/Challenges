# https://dev.to/thepracticaldev/daily-challenge-195-no-zeroes-for-heroes-2mm4

'''
It has officially been decided that numbers that end with zeroes are boring.
They might be fun in your world, but definitely not here.
Implement a function to eradicate any trailing zeroes.
If the given number is 0, just leave him alone. Poor guy anyway.

	1450 -> 145
	960000 -> 96
	1050 -> 105
	-1050 -> -105
'''

var = int(input("Enter the number: "))

while var != 0:
	if var%10 == 0:
		var = var/10
	else:
		break
print(int(var))


