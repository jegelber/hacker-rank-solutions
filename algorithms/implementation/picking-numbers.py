# Problem: https://www.hackerrank.com/challenges/picking-numbers/problem
# Score: 20/20

def pickingNumbers(a):
    freq = {x:0 for x in range(max(a) + 2)}
    longest = -1
    for x in a:
        freq[x] += 1
        y = freq[x] + freq[x+1]
        z = freq[x] + freq[x-1]
        longest = max([longest, y, z])
    return longest
