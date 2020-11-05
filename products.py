products = []
while True: 
	name = input ('Please enter the product name:')
	if name == 'q':
		break
	price = input ('Please enter the price:')
	products.append([name,price])
print(products)

for p in products:
	print('The price of', p[0], 'is', p[1])