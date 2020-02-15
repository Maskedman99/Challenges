# https://dev.to/thepracticaldev/daily-challenge-187-most-sales-1a10

'''
You work in the best consumer electronics company around.
Your boss asked you to find out which products generate the most revenue.
You'll be given lists of products, amounts, and prices.
Given these three lists of same length, return the product name(s) with the highest revenue (amount * price).
If multiple products have the same revenue, order them according to their original positions.
	products: ["Computer", "Cell Phones", "Vacuum Cleaner"]
	amounts: [3, 24, 8]
	prices: [199, 299, 399]

	return: Cell Phones
'''

products = input("Enter the product names: ")
products = products.split(' ')
amounts = input("Enter the amounts: ")
amounts = amounts.split(' ')
prices = input("Enter the prices: ")
prices = prices.split(' ')

for i in range(len(prices)):
	prices[i] = int(amounts[i])*int(prices[i])

j = max(prices)

for i in range(len(prices)):
	if prices[i] == j:
		print(products[i])

