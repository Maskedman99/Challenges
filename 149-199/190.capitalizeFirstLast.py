# https://dev.to/thepracticaldev/daily-challenge-190-capitalizefirstlast-58jf

'''
For this challenge, you will have to write a function called capitalizeFirstLast or capitalize_first_last.
This function will capitalize the first and last letter of each word, and lowercase what is in between.
	capitalizeFirstLast "and still i rise"               -- "AnD StilL I RisE"
	capitalizeFirstLast "when words fail music speaks"   -- "WheN WordS FaiL MusiC SpeakS"
	capitalizeFirstLast "WHAT WE THINK WE BECOME"        -- "WhaT WE ThinK WE BecomE"
	capitalizeFirstLast "dIe wITh mEMORIEs nOt dREAMs"   -- "DiE WitH MemorieS NoT DreamS"
	capitalizeFirstLast "hello"                          -- "HellO"
'''

var = input("Enter the String: ")

def capitalizeFirstLast(x):
	x = x.lower()
	x = list(x)
	x[0] = x[0].upper()
	x[len(x)-1] = x[len(x)-1].upper()

	for i in range(len(x)):
		if x[i] == ' ':
			x[i-1] = x[i-1].upper()
			x[i+1] = x[i+1].upper()

	return(''.join(x))

print(capitalizeFirstLast(var))
