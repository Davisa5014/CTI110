# CTI - 110
# P4T4 - Running Total with Sentinel
# Anthony Davis
# 26 Oct 2021

# We will again add up numbers, this time it's hours worked.
# The user will enter values until they enter a -1.
# Here the -1 is a "Sentinel" value that just means "done".

total = 0
currentHours = 0
keepGoing = True

# Explain what's happening
print ("Enter each days's hours worked on a different line.")
print ("Enter -1 (or any negative number) to finish.")
# Loop until done
while keepGoing == True:
    
    # Ask the user for numbers of hours
    currentHours = float(input("Enter numbers of hours worked: "))
    # if it's less than 0, we're finished
    if currentHours < 0:
        keepGoing = False
        
    # otherwise, add it to the total
    else:
        total += currentHours # same as total = total + currentHours

# we're out of the loop
print ("Total hours entered:", total)
