# Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Score: 10/10

def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]
    bcount = 0
    wcount = 0
    for s in scores:
        if s > best:
            best = s
            bcount = bcount + 1
        if s < worst:
            worst = s
            wcount = wcount + 1
    return bcount, wcount
