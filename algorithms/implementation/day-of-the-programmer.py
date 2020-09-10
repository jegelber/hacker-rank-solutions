# Problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# Score: 15/15

def dayOfProgrammer(year):
    days = 243
    # Julian calendar
    if year < 1918:
        if year%4 == 0:
            days += 1
    # Gregorian calendar
    elif year > 1918:
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            days += 1
    # Year is 1918
    else:
        days -= 13
    day = 256 - days
    date = "{0}.09.{1}".format(day, year)
    return date
