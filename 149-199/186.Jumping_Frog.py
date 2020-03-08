# https://dev.to/thepracticaldev/daily-challenge-186-jumping-frog-2fdg

'''
There is a lonely frog that lives in a pond.
Lily-pads are laid out on a coordinate axis atop the pond.
The frog can only jump one unit more than the length of the last jump.
With a starting point of 0, reach the target point of n using the frog's jumping ability.
You can choose to jump forward to backward.
Reach the target with the minimal amount of steps.
	For n = 2, the output should be 3
		step 1:  0 ->  1  (Jump forward, distance 1)
		step 2:  1 -> -1  (Jump backward, distance 2)
		step 3: -1 ->  2  (Jump forward, distance 3)
	For n = 6, the output should be 3.
		step 1: 0 -> 1  (Jump forward, distance 1)
		step 2: 1 -> 3  (Jump forward, distance 2)
		step 3: 3 -> 6  (Jump forward, distance 3)
'''

var = int(input("Enter the number: "))

for i in range(var+2):
	if i*(i+1)/2 > var:
		break

print(int( (var - i*(i-1)/2)*2 + (i-1) ))
