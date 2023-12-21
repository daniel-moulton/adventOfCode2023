import re

print("Part 1")

total=0
maxReds = 12
maxGreens = 13
maxBlues = 14

with open("Inputs/day2.txt") as f:
    lines = f.readlines()
    id=1
    total=0
    for line in lines:
        validLine = True
        x = re.findall("(\d+) (red|green|blue)", line)
        for i in x:
            colourLimit=-1
            match i[1]:
                case "red":
                    colourLimit = maxReds
                case "green":
                    colourLimit = maxGreens
                case "blue":
                    colourLimit = maxBlues
            if int(i[0]) > colourLimit:
                validLine = False
                break
        if validLine:
            total+=id
        id+=1
    print(total)
                    

print("Part 2")




with open("Inputs/day2.txt") as f:
    lines = f.readlines()
    total=0
    for line in lines:
        maxBlues = maxGreens = maxReds = -1
        x = re.findall("(\d+) (red|green|blue)", line)
        for i in x:
            match i[1]:
                case "red":
                    if int(i[0]) > maxReds:
                        maxReds = int(i[0])
                case "green":
                    if int(i[0]) > maxGreens:
                        maxGreens = int(i[0])
                case "blue":
                    if int(i[0]) > maxBlues:
                        maxBlues = int(i[0])
        total+=maxReds*maxGreens*maxBlues
    print(total)
                    