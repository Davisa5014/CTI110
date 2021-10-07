# P3LAB3 - Interstate Highway
# CTI - 110
# Anthony Davis
# 7 Oct 2021

"""
Background:
Primary U.S. interstate highways are numbered 1-99.
Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90)
go east/west. Auxiliary highways are numbered 100-999,
and service the primary highway indicated by the rightmost two digits.
Thus, I-405 services I-5, and I-290 services I-90. 
"""

# Given a highway number, indicate whether it is a primary or auxiliary highway.
# If auxiliary, indicate what primary highway it serves.
# Also indicate if the (primary) highway runs north/south or east/west. 

# User inputs highway number.

isPrimary = True
isValid = True
highway = int(input("Enter highway number: "))


if highway >= 1 and highway <= 99: #Determines if primary highway.
    print ('I-' + str (highway), 'is a primary highway.')
 
elif highway >= 100 and highway <=999: #Determines if auxiliary highway.
    print ('I-' + str (highway), 'is an auxiliary highway.')
    isPrimary = False # Flag set if auxiliary highway.
else:
    print (highway, 'is not a valid highway number.') # Displayed if not valid.
    isValid = False
    
if isPrimary == False: # Shows that input is auxiliary from isPrimary flag.
    primary = highway % 100 # Modulo to take off 100's place of highway.
    print ('It serves highway I-' + str (primary) + str ('.'))

if isValid == True:
    if highway % 2 == 0: # Modulo to show even which is east/west.
        print ('The highway goes east/west.')
    else: # Shows odd which makes highway north/south.
        print ('The highway goes north/south.')
