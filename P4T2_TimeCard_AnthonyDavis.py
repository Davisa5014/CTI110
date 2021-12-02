# CTI 110
# P4T2
# TIME CARD
# ANTHONY DAVIS
# 21 OCT 2021

# This program will act like a time card reader,
# adding up each day's hours to get the total.

# TODO: it would be nice if it used the actual
# days of the week ("Monday", etc.)
# Version 1
# Change number of days for 7 day work week.

"""
DAYS_IN_WEEK = 5
totalHours = 0 # Obviously the total starts at zero.

print("Please enter your hours worked.")

for day in range (DAYS_IN_WEEK):
    print("Hours for day", day+1, ":")
    hoursToday = float(input())
    totalHours = totalHours + hoursToday # add to running total

# print the total
print("You worked a total of", totalHours, "hours this week.")

# print the average
avgHours = totalHours / DAYS_IN_WEEK
print ("For an averaage of", format(avgHours, "0.2f"),  "hours per day.")
"""

# Version 2 - using names of the days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
totalHours = 0

for day in days:
    print ("Hours for", day, ":")
    hoursToday = float(input())
    totalHours = totalHours + hoursToday

print ("You worked a total of", totalHours, "hours this week.")

avgHours = totalHours / 7
print ("For an average of", format(avgHours, "0.2f"), "hours per day.")
