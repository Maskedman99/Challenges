# https://dev.to/thepracticaldev/daily-challenge-198-21-blackjack-31mg

'''
Implement a function that determines the score of a hand in the card game 21 Blackjack.
The function will receive an array filled with strings that represent each card in the hand.
Your function should return the score of the hand as an integer.
Number cards count as their face value (2 through 10). Jack, Queen and King count as 10. An Ace can be counted as either 1 or 11.
Return the highest score of the cards that is less than or equal to 21.
If there is no score less than or equal to 21 return the smallest score more than 21.
	["A"] ==> 11
	["5", "4", "3", "2", "A", "K"] ==> 25
	["A", "J"] ==> 21
	["A", "10", "A"] ==> 12
	["5", "3", "7"] ==> 15
'''

var = input("Enter the string: ")
var = var.split(' ')

sum = 0;
a = 0
for i in var:
	if i == 'K' or i == 'J' or i == 'Q':
		sum += 10
	elif i == 'A':
		a += 1
	else:
		sum += int(i)

if sum + a*11 <= 21:
	sum += a*11
elif sum + a <= 21:
	sum += a
else:
	for i in range(a):
		if sum <= 21:
			sum += 11
		else:
			sum += a-i
			break

print(sum)
