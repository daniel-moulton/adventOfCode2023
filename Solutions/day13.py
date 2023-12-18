from pprint import pprint

def findSymmetry(pattern, vertical=False):
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            x = i
            y = i+1
            while (x >= 0) and (y < len(pattern)) and (pattern[x] == pattern[y]):
                x -= 1
                y += 1
            if (x == -1) or (y == len(pattern)):
                if vertical:
                    return True, i+1
                else:
                    return False, i+1
            
    # Transpose the pattern
    transposed = list(map(list, zip(*pattern)))
    return findSymmetry(transposed, True)


with open("Inputs/day13.txt", 'r') as file:
    patterns = []
    currPattern = []
    for line in file.readlines():
        if line == '\n':
            patterns.append(currPattern)
            currPattern = []
        else:
            currPattern.append(line.strip())
    if currPattern:
        patterns.append(currPattern)

    total = 0
    for pattern in patterns:
        isVertical, numLines = findSymmetry(pattern)
        if isVertical:
            total += numLines
        else:
            total += numLines * 100
    print(total)
