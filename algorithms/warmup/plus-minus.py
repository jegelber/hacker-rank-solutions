# Problem: https://www.hackerrank.com/challenges/plus-minus/problem
# Score: 10/10

def plusMinus(arr):
    pcount = 0
    ncount = 0
    zcount = 0
    length = len(arr)
    for i in range(length):
        if arr[i] < 0:
            ncount += 1
        elif arr[i] > 0:
            pcount += 1
        else:
            zcount += 1
    print('%.6f'%(pcount/length))
    print('%.6f'%(ncount/length))
    print('%.6f'%(zcount/length))
