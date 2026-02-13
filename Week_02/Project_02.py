# Project 2
# Zachary Boelter

# 1.Cell
print('Sales Calculating Program \n \n')
# 2.
item_description = input('Enter item description: ')
# 3. 
item_number = int(input(f'Enter number of {item_description}: '))
# 4.
item_price = float(input(f'Enter price per {item_description}: '))
# 5.
total_sales = item_number * item_price
# 6.
print(f'\n \nYour total order for {item_number} {item_description} is ${total_sales} at ${item_price} each.')