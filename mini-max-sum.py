#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
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

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
