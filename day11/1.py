import math

def get_power_level(cell):
    rack_id = cell[0] + 10
    power_level = rack_id * cell[1]
    power_level += serial_number
    power_level *= rack_id
    power_level = math.floor(power_level / 100) % 10
    power_level -= 5
    return power_level

def create_square(c, s):
    return [(i,j) for i in range(c[0],c[0]+s) for j in range(c[1], c[1]+s)] 

with open('input.txt') as input:
    serial_number = int(input.read())

    grid_size = 300 
    grid = [[(j, i) for j in range(1, grid_size+1)] for i in range(1, grid_size+1)]

    largest_power = dict({
        'cell': None,
        'power': 0 
    })

    square_size = 3
    for row in grid:
        for cell in row:
            c = (grid.index(row), row.index(cell))
            if c[1] <= grid_size - square_size + 1 and c[0] <= grid_size - square_size + 1:
                square = list(map(lambda c: grid[c[0]-1][c[1]-1], create_square(c, square_size)))
                power = sum(list(map(get_power_level, square)))
                if power > largest_power['power']:
                    largest_power['cell'] = c
                    largest_power['power'] = power

    print(largest_power)