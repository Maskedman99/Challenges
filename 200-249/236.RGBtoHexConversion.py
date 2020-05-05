# https://dev.to/thepracticaldev/daily-challenge-236-rgb-to-hex-conversion-2iep

'''
This rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.
The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

Tests:
rgb(-20,275,125)
rgb(255,255,255)
'''
r = int(input("R: "))
g = int(input("G: "))
b = int(input("B: "))

def toHex(var):
	if var < 0:
		var = 0
	if var > 255:
		var = 255

	return hex(var).split('x')[-1].zfill(2)

def rgb(r, g, b):
	return(toHex(r)+toHex(g)+toHex(b))

print(rgb(r, g, b))
