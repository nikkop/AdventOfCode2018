import re

def create_patch(data):
    values = re.findall(r"[0-9]+", data.strip())
    keys = list(['id', 'x', 'y', 'w', 'h'])
    patch = dict(zip(keys, [int(val) for val in values]))
    return patch 

def is_unique(patch, grid):
    for x in range(patch.get('x'), patch.get('x') + patch.get('w')):
        for y in range(patch.get('y'), patch.get('y') + patch.get('h')):
            if grid[x][y] > 1:
                return False
    return True

def create_grid(width, height):
    grid = list()
    for x in range(width):
        grid.append(list())
        for y in range(height):
            grid[x].append(0)
    return grid

with open('input.txt') as input:
    patches = [create_patch(patch) for patch in input]

    width = max(set(patch.get('x') + patch.get('w') for patch in patches))
    height = max(set(patch.get('y') + patch.get('h') for patch in patches))
    grid = create_grid(width, height)
    
    for patch in patches:
        for x in range(patch.get('x'), patch.get('x') + patch.get('w')):
            for y in range(patch.get('y'), patch.get('y') + patch.get('h')):
                grid[x][y] += 1

    result = next(patch for patch in patches if is_unique(patch, grid))
    print(result)