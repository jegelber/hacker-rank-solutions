# Score: 40/40

# [4, 5, 7, 6, 1, 2, 3]
# initialize swaps count
# for each index of arr
# if index + 1 doesn't match arr[index]
# while index + 1 doesn't match arr[index]
## set temp = arr[index]
## arr[index] = arr[arr[index]-1]
## arr[arr[index]-1] = temp
## add 1 to swaps count
# return swaps

def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while(arr[i] != (i + 1)):
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            swaps += 1
    return swaps
