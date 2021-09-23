# CTI 110
# P1T3
# ANTHONY DAVIS
# 23 SEP 2021

# PRINT A RESTURAUNT RECEIPT

mealCost = (float(input('Please enter your meal total: $')))
taxPct = 0.07
mealTax = mealCost * taxPct
mealTotal = mealCost + mealTax
print ('Thank you for dining at Python Cafe')
print ('-' * 35)
print ('Meal: $'+str(format (mealCost, '.2f')))
print ()
print ('Tax:  $'+str(format (mealTax, '.2f')))
print ('-' * 35)
print ('Total: $'+str(format (mealTotal, '.2f')))