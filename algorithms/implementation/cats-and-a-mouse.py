# Problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Score: 15/15

def catAndMouse(x, y, z):
    cata = abs(x - z)
    catb = abs(y - z)
    if cata < catb:
        return "Cat A"
    elif cata > catb:
        return "Cat B"
    else:
        return "Mouse C"
