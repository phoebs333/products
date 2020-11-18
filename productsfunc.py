import os # operating system

#Read file
def read_file(filename):
    products = []
    with open (filename, 'r', encoding='utf-8') as f:
        for line in f:
            if ('name,price') in line:
                continue #skip to the next loop
            name, price = line.strip().split(',')
            products. append ([name, price]) 
    return products  

# User input
def user_input (products):
    while True: 
        name = input ('Please enter the product name:')
        if name == 'q':
            break
        price = input ('Please enter the price:')
        products.append([name,price])
    print(products)

# Print all purchasing record
def print_products(products):
    for p in products:
        print('The price of', p[0], 'is', p[1])

# Write in file
def write_files (filename, products):
    with open ('products.csv', 'w', encoding= 'utf-8') as f:
        f.write('Name, Price\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('yeah! Found the file!')
        products = read_file(filename)       
    else:
        print('File not found.')

    products = user_input(products)
    print_products(products)
    write_files('products.csv', products)

main()
