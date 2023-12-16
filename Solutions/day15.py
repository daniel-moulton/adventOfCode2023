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
    stepDict = {}
    sum = 0
    for step in input:
        if step not in stepDict:
            stepDict[step] = calcStep(step)
        sum += stepDict[step]
    print(sum)

with open("Inputs/day15.txt", 'r') as file:
    input = file.readline().strip().split(',')
    stepDict = {}
    sum = 0
    for i in range(256):
        stepDict[i] = []
    for step in input:
        print(step)
        if '-' in step:
            # If we have a -, we want to hash the rest of the step, go to that box
            # and if a lens w matching label is there, remove it and shift rest left
            # Otherwise do nothing 
            hash = calcStep(step[:-1])
            contents = stepDict[hash]
            for box in contents:
                if box[0] == ''.join(step[:-1]):
                    contents.remove(box)
                    break
        else:
            focalLens = step[-1]
            hash = calcStep(step[:-2])
            contents = stepDict[hash]
            for box in contents:
                if box[0] == ''.join(step[:-2]):
                    box[1]=focalLens
                    break
            else:
                contents.append([step[:-2], focalLens])
            pass
    for key in stepDict:
        if stepDict[key] != []:
            for i, box in enumerate(stepDict[key]):
                sum += (key+1) * (i+1) * int(box[1])
    print(sum)
