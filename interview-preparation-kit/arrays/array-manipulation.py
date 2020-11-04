# Score: 60/60

# initialize array of n 0s
# initialize max_val to -1
# for each query in queries
## extract values of a, b, and k
## for x from index a to index b in arr
### add k to x
### test if x is new max_val
# return max_val

# Brute Force Solution
# def arrayManipulation(n, queries):
#     arr = [0 for x in range(n)]
#     max_val = 0
#     for i in range(len(queries)):
#         a = queries[i][0]
#         b = queries[i][1]
#         k = queries[i][2]
#         for j in range(max(a - 1, 0), b):
#             arr[j] += k
#             max_val = max(max_val, arr[j])
#     return max_val

# Optimal Solution 
def arrayManipulation(n, queries):
    arr = [0] * n
    for q in queries:
        arr[q[0] - 1] += q[2]
        if q[1] != n:
            arr[q[1]] -= q[2]
    max_val = 0
    step = 0
    for x in arr:
        step += x
        max_val = max(max_val, step)
    return max_val

arrayManipulation(5, [[1, 2, 100],[2, 5, 100],[3, 4, 100]])
