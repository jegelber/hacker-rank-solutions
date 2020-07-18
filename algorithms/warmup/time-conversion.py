# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Score: 15/15

def timeConversion(s):
    ret = ''
    hour = int(s[:2])
    morning = 'AM' in s
    if hour == 12 and morning:
        ret = '00' + s[2:8]
    elif morning:
        ret = s[:8]
    elif hour == 12 and not morning:
        ret = '12' + s[2:8]
    else:
        hour = hour + 12
        ret = str(hour) + s[2:8]
    return ret
