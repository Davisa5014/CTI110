# CTI 110
# P2LAB2
# CAFFEINE LEVELS
# ANTHONY DAVIS
# 28 SEP 2021

# Code will ask for initial caffeine level and then give half life
# throughout the day.



caffeine_mg = float(input('Enter caffeine amount: '))

caffeine_mg = caffeine_mg / 2

print ('After 6 hours: ''{:.2f}' ' mg'.format (caffeine_mg))

caffeine_mg = caffeine_mg / 2

print ('After 12 hours: ''{:.2f}' ' mg'.format (caffeine_mg))

caffeine_mg = caffeine_mg / 4 # Changed this to 4 after realizing 24 hrs

print ('After 24 hours: ''{:.2f}' ' mg'.format (caffeine_mg))


