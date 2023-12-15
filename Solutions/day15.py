from pprint import pprint

def calcStep(step):
    total=0
    for char in step:
        total += ord(char)
        total *= 17
        total %= 256
    return total

with open("Inputs/day15.txt", 'r') as file:
    input = file.readline().strip().split(',')
    pprint(input)
    stepDict = {}
    sum = 0
    for step in input:
        if step not in stepDict:
            stepDict[step] = calcStep(step)
        sum += stepDict[step]
    print(sum)
    
with open("Inputs/day15.txt", 'r') as file:
    input = file.readline().strip().split(',')
    pprint(input)
    stepDict = {}
    sum = 0
    for step in input:
        if step not in stepDict:
            stepDict[step] = calcStep(step)
        sum += stepDict[step]
    print(sum)