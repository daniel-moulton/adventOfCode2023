from pprint import pprint
import re
# with open("Inputs/day8.txt") as f:
#     instructions = f.readline()
#     instructions = [x for x in instructions if x != "\n"]
#     f.readline()

#     lines = f.readlines()
#     nodes = []
#     for line in lines:
#         node = (re.findall("[a-zA-Z]+", line))
#         nodes.append(node)

#     currentDest = "AAA"
#     index = -1
#     numMoves = 0
#     while currentDest != "ZZZ":
#         index = (index + 1) % len(instructions)
#         numMoves+=1
#         for i in range(len(nodes)):
#             if nodes[i][0] == currentDest:
#                 if (instructions[index] == "L"):
#                     currentDest = nodes[i][1]
#                 else:
#                     currentDest = nodes[i][2]
#                 break
    
#     print(numMoves)


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
    loop = True
    while (loop):
        numMoves+=1
        index = (index + 1) % len(instructions)
        for x in range(len(currentDests)):
            for i in range(len(nodes)):
                if nodes[i][0] == currentDests[x]:
                    if (instructions[index] == "L"):
                        currentDests[x] = nodes[i][1]
                    else:
                        currentDests[x] = nodes[i][2]
                    break
        
        pprint(currentDests)

        allZ = True
        for x in range(len(currentDests)):
            if (currentDests[x][-1] != 'Z'):
                allZ = False
                break
        
        if (allZ):
            print("FINISHED")
            loop = False
            break
    print(numMoves)