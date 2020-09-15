# Problem: https://www.hackerrank.com/challenges/electronics-shop/problem
# Score: 15/15

def getMoneySpent(keyboards, drives, b):
    spent = -1
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                spent = max(spent, i + j)
    return spent
