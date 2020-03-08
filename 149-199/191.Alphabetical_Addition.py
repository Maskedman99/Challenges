# https://dev.to/thepracticaldev/daily-challenge-191-alphabetical-addition-27ki

'''
Write a function that can add letters together. Each letter will be valued based on their position in the alphabet.
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
If no letters are given, the function should return 'z'
	addLetters('a', 'b', 'c') = 'f'
	addLetters('a', 'b') = 'c'
	addLetters('z') = 'z'
	addLetters('z', 'a') = 'a'
	addLetters('y', 'c', 'b') = 'd' // notice the letters overflowing
	addLetters() = 'z'
'''

var = input("Enter input: ")
var = list(var)

def addLetters(var):
	if len(var) == 0:
		return 'z';
	else:
		sum = 0
		for i in var:
			sum += ord(i) - 96

		while sum > ord('z') - 96:
			sum -= ord('z') - 96

		return chr(sum + 96)

print(addLetters(var))
