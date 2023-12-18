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



### Part 2

with open("Inputs/day14.txt", 'r') as file:

    rockMap = [list(line.strip()) for line in file.readlines()]
    # Transpose map to make column logic easier
    transposed_map = list(map(list, zip(*rockMap)))

    current_map = transposed_map
    prev_map = []
    cycles = {}
    cycleLength = 0
    j=0
    while j < 1_000_000_000:
        total = 0
        if (j%1_000_000 == 0):
            print(j)
        # Roll north
        for line in transposed_map:
            for i, char in enumerate(line):
                if char == 'O':
                    while (i>0) and (line[i-1] != '#'):
                        line[i-1], line[i] = line[i], line[i-1]
                        i -= 1
        
        transposed_map = list(map(list, zip(*transposed_map)))

        # Roll west
        for line in transposed_map:
            for i, char in enumerate(line):
                if char == 'O':
                    while (i>0) and (line[i-1] != '#'):
                        line[i-1], line[i] = line[i], line[i-1]
                        i -= 1

        transposed_map = list(map(list, zip(*transposed_map)))

        # Roll south
        for line in transposed_map:
            for i, char in enumerate(line):
                if char == 'O':
                    while (i<len(line)-1) and (line[i+1] != '#'):
                        line[i+1], line[i] = line[i], line[i+1]
                        i += 1
            
        transposed_map = list(map(list, zip(*transposed_map)))

        # Roll east
        for line in transposed_map:
            for i, char in enumerate(line):
                if char == 'O':
                    while (i<len(line)-1) and (line[i+1] != '#'):
                        line[i+1], line[i] = line[i], line[i+1]
                        i += 1
    
        transposed_map = list(map(list, zip(*transposed_map)))

        for i, line in enumerate(transposed_map):
            distFromBottom = len(transposed_map) - i
            for char in line:
                if char == 'O':
                    total += distFromBottom
        
        if total in cycles:
            cycleLength = j - cycles[total]
            print("Cycle length: ", cycleLength)
            print("Cycle start: ", cycles[total])
            print("Cycle end: ", j)
            print("total: ", total)
            pprint(cycles)
            remainder = (1_000_000_000 - j) % cycleLength
            print("Remainder: ", remainder)
            # Work out the remainder of doing that cycle until we're close to 1_000_000_000
            # Then do the remainder
            j = 1_000_000_000 - remainder + 2
        else:
            cycles[total] = j

        j+=1
    print(total)
    print(cycleLength)