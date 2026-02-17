#Zachary Boelter
#Project 3

#1
print('Paycheck Program \n\n')
#2
num_of_employees = int(input('Enter Number of Employees to Process: '))
for i in range(num_of_employees):
    #4
    hours = float(input(f'Enter hours worked for employee {i+1}: '))
    rate = float(input(f'Enter hourly pay rate for employee {i+1}: '))
    #4.3
    if hours <= 40:
        paycheck = hours * rate
    else:
        paycheck = (40 * rate) + ((hours - 40) * (rate * 1.5))
    #4.4
    print(f'Employee worked {hours} hours at ${rate} rate for a gross wage of ${paycheck}')