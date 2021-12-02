# CTI - 110
# P3HW2 - Salary
# Anthony Davis
# 14 Oct 2021

# Asks the user to name of employee
# Ask user to enter number of hours the employee worked this month
# Ask user to enter employee's pay rate
# Evaluate if employee has worked overtime. If yes calcuate amount owed to employee for overtime hours
# Calculate amount employee shoud be paid for regular hours worked.
# Display gross pay (total amount that should be paid to employee)
# The program is to display the following ( Employee name, pay rate,
# number of hours worked, overtime hours, overtime pay , pay for regular hours and gross pay).

name = input("Please enter employee's name: ")
hours_worked = float(input('Please enter hours worked this week: '))
pay_rate = float(input("Please enter employee's pay rate: "))
print ('------------------------------------------')

if (hours_worked > 40) and (hours_worked < 80):
    reg_pay = (hours_worked - hours_worked % 40) * pay_rate # Total code for regular pay
elif hours_worked >= 80:
    reg_pay = (hours_worked - hours_worked % 40 - 40) * pay_rate
else:
    reg_pay = hours_worked * pay_rate

over_time_rate = pay_rate * 1.5 # Time and a half pay

if hours_worked <= 40: # Formula for over time hours.
    over_time = 0
elif (hours_worked > 40) and (hours_worked < 80):
    over_time = hours_worked % 40
else:
    over_time = hours_worked - 40

over_time_pay = over_time * over_time_rate # Over time pay
gross_pay = reg_pay + over_time_pay # Total pay


print ('Employee Name: ', name)
print ('------------------------------------------')
print ('Hours Worked: '+str(format (hours_worked, '.2f')))
print ('------------------------------------------')
print ('Pay Rate: $'+str(format (pay_rate, '.2f')))
print ('------------------------------------------')
print ('Over Time: '+str(format (over_time, '.2f')))
print ('------------------------------------------')
print ('Over Time Pay: $'+str(format (over_time_pay, '.2f')))
print ('------------------------------------------')
print ('Regular Hour Pay: $'+str(format (reg_pay, '.2f')))
print ('------------------------------------------')
print ('Gross Pay: $'+str(format (gross_pay, '.2f')))
print ('------------------------------------------')
