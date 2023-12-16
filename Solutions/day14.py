from pprint import pprint

with open("Inputs/day14.txt", 'r') as file:
    rockMap = [list(line.strip()) for line in file.readlines()]
    # Transpose map to make column logic easier
    transposed_map = list(map(list, zip(*rockMap)))
    total = 0
    for line in transposed_map:
        for i, char in enumerate(line):
            if char == 'O':
                while (i>0) and (line[i-1] != '#'):
                    line[i-1], line[i] = line[i], line[i-1]
                    i -= 1
    
    reverted_map = list(map(list, zip(*transposed_map)))
    for i, line in enumerate(reverted_map):
        distFromBottom = len(reverted_map) - i
        for char in line:
            if char == 'O':
                total += distFromBottom
    print(total)


with open("Inputs/day14.txt", 'r') as file:

    rockMap = [list(line.strip()) for line in file.readlines()]
    # Transpose map to make column logic easier
    transposed_map = list(map(list, zip(*rockMap)))
    total = 0

    current_map = transposed_map
    prev_map = []
    j=0
    while j < 3:
        j+=1
        # Roll north
        for line in transposed_map:
            for i, char in enumerate(line):
                if char == 'O':
                    while (i>0) and (line[i-1] != '#'):
                        line[i-1], line[i] = line[i], line[i-1]
                        i -= 1
        
        reverted_map = list(map(list, zip(*transposed_map)))

        # Roll west
        for line in reverted_map:
            for i, char in enumerate(line):
                if char == 'O':
                    while (i>0) and (line[i-1] != '#'):
                        line[i-1], line[i] = line[i], line[i-1]
                        i -= 1

        reverted_map = list(map(list, zip(*reverted_map)))

        # Roll south
        for line in reverted_map:
            for i, char in enumerate(line):
                if char == 'O':
                    while (i<len(line)-1) and (line[i+1] != '#'):
                        line[i+1], line[i] = line[i], line[i+1]
                        i += 1
            
        reverted_map = list(map(list, zip(*reverted_map)))

        # Roll east
        for line in reverted_map:
            for i, char in enumerate(line):
                if char == 'O':
                    while (i<len(line)-1) and (line[i+1] != '#'):
                        line[i+1], line[i] = line[i], line[i+1]
                        i += 1
    
        # reverted_map = list(map(list, zip(*reverted_map)))
        prev_map = current_map
        current_map = reverted_map

        for s in current_map:
            print(*s)
        print()

    for i, line in enumerate(reverted_map):
        distFromBottom = len(reverted_map) - i
        for char in line:
            if char == 'O':
                total += distFromBottom
    print(total)