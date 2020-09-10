# Problem: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Score: 10/10

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i] + ar[j])%k == 0:
                count += 1
    return count
