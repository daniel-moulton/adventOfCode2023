from pprint import pprint


# Coords in form map[y][x]

def findStart(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (map[y][x] == 'S'):
                return [y,x]

# def howToMove(currPos, tile, tilePos):
#     # currPos & tilePos in form [y, x] to match map
#     # Tile is the current tile

#     match tile:
#         case '|':
#             if (currPos[0]<tilePos[0]):
#                 return 1,0 # Down
#             else:
#                 return -1,0 # Up
#         case '-':
#             if (currPos[1]<tilePos[1]):
#                 return 0,1 # Right
#             else:
#                 return 0,-1 # Left
#         case 'F':
#             if (currPos[0] == tilePos[0]):
#                 return 1,-1 # Down-Left
#             else:
#                 return -1,1 # Up-Right
#         case '7':
#             if (currPos[0] == tilePos[0]):
#                 return 1,1 # Down-Right
#             else:
#                 return -1,-1 # Up-Left
#         case 'J':
#             if (currPos[0] == tilePos[0]):
#                 return -1,1 # Up-Right
#             else:
#                 return 1,-1 # Down-Left
#         case 'L':
#             if (currPos[0] == tilePos[0]):
#                 return -1,-1 # Up-Left
#             else:
#                 return 1,1 # Down-Right

def getNextTilePos(currPos, map, prevTilePos, start=False):
    # Check up down left and right for a tile which we can move to
    # If one found, return that tile

    print("Checking for next tile from", currPos, "to", prevTilePos)
    # Check up
    if (currPos[0]-1 == prevTilePos[0] and not start):
        pass
    elif (currPos[0]-1 >= 0):
        if (map[currPos[0]-1][currPos[1]] == '|' or 
            map[currPos[0]][currPos[1]+1] == 'F' or 
            map[currPos[0]][currPos[1]+1] == '7'):
            return [currPos[0]-1, currPos[1]]
    # Check down
    if (currPos[0]+1 == prevTilePos[0] and not start):
        pass
    elif (currPos[0]+1 < len(map)):
        if (map[currPos[0]+1][currPos[1]] == '|' or 
            map[currPos[0]][currPos[1]+1] == 'J' or 
            map[currPos[0]][currPos[1]+1] == 'L'):
            return [currPos[0]+1, currPos[1]]
    # Check left
    if (currPos[1]-1 == prevTilePos[1] and not start):
        pass
    elif (currPos[1]-1 >= 0):
        if (map[currPos[0]][currPos[1]-1] == '-' or
            map[currPos[0]][currPos[1]-1] == 'F' or
            map[currPos[0]][currPos[1]-1] == 'L'):
            return [currPos[0], currPos[1]-1]
    # Check right
    if (currPos[1]+1 == prevTilePos[1] and not start):
        pass
    elif (currPos[1]+1 < len(map[currPos[0]])):
        if (map[currPos[0]][currPos[1]+1] == '-' or 
            map[currPos[0]][currPos[1]+1] == '7' or
            map[currPos[0]][currPos[1]+1] ==  'J'):
            return [currPos[0], currPos[1]+1]

def makeMove(map, currPos, moveSteps):
    pprint(moveSteps)
    return [currPos[0] + moveSteps[0], currPos[1] + moveSteps[1]]

with open("Inputs/day10.txt", 'r') as file:
    map = file.read().split('\n')
    path=[]
    startCoords = findStart(map)
    print("Start coords:", startCoords)
    numMoves = 0
    currPos = startCoords
    prevTilePos = startCoords
    for i in range(10):
        tilePos = getNextTilePos(currPos, map, prevTilePos, start=(numMoves==0))
        # moveSteps = howToMove(currPos, map[tilePos[0]][tilePos[1]], tilePos)
        nextPos = makeMove(map, currPos, tilePos)
        print("Moving from", currPos, "(", map[currPos[0]][currPos[1]], ") to", nextPos, "(", map[nextPos[0]][nextPos[1]], ") via", map[tilePos[0]][tilePos[1]], "with", moveSteps, "\n")
        path.append(map[currPos[0]][currPos[1]])
        numMoves += 1
        prevTilePos = tilePos
        currPos = nextPos
        if (map[currPos[0]][currPos[1]] == 'S'):
            break
    print(path)

