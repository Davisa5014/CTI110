# CTI - 110
# P4HW2 - Salary
# Anthony Davis
# 8 Nov 2021

# Asks the user employee name
# If user pay rate and hours worked
# Calculate overpay and regPay. Store these values in variables
# at the end of the program you will display overtime total , regular pay total ,gross pay total and number of employees entered
# Ask user to enter another employee's name to calculate salary for or "None" to terminate program. Note we are using sentinals here.
# THE PROGRAM ONLY TERMINATES IF THE USERS "None" for employee name.



def main():

    repeat = True # Flag for repeating loop
    employees = 0 # Variables
    totalOvertime = 0
    totalReghours = 0
    totalGrosspays = 0
    name = ()
    pay_rate = 0
    
    while repeat == True:

        name = input("Please enter employee's name or 'None' to terminate: ")
        if name != "None": # sentinel

            employees = employees + 1
            
            hours_worked = float(input("How many hours did {} work? " .format(name))) # Formatting to show name in question
            pay_rate = float(input("What is {}'s pay rate? ".format(name)))
            
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
            totalOvertime = totalOvertime + over_time_pay
            totalReghours = totalReghours + reg_pay
            totalGrosspays = totalGrosspays + gross_pay


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
            print ()

        else:
            repeat = False # Ending the loop
            
    print ()
    print ("Total number of employees entered:", employees)
    print ("Total amount payed for overtime: $"+str(format (totalOvertime,'.2f')))
    print ("Total amount payed for regular hours: $"+str(format (totalReghours,'.2f')))
    print ("Total amount payed in gross: $"+str(format (totalGrosspays,'.2f')))



main()
