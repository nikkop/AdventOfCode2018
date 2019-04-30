import re

def create_patch(data):
    values = re.findall(r"[0-9]+", data.strip())
    keys = list(['id', 'x', 'y', 'width', 'height'])
    patch = dict(zip(keys, [int(val) for val in values]))
    return patch 

with open('input.txt') as input:
    patches = [create_patch(patch) for patch in input]

    width = max(set(patch.get('x') + patch.get('width') for patch in patches))
    height = max(set(patch.get('y') + patch.get('height') for patch in patches))

    grid = list()
    for x in range(width):
        grid.append(list())
        for y in range(height):
            grid[x].append(0)
    
    for patch in patches:
        for x in range(patch.get('width')):
            for y in range(patch.get('height')):
                grid[patch.get('x') + x][patch.get('y') + y] += 1

    collisions = 0
    for x in grid:
        for y in x:
            if y > 1:
                collisions += 1

    print(collisions)