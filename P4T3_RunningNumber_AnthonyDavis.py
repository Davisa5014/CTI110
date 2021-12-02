# CTI - 110
# P4T3
# RUNNING TOTAL
# ANTHONY DAVIS
# 21 OCT 2021

# FOR THIS PROGRAM WE'RE ADDING UP NUMBERS

currentNumber = 0 # WE'LL STORE EACH NUMBER HERE BEFORE ADDING
total = 0
numEntries = 0 # ASK USER HOW MANY TIMES TO LOOP
count = 0 # USED TO KEEP TRACK OF OUR LOOP


# WE'LL ASK THE USER HOW MANY

numEntries = int(input("How many numbers to add? "))
while numEntries <= 0:
    print("Please enter a value greater than zero.")
    numEntries = int(input("How many numbers to add? "))

# THEN LOOP AND ENTER EACH NUMBER

while count < numEntries:
    #print ("*count =" , count, "numEntries =", numEntries) # debugging
    currentNumber = int(input("Enter number: "))
    total = total + currentNumber
    count = count + 1
    
# FINALLY PRINT THE TOTAL

print ("The total is: ", total)

# CAN WE FIND THE AVERAGE?

average = total / numEntries
print ("The average is:", average)

