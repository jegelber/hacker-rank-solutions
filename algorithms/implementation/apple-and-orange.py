# Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Score: 10/10

def countApplesAndOranges(s, t, a, b, apples, oranges):
    fruitCount(s, t, a, apples)
    fruitCount(s, t, b, oranges)

def fruitCount(s, t, tree, fruit):
    count = 0
    for f in fruit:
        position = tree + f
        if s <= position <= t:
            count = count + 1
    print(count)
