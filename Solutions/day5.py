from pprint import pprint


'''
Destination     Source      Range
X               Y           Z

Given a seed, S, we want to check if the seed lies between Y and Y+Z, if it does map that to it's corresponding value between X and X+Z
'''
with open("inputs/day5.txt") as f:
    seedLine = f.readline()
    seed = [int(x) for x in seedLine.split(" ") if x != "seeds:"]

    # lines = f.readlines()
    # lines = [x.strip() for x in lines]
    # lines = [x.split(" ") for x in lines]
    # pprint(lines)

    # Read file into a list of lists, each list being separated by an empty 
    f.readline()
    lines = []
    line = []
    for x in f:
        if x == "\n":
            lines.append(line)
            line = []
        else:
            line.append(x.strip())
    pprint(lines[1])