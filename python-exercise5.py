#get day number from user
day = int(input('Day (0-6)? '))

#tell user what to do based on input
if day == 0 or day == 1:
    print('Sleep in')
else:
    print('Go to work')