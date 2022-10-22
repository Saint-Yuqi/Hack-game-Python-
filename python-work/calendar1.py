month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
s = 0
m = 11
y = 2001

not_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = (y-1) % 400
day = (day//100) * 5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4) * 2
day = day % 7

if y % 4 == 0:
    for i in range(m-1):
        s += leap_year[i]
else:
    for i in range(m-1):
        s += not_leap_year[i]

day = (day + (s % 7)) % 7

print(month[m], y)
print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')

space = ' '
space = space.rjust(2, ' ')

if m == 4 or m == 6 or m == 9 or m == 11:
    for i in range(31 + day):
        if i <= day and day != 6:
            print(space, end=' ')
        elif (i - day) > 0:
            print("{:02d}".format(i - day), end=' ')
            if (i + 1) % 7 == 0:
                print()
elif m == 2:
    if y % 4 == 0:
        p = 30
    else:
        p = 29
    for i in range(p + day):
        if i <= day and day != 6:
            print(space, end=' ')
        elif (i - day) > 0:
            print("{:02d}".format(i - day), end=' ')
            if (i + 1) % 7 == 0:
                print()
else:
    for i in range(32 + day):
        if i <= day and day != 6:
            print(space, end=' ')
        elif (i - day) > 0:
            print("{:02d}".format(i - day), end=' ')
            if (i + 1) % 7 == 0:
                print()
