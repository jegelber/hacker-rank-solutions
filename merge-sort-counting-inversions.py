#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    result, sortedList = sortAndCount(arr)
    return result

def sortAndCount(L):
    lengthL = len(L)
    # Base Case: If the length of the list is 1, there are no
    # inversions, return 0 inversions and the list.
    if lengthL == 1:
        return (0, L)
    # Else, the list is longer than 1.
    else:
        # Split the list into two equal parts. A being the first
        # half and B being the second.
        A = L[:lengthL//2]
        B = L[lengthL//2:]
        # Recursively run the function on each part of the list,
        # returning the number of inversions in each part and
        # the sorted list.
        (invA, A) = sortAndCount(A)
        (invB, B) = sortAndCount(B)
        # Merge the two sorted lists using the mergeAndCount function,
        # returning the number of inversions and merged list.
        (inv, L) = mergeAndCount(A, B)
        # Return the total number of inversions and the merged, sorted list.
        return (invA + invB + inv, L)

# mergeAndCount sorts lists A and B and returns the number of inversions
# in the lists and the lists merged into one list.
# Runtime: O(n)
def mergeAndCount(A, B):
    # Initialize the empty mergedList return list to empty.
    mergedList = []
    # Initialize the inversion count and list pointers to 0.
    # i points to the current place in A, while j points
    # to the current place in B.
    invCount = 0
    i = 0
    j = 0
    lengthA = len(A)
    lengthB = len(B)
    # While the pointers have not reached the end of either list.
    while i < lengthA and j < lengthB:
        # If the smaller element is in B, append that element to return list, add the
        # number elements in A that have not yet been incremented to the 
        # inversion count and increment j.
        if B[j] < A[i]:
            mergedList.append(B[j])
            invCount += lengthA-i
            j+=1
        # Else, the smaller element is in A, append that element to return list
        # and increment i.
        else:
            mergedList.append(A[i])
            i+=1
    # If i has not reached the end of A, append the rest of A
    # to the return list.
    if i != lengthA:
        mergedList.extend(A[i:])
    # Else j has not reached the end of B, append the rest of
    # B to the return list.
    else:
        mergedList.extend(B[j:])
    # Return the final inversion count and merged list.
    return (invCount, mergedList)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
