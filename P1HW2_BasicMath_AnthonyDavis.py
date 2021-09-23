# Using math to show monthly and yearly bill amounts
# 21 Sep 2021
# CTI-110 P1HW2 - Basic Math
# Anthony Davis

# Ask user for billName() - Name of the bill
# Ask user for float() billAmount - amount of billName
# Display billName and billAmount
# Display float() salesTax = billAmount * 0.0475
# Display monthly amount float(billTotal) = billAmount + salesTax
# Display yearly amounty float() billTotal * 12

billName = (input("Please enter name of expense: "))
billAmount = float(input("Please enter amount of expense: $"))
print ("Bill:", billName, "--------", "Amount Before Tax: $"+str(format (billAmount, '.2f')))
salesTax = billAmount * 0.0700
monthlyCharge = billAmount + salesTax
yearlyCharge = monthlyCharge * 12
print ("Monthly Tax: $"+str(format (salesTax, '.2f'))) # Rounded to 2 decimal places
print ("Monthly Charge: $"+str(format (monthlyCharge, '.2f')))
print ("Annual Charge: $"+str(format (yearlyCharge, '.2f')))
