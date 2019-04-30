import math

def get_power_level(x, y, sn):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += sn
    power_level *= rack_id
    power_level = math.floor(power_level / 100) % 10
    power_level -= 5
    return power_level

with open('input.txt') as input:
    serial_number = int(input.read())
    grid_size = 300 
    square_size = 3

    most_power = 0
    cell = None
    size = 0

    cells = [get_power_level(x, y, serial_number) for x in range(1, grid_size+1) for y in range(1, grid_size+1)]

    for s in range(1, grid_size + 1):
        print(s)
        cut_cells = [cell for i, cell in enumerate(cells) if i % grid_size <= grid_size - s and math.floor(i / grid_size) <= grid_size - s]
        for c, cell in enumerate(cut_cells):
            square = list()
            for i in range(3):
                for j in range(3):
                    index = c + j + (grid_size * i)
            power_sum = sum(square)
            if power_sum > most_power:
                most_power = power_sum

    print(cell, most_power, size)