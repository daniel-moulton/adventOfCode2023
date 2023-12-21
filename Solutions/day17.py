class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.direction = None
        self.g = 0
        self.h = 0
        self.f = 0
        self.heatValue = 0

    def __eq__(self, other):
        return (self.position == other.position)

with open("Inputs/day17.txt", "r") as file:
    map = file.readlines()
    map = [list(line.strip()) for line in map]

    start = (0,0)
    end = (len(map)-1, len(map[0])-1)

    startNode = Node(None, start)
    endNode = Node(None, end)

    endNode.heatValue = map[(len(map)-1)][(len(map[0])-1)]

    open = []
    closed = []

    open.append(startNode)

    while open:
        currentNode = min(open, key=lambda x: x.f)
        open.remove(currentNode)
        closed.append(currentNode)
        if currentNode == endNode:
            path = []
            while currentNode is not None:
                vals = (currentNode.position, currentNode.heatValue)
                path.append(vals)
                currentNode = currentNode.parent
            path = path[::-1]
            total = 0
            for entry in path:
                total += int(entry[1])
                print(entry[0])
                print(entry[1])
                print()
            print(total)
            break
        
        children = []
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])
            if nodePosition[0] < 0 or nodePosition[0] >= len(map) or nodePosition[1] < 0 or nodePosition[1] >= len(map[0]):
                continue
            newNode = Node(currentNode, nodePosition)
            newNode.heatValue = map[nodePosition[0]][nodePosition[1]]
            newNode.direction = newPosition
            children.append(newNode)

        for child in children:
            if child in closed:
                continue

            lastThreeDirections = []
            currNode = child
            same_direction = False
            while currNode is not None and len(lastThreeDirections) < 3:
                lastThreeDirections.append(currNode.direction)
                currNode = currNode.parent
            if len(set(lastThreeDirections)) == 1:
                continue
            child.g = currentNode.g + 1
            child.h = abs(child.position[0] - endNode.position[0]) + abs(child.position[1] - endNode.position[1])
            child.f = child.g + child.h
            if child in open:
                if child.g > currentNode.g:
                    continue
            open.append(child)