# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Score: 10/10

def diagonalDifference(arr):
    x = len(arr)
    lrSum = 0
    rlSum = 0
    for i in range(x):
        lrSum += arr[i][i]
        rlSum += arr[i][x-1-i]
    return abs(lrSum - rlSum)
