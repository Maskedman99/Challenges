# https://dev.to/thepracticaldev/daily-challenge-193-what-s-the-real-floor-3jng

'''
Americans can be weird sometimes. The first floor of a building is typically referred to as the ground floor.
In some American buildings, there is no 13th floor because of old superstitions.
Implement a function that takes an American floor passed as an integer and returns the actual floor number.
Your function should also work for basement floors.
	getRealFloor(1) == 0
	getRealFloor(0) == 0
	getRealFloor(5) == 4
	getRealFloor(15) == 13
	getRealFloor(-3) == -3
'''

var = int(input("Enter the floor number: "))

if var <= 0:
	print(var)
elif var > 13:
	print(var-2)
else:
	print(var-1)

