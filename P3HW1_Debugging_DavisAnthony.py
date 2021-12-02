# CTI - 110
# P3HW1_Debugging
# Anthony Davis
# 12 Oct 2021

# Debug program so that user inputs number and outputs a letter grade.

import time

def main ():
    
    # Grade variables defined.
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    print ('-----Grading Calculator-----')
    print ()
    score = float(input ('Please enter a number grade: '))
    print ()
    print ('Calculating...')
    time.sleep(2)
    print ()
    if score >= A_score:
        print ('Your grade is an A! Good Job!')
    elif score >= B_score:
        print ('Your grade is a B.')
    elif score >= C_score:
        print ('Your grade is a C.')
    elif score >= D_score:
        print ('Your grade is a D.')

    else:
        print ('Uh oh! Your grade is an F.')

main ()


        
