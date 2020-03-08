# https://dev.to/thepracticaldev/daily-challenge-10-calculator-23n7
'''
Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression.
Remember about the order of operations!
Multiplications and divisions have a higher priority and should be performed left-to-right.
Additions and subtractions have a lower priority and should also be performed left-to-right.
Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
'''

# This also works
'''
var = input("Enter the Operations: ")
print(eval(var))
'''

var = input("Enter the Operations: ")
var = var.split(' ')
var1 = []
var2 = []

a = iter(var)
for i in a:
	if i == '*':
		var1.append(float(var1.pop()) * float(next(a)))
	elif i == '/':
		var1.append(float(var1.pop()) / float(next(a)))
	else:
		var1.append(i)

b = iter(var1)
for i in b:
	if i == '+':
		var2.append(float(var2.pop()) + float(next(b)))
	elif i == '-':
		var2.append(float(var2.pop()) - float(next(b)))
	else:
		var2.append(i)

if len(var2) == 1:
	print(var2[0])
else:
	print('Invalid Expression')
