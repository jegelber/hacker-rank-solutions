from collections import Counter

def countTriplets(arr, r):
    freq = Counter(arr)
    pairs = {}
    count = 0

    for val in reversed(arr):
        val_x_ratio = (val * r)
        if val_x_ratio in pairs:
            count += pairs[val_x_ratio]
        if val_x_ratio in freq:
            if val in pairs:
                pairs[val] += freq[val_x_ratio]
            else:
                pairs[val] = freq[val_x_ratio]
    return count


print(countTriplets([1,4,16,64], 4))
