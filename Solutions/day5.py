from pprint import pprint
import time
start_time = time.time()

'''
Destination     Source      Range
X               Y           Z

Given a seed, S, we want to check if the seed lies between Y and Y+Z, if it does map that to it's corresponding value between X and X+Z
'''
with open("inputs/day5.txt") as f:
    seedLine = f.readline()
    seeds = [int(x) for x in seedLine.split(" ") if x != "seeds:"]

    f.readline()
    maps = []
    line = []
    for x in f:
        if x == "\n":
            maps.append(line)
            line = []
        else:
            if ("map:" not in x):
                line.append(x.strip())
    if line:
        maps.append(line)


    maps = [[[int(y) for y in x.split(" ")] for x in line] for line in maps]

    # Maps is now a 3d array of all the different maps,
    # maps[x] specifies the map i.e. seed-to-soil map
    # maps[x][y] specifies the line of the map which has the destination, source and range
    # maps[x][y][z] specifies the destination, source or range

    lowest = 0
    for seed in seeds:
        val=seed
        for map in maps:
            for line in map:
                if (line[1] <= val <= line[1] + line[2]):
                    val = line[0] + val - line[1]
                    break
        if (val < lowest or lowest == 0):
            lowest = val
    print(lowest)


with open("inputs/day5.txt") as f:
    seedLine = f.readline()
    seeds = [int(x) for x in seedLine.split(" ") if x != "seeds:"]
    # split seeds into pairs of 2
    seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]

    f.readline()
    maps = []
    line = []
    for x in f:
        if x == "\n":
            maps.append(line)
            line = []
        else:
            if ("map:" not in x):
                line.append(x.strip())
    if line:
        maps.append(line)


    maps = [[[int(y) for y in x.split(" ")] for x in line] for line in maps]

    # Maps is now a 3d array of all the different maps,
    # maps[x] specifies the map i.e. seed-to-soil map
    # maps[x][y] specifies the line of the map which has the destination, source and range
    # maps[x][y][z] specifies the destination, source or range

    lowest = 0
    for pair in seeds:
        pprint("PAIR: " + str(pair[0]))
        print(pair)
        for i in range(pair[0], pair[0]+pair[1]):
            seed = i
            val=seed
            for map in maps:
                for line in map:
                    if (line[1] <= val <= line[1] + line[2]):
                        val = line[0] + val - line[1]
                        break
            if (val < lowest or lowest == 0):
                lowest = val
    print(lowest)
    print("--- %s seconds ---" % (time.time() - start_time))


# Write a for loop from 28 to 928.
