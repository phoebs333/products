import os # operating system

products = []
if os.path.isfile('products.csv'):
    print('yeah! Found the file!')
    with open ('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if ('name,price') in line:
                continue #skip to the next loop
            name, price = line.strip().split(',')
            products. append ([name, price])
    print (products)

else:
    print('File not found.')


#Read file


# User input
while True: 
	name = input ('Please enter the product name:')
	if name == 'q':
		break
	price = input ('Please enter the price:')
	products.append([name,price])
print(products)

# Print all purchasing record
for p in products:
	print('The price of', p[0], 'is', p[1])

# Write in file
with open ('products.csv', 'w', encoding= 'utf-8') as f:
    f.write('Name, Price\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')