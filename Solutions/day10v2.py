from pprint import pprint


# Coords in form map[y][x]

def findStart(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (map[y][x] == 'S'):
                return [y,x]
            
def findNextPos(map, currPos, prevTilePos, validMoveMap):
    # Need to check up, down, left and right for any legal moves
    # Check up
    dir = ""
    if (currPos[0]>0):
        if (map[currPos[0]-1][currPos[1]] == '|' or 
            map[currPos[0]-1][currPos[1]] == 'F' or 
            map[currPos[0]-1][currPos[1]] == '7' or
            map[currPos[0]-1][currPos[1]] == 'S'):
            dir += "up"
            if (currPos[0]-1 != prevTilePos[0]) and (map[currPos[0]][currPos[1]]) in validMoveMap["up"]:
                return [currPos[0]-1, currPos[1]]
    # Check down
    if (currPos[0]<len(map)-1):
        if (map[currPos[0]+1][currPos[1]] == '|' or 
            map[currPos[0]+1][currPos[1]] == 'J' or 
            map[currPos[0]+1][currPos[1]] == 'L' or
            map[currPos[0]+1][currPos[1]] == 'S'):
            dir += "down"
            if (currPos[0]+1 != prevTilePos[0]) and (map[currPos[0]][currPos[1]]) in validMoveMap["down"]:
                return [currPos[0]+1, currPos[1]]
    # Check left
    if (currPos[1]>0):
        if (map[currPos[0]][currPos[1]-1] == '-' or 
            map[currPos[0]][currPos[1]-1] == 'F' or 
            map[currPos[0]][currPos[1]-1] == 'L' or
            map[currPos[0]][currPos[1]-1] == 'S'):
            dir += "left"
            if (currPos[1]-1 != prevTilePos[1]) and (map[currPos[0]][currPos[1]]) in validMoveMap["left"]:
                return [currPos[0], currPos[1]-1]
    # Check right
    if (currPos[1]<len(map[0])-1):
        if (map[currPos[0]][currPos[1]+1] == '-' or 
            map[currPos[0]][currPos[1]+1] == '7' or 
            map[currPos[0]][currPos[1]+1] == 'J' or
            map[currPos[0]][currPos[1]+1] == 'S'):
            dir += "right"
            if (currPos[1]+1 != prevTilePos[1]) and (map[currPos[0]][currPos[1]]) in validMoveMap["right"]:
                return [currPos[0], currPos[1]+1]
    # If no legal moves found, return prevTilePos
    print("No legal moves found")
    print("We are at ", currPos, "and prevTilePos is ", prevTilePos)
    print(map[currPos[0]][currPos[1]])
    print(map[prevTilePos[0]][prevTilePos[1]])
    print("Valid moves are", dir)
    # Print current row
    print(map[currPos[0]])


with open("Inputs/day10.txt", 'r') as file:
    map = file.read().split('\n')
    path=[]
    startCoords = findStart(map)
    print("Start coords:", startCoords)
    numMoves = 0
    currPos = startCoords
    prevTilePos = [-1,-1]
    validMoveMap = {}
    validMoveMap["up"] = ['J', 'L', '|', 'S']
    validMoveMap["down"] = ['F', '7', '|', 'S']
    validMoveMap["right"] = ['F', 'L', '-', 'S']
    validMoveMap["left"] = ['7', 'J', '-', 'S']

    # validMoveMap.append("up", ['J', 'L', '|'])
    # validMoveMap.append("down", ['F', '7', '|'])
    # validMoveMap.append("left", ['F', 'L', '-'])
    # validMoveMap.append("right", ['7', 'J', '-'])
    while True:
        tilePos = findNextPos(map, currPos, prevTilePos, validMoveMap)
        prevTilePos = currPos
        currPos = tilePos
        path.append(map[currPos[0]][currPos[1]])
        numMoves += 1
        if (map[currPos[0]][currPos[1]] == 'S'):
            break
    print((numMoves + 1) // 2)
