#Midterm Assignment
#Zachary Boelter

num_employees = int(input("Enter the number of employees: "))

payroll_data = []
total_gross = 0.0
total_deductions = 0.0
total_net = 0.0

for i in range(num_employees):
    name = input("\nEnter the employee's name: ")
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))

    if hours > 40:
        overtime_hours = hours - 40
        gross = (40 * rate) + (overtime_hours * (rate * 1.5))
    else:
        gross = hours * rate