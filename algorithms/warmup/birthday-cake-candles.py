# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Score: 10

def birthdayCakeCandles(ar):
    tallest = max(ar)
    count = 0
    for i in range(len(ar)):
        if ar[i] == tallest:
            count = count + 1
    return count
