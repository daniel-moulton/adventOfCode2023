import re
import math as Math

print("Part 1")

winnersLength=0

with open("Inputs/day4.txt") as f:
    lines = f.readlines()
    total=0
    for line in lines:
        localCount=-1
        parts = line.split("|")
        winners = re.findall("\d+", parts[0])
        numbers = re.findall("\d+", parts[1])
        winners.pop(0)
        for i in range(len(numbers)):
            if numbers[i] in winners:
                localCount+=1
        if (localCount != -1):
            total+=Math.pow(2, localCount)
        if (len(winners) > winnersLength):
            winnersLength = len(winners)
    print(total)


print("Part 2")

with open("Inputs/day4.txt") as f:
    lines = f.readlines()
    total=0
    arr = [1] * (winnersLength+1)
    print("START")
    for line in lines:
        numMatching=0
        parts = line.split("|")
        winners = re.findall("\d+", parts[0])
        numbers = re.findall("\d+", parts[1])
        winners.pop(0)

        # For each number in numbers, check if it is a winning value, if so increment numMatching
        for i in range(len(numbers)):
            if numbers[i] in winners:
                numMatching+=1
        

        for j in range(0, arr[0]):
            for i in range(1, numMatching+1):
                arr[i]+=1
        total+=arr[0]
        
        # Shift array left
        for i in range(0, winnersLength):
            arr[i] = arr[i+1]
        arr[winnersLength] = 1
    print(total)

