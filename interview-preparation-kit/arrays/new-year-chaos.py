# Score: 40/40

def minimumBribes(q):
    initial = 1
    bribes = 0
    for p in q:
        if p > initial + 2:
            print("Too chaotic")
            return
        for i in range(max(p-2, 0), initial):
            if q[i] > p:
                bribes += 1
        initial += 1
    print(bribes)
