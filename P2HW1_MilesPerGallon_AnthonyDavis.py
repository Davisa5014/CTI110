# Program will calculate Miles Per Gallon and gas costs
# 4 Oct 2021
# CTI - 110 P2HW1 - Miles per Gallon
# Anthony Davis

# Setting input variables for later math

print ('Handy Dandy Gas Calculater 5000!')
print ()
milesDriven = int(input ('Enter Miles Driven: '))
gallons = int(input ('Enter Gallons Used: '))
gasCost = float(input ('Enter Gas Cost: '))
print ()

# Setting up arithmetic before print statements

milesPer = milesDriven / gallons # Calculates Miles Per Gallon

totalCost = gallons * gasCost # Calculates Total Gas Cost

costMile = totalCost / milesDriven # Calculates gas Cost Per Mile

print ('Miles Per Gallon:   ''{:.2f}'.format (milesPer))
print ('Total Gas Cost:     $''{:.2f}'.format (totalCost))
print ('Cost Per Mile:      $''{:.1f}'.format (costMile))
