# Problem: https://www.hackerrank.com/challenges/drawing-book/problem
# Score: 10/10
import math

def pageCount(n, p):
    turns = math.floor(n/2)
    front = math.floor(p/2)
    back = turns - front
    return min(front, back)
