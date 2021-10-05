# CTI 110
# P3T2 - Nested IFs
# Anthonoy Davis
# 5 Oct 2021

# To qualify:
#    - must have salary >= 30 000
#    - must have worked current job 2+ years

# Ask user for salary and time worked at job
# Check if salary qualifies
#    If it does...
#    Check if years_worked >= 2
#         If both are true, they qualify

salary = float (input ('Enter salary: '))
years_worked = int (input ('Enter years at current job: '))

if salary >= 30000:
    #print ("Salary is high enough.")
    if years_worked >= 2:
        print ('Congratulations! You qualify for the loan.')
    else:
        print ('Sorry, your time at current job does not qualify for the loan.')

else:
    print ('Sorry, your salary does not qualify for this loan.')
