# If writing more than one condition use elif to continue
if 2 < 10:
    print('2 is less than 10')
elif 3 > 2:
    print('3 is also greater than 2')
else:
    print('I dont even know what you just typed man')


# The if statement can also be nested
if 2 < 10:
    print('2 is less than 10')
    if 3 > 1:
        print('3 is also greater than 1')
    else:
        print('3 is apparently not greater than 1')
else:
    print('2 is apparently not less than 10')

