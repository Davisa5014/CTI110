# CTI - 110
# P4HW1 - Expense Calculator
# Anthony Davis
# 28 Oct 2021

# Prompt user to enter amount in account in which money will be withdrawn.
# Prompt user to enter amount of first expense.
# Subtract expense from account.
# Ask user if they would like to enter another expense.
# Program DOES NOT move on to next step unless user chooses NOT to enter another expense.

def main():
    # assigning variables
    account = 0
    expenses = 0
    expenseCount = 0
    keepGoing = True # Using flag because makes sense in my mind.

    account = float(input("Enter starting amount in account $"))

    while keepGoing == True: # entire while loop
        expenses = float(input("Enter expense: "))
        expenseCount = expenseCount + 1
        # print (expenseCount) - Original test for counting number of expenses.
        repeat = input("Do you want to enter another expense? (y/n)")
        if repeat == 'y':
            keepGoing = True # Keeps repeating loop

        else:
            keepGoing = False # Ends loop

    print ("Amount in account before expenses subracted $"+str(format (account, '.2f')))
    print ("Number of expenses entered:", expenseCount)
    print ("Amount in account after expenses subracted is $"+str(format (account - expenses, '.2f')))
             
        



main ()
        
