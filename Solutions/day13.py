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



### Part 2
"""
Okay not sure how well this will work but in theory (hope) it is logically sound.
Need to do the same as for part 1 but instead need to find the smudge in the pattern 
and change it which will give us a new line of symmetry.

First idea to find the smudge is to convert the string to binary representation
and do the same as in part 1 but if we get a pairing that doesn't match store that for later.

If we end up with only one mismatched pairing then convert the two lines to a binary representation
and see if they differ by a value of 2^N (actually can just check that the resulting string has one '1').
So if we had 
#.##..##.
..##..##.
they differ by 1 character, if we convert each to a binary value (0 for . and 1 for #) we get
101100110
001100110
If we (abs) subtract these we get 100000000 which contains one '1' so we know that the two lines only differ by 1 char.
And since these were the onyl two lines that differed, we know the new line of symmetry is valid.

(Definitely unnecessary but I like the binary idea so screw it)


Update: subtraction isn't foolproof, some edge cases where the answer can be one off,
but the two nums differ by more than one character. XOR fixes this as compares as a pair of bits.
"""

def findSymmetryPart2(pattern, vertical=False):
    for i in range(len(pattern)-1):
        numMismatchedPairs = []
        x = i
        y = i+1
        while (x >= 0) and (y < len(pattern)) and len(numMismatchedPairs) <= 2:
            if pattern[x] != pattern[y]:
                numMismatchedPairs.append(pattern[x])
                numMismatchedPairs.append(pattern[y])
            x -= 1
            y += 1
            if (x == -1) or (y == len(pattern)):
                break
        if len(numMismatchedPairs) == 2 and (x == -1 or y == len(pattern)):
            str1 = ''.join(numMismatchedPairs[0]).replace('.', '0').replace('#', '1')
            str2 = ''.join(numMismatchedPairs[1]).replace('.', '0').replace('#', '1')
            diff = int(str1, 2) ^ int(str2, 2)
            if bin(diff).count('1') == 1:
                print(str1, str2)
                print(bin(diff))
                if vertical:
                    return True, i+1
                else:
                    return False, i+1

        # if pattern[i] == pattern[i+1]:
        #     x = i
        #     y = i+1
        #     while (x >= 0) and (y < len(pattern)) and (pattern[x] == pattern[y]):
        #         x -= 1
        #         y += 1
        #     if (x == -1) or (y == len(pattern)):
        #         if vertical:
        #             return True, i+1
        #         else:
        #             return False, i+1
    
    if (not vertical):
        transposed = list(map(list, zip(*pattern)))
        return findSymmetryPart2(transposed, True)



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
        isVertical, numLines = findSymmetryPart2(pattern)
        if isVertical:
            total += numLines
        else:
            total += numLines * 100
    print(total)
