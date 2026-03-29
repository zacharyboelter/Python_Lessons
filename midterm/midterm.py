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

    if gross >= 200:
        deductions = gross * 0.15
    else:
        deductions = 0.0

    net = gross - deductions

    payroll_data.append([name, hours, rate, gross, deductions, net])

    total_gross += gross
    total_deductions += deductions
    total_net += net

print("\n")
print("Payroll Report")
print("Name\tHours\tRate\tGross\tDeductions\tNet")
print("_" * 60)

for emp in payroll_data:
    print(f"{emp[0]}\t{emp[1]}\t{emp[2]}\t{emp[3]}\t{emp[4]}\t{emp[5]}")

print(f"\nTotal Gross for all employees: {total_gross}")
print(f"Total Deductions for all employees: {total_deductions}")
print(f"Total Net for all employees: {total_net}")