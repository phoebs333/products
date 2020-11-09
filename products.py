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

with open ('products.csv', 'w', encoding= 'utf-8') as f:
    f.write('Item, Price\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')