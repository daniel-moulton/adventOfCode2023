from pprint import pprint
from itertools import combinations


with open("Inputs/day11.txt", "r") as file:
    original_map = [list(line.strip()) for line in file.readlines()]
    new_map = []
    for line in original_map:
        new_map.append(line)
        if '#' not in line:
            new_map.append(line)

    transposed_map = list(map(list, zip(*new_map)))
    final_map = []
    for column in transposed_map:
        final_map.append(column)
        if '#' not in column:
            final_map.append(column)
    

coords = []

for i, row in enumerate(final_map):
    for j, cell in enumerate(row):
        if cell == '#':
            coords.append((i, j))

# Calculate Manhattan distance between each pair of coordinates
distances = [abs(x1-x2) + abs(y1-y2) for (x1, y1), (x2, y2) in combinations(coords, 2)]

print(sum(distances))


'''


Part 2


'''


with open("Inputs/day11.txt", "r") as file:
    original_map = [list(line.strip()) for line in file.readlines()]

coords=[]

for i, row in enumerate(original_map):
    for j, cell in enumerate(row):
        if cell == '#':
            coords.append((i, j))

emptyRows = [i for i, row in enumerate(original_map) if '#' not in row]

transposed_map = list(map(list, zip(*original_map)))

emptyCols = [j for j, column in enumerate(transposed_map) if '#' not in column]

distances = []
for (x1, y1), (x2, y2) in combinations(coords, 2):
    distance = abs(x1-x2) + abs(y1-y2)
    for empty_row in emptyRows:
        if min(x1, x2) <= empty_row <= max(x1, x2):
            distance += 999999
    for empty_col in emptyCols:
        if min(y1, y2) <= empty_col <= max(y1, y2):
            distance += 999999
    distances.append(distance)

print(sum(distances))