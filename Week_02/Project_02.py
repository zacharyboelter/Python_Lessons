# Project 2
# Zachary Boelter

# # 1.
# print('Sales Calculating Program \n \n')
# # 2.
# item_description = input('Enter item description: ')
# # 3. 
# item_number = int(input(f'Enter number of {item_description}: '))
# # 4.
# item_price = float(input(f'Enter price per {item_description}: '))
# # 5.
# total_sales = item_number * item_price
# # 6.
# print(f'\n \nYour total order for {item_number} {item_description} is ${total_sales:.2f} at ${item_price} each.')

item_description = input('Enter item description: \n \n')

try:
    item_qty = int(input("Enter the quantity: "))
    item_price = float(input('Enter the price: '))

    total_sales = item_qty * item_price
    print(f'\n \nYour total order for {item_qty} {item_description} is ${total_sales:.2f} at ${item_price}')

except ValueError:
    print('\n[!] ERROR: Please enter numeric values only.')
    print('The program will now exit safely.')

except Exception as e:
    print(f'An unexpected error occurred: {e}')