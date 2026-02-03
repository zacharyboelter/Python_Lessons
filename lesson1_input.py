# First exercise
try: 
    print('Welcome to your first Python tutor session, Zack!')
    data = input('Enter three numbers separated by spaces: ')
    num1, num2, num3 = [float(x) for x in data.split()]

    print(f'Number 1: {num1}')
    print(f'Number 2: {num2}')
    print(f'Number 3: {num3}')
    print(f'Total: {num1 + num2 + num3}')
except ValueError:
    print('Oops! Please make sure to enter three valid numbers separated by spaces. Try again.')