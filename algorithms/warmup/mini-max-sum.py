# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Score: 10/10

def miniMaxSum(arr):
    smallest = arr[0]
    largest = 0
    total = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
        elif arr[i] > largest:
            largest = arr[i]
        total = total + arr[i]
    print(total - largest, total - smallest)

def altMiniMaxSum(arr):
    minSum = sum(arr) - max(arr)
    maxSume = sum(arr) - min(arr)
    print(minSum, maxSum)
