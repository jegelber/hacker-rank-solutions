# Problem: https://www.hackerrank.com/challenges/migratory-birds/problem
# Score: 10/10

def migratoryBirds(arr):
    sightings = [0, 0, 0, 0, 0, 0]
    mostCommonNum = 0
    mostCommonId = 0

    for bird in arr:
        sightings[bird] += 1

    for i in range(6):
        if sightings[i] > mostCommonNum:
            mostCommonNum = sightings[i]
            mostCommonId = i

    return mostCommonId
