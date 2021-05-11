
import csv

with open('customers.csv') as csv_file: #OPENS FILE FOR READING
    reader = csv.reader(csv_file, skipinitialspace = True)
    next(reader) #REMOVES THE TOP ROW WHEN IT PRINTS

    for row in reader:
        id = row[0]
        name = row[1]
        address = row[2]
        print(f'Customer: {name}, {address}') #PRINTS CUSTOMER INFO
    print('\n')

product_price = {} #THIS DICTIONARY IS CREATED TO STORE PRICE OF THE PRODUCT
with open('products.csv') as csv_file:
    reader = csv.reader(csv_file, skipinitialspace = True)
    next(reader)

    for row in reader:
        id = row[0]
        product_name = row[1]
        price = int(row[2])
        product_price[id] = price
        print(f'Product: {product_name}, {price}') #PRINTS PRODUCT INFO
    print('\n')

big_dictionary = {} #THIS DICTIONARY IS CREATED TO STORE AMOUNT OF PRODUCT
with open('orders.csv') as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True) #ANOTHER WAY TO MAKE THE CSV FILE READ
                                                             #INSTEAD OF USING ROW NUMBERS, WE USE THE ROWS TITLE
    for row in reader:
        id = row['id']
        customerid = row['customerid']
        productid = row['productid']
        amount = int(row['amount'])


        if productid in big_dictionary:
            big_dictionary[productid] += amount

        if productid not in big_dictionary:
            big_dictionary[productid] = amount

with open('products.csv') as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)
    next(reader)

    for row in reader:
        id = row[0]
        product_name = row[1]
        price = row[2]

        if id in big_dictionary:
            big_dictionary[product_name] = big_dictionary.pop(id)
    for pair in big_dictionary.items(): #LETS BOTH DISTRUBUTION OF SINGLE VARIABLE AND RELATIONSHIP BETWEEN TWO VARIABLES
        print(f'{pair[0]} amount: {pair[1]}') #PRINTS THE NUMBER OF PRODUCT
    print('\n')


with open('products.csv') as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)
    next(reader)

    for row in reader:
        id = row[0]
        product_name = row[1]
        price = int(row[2])
        beta_price = int(big_dictionary.get(row[1]))
        if product_name in big_dictionary:
            big_dictionary[product_name] = beta_price*price

    for pair in big_dictionary.items():
        print(f'{pair[0]} gross income: {pair[1]}') #PRINTS TOTAL AMOUNT OF PRODUCT SOLD
    print('\n')



big_dictionary1 = {} #THIS DICTIONARY IS CREATED TO STORE CUSTOMER ID
with open('orders.csv') as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True)

    for row in reader:
        customerid = row['customerid']
        amount = int(row['amount'])
        productid = row['productid']


        if customerid in big_dictionary1:
            big_dictionary1[customerid] += amount * product_price[productid]

        if customerid not in big_dictionary1:
            big_dictionary1[customerid] = amount * product_price[productid]


with open('customers.csv') as csv_file: #OPENS FILE FOR READING
    reader = csv.reader(csv_file, skipinitialspace = True)
    next(reader) #REMOVES THE TOP ROW WHEN IT PRINTS

    for row in reader:
        id = row[0]
        name = row[1]

        print("{0} money spent: {1}".format(name, big_dictionary1[id])) #ANOTHER WAY TO PRINT ITEM (THE FORMAT WAY)
                                                                        #PRINTS HOW MUCH EACH PERSON SPENT



