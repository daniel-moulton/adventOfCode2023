from pprint import pprint

def getHistory(nums):
    sequences = []
    sequences.append(nums)

    while (set(sequences[-1]) != {0}):
        sequences.append([])
        for i in range(len(sequences[-2])-1):
            sequences[-1].append(sequences[-2][i+1]-sequences[-2][i])

    for i in range(len(sequences)-1, 0, -1):
        sequences[i-1].append(sequences[i-1][-1] + sequences[i][-1])
    return sequences[0][-1]

def getOldestHistory(nums):
    # Repeat the same as getHistory, but instead of adding the difference to the end of the list, add it to the beginning
    sequences = []
    sequences.append(nums)

    while (set(sequences[-1]) != {0}):
        sequences.append([])
        for i in range(len(sequences[-2])-1):
            sequences[-1].append(sequences[-2][i+1]-sequences[-2][i])

    for i in range(len(sequences)-1, 0, -1):
        sequences[i-1].insert(0, sequences[i-1][0] - sequences[i][0])
    return sequences[0][0]

with open("Inputs/day9.txt") as f:
    lines = f.readlines()
    total=0
    for line in lines:
        nums = line.split()
        nums = [int(x) for x in nums]
        next = getHistory(nums)
        total+=next
    print(total)


with open("Inputs/day9.txt") as f:
    lines = f.readlines()
    total=0
    for line in lines:
        nums = line.split()
        nums = [int(x) for x in nums]
        next = getOldestHistory(nums)
        total+=next
    print(total)
