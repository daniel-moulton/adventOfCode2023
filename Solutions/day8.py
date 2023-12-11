from pprint import pprint
import re
import math as Math
with open("Inputs/day8.txt") as f:
    instructions = f.readline()
    instructions = [x for x in instructions if x != "\n"]
    f.readline()

    lines = f.readlines()
    nodes = []
    for line in lines:
        node = (re.findall("[a-zA-Z]+", line))
        nodes.append(node)

    currentDest = "AAA"
    index = -1
    numMoves = 0
    while currentDest != "ZZZ":
        index = (index + 1) % len(instructions)
        numMoves+=1
        for i in range(len(nodes)):
            if nodes[i][0] == currentDest:
                if (instructions[index] == "L"):
                    currentDest = nodes[i][1]
                else:
                    currentDest = nodes[i][2]
                break
    
    print(numMoves)


with open("Inputs/day8.txt") as f:
    instructions = f.readline()
    instructions = [x for x in instructions if x != "\n"]
    f.readline()

    lines = f.readlines()
    nodes = []
    for line in lines:
        node = (re.findall("[a-zA-Z0-9]+", line))
        nodes.append(node)

    currentDests = []
    for x in nodes:
        if (x[0][-1] == 'A'):
            currentDests.append(x[0])
    pprint(currentDests)
    index = -1
    numMoves = 0
    numMovesList = []

    for i in range(len(currentDests)):
        currentDest = currentDests[i]
        while currentDest[-1] != "Z":
            index = (index + 1) % len(instructions)
            numMoves+=1
            for i in range(len(nodes)):
                if nodes[i][0] == currentDest:
                    if (instructions[index] == "L"):
                        currentDest = nodes[i][1]
                    else:
                        currentDest = nodes[i][2]
                    break
        numMovesList.append(numMoves)
        numMoves = 0
        index = -1
    
    print(Math.lcm(*numMovesList))