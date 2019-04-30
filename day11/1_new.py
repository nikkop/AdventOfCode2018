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
    size = 3

    most_power = 0
    cell = None

    index = 0
    for x in range(1, grid_size + 1 - size):
        for y in range(1, grid_size + 1 - size):
            power_cells = (get_power_level(x+i, y+j, serial_number) for i in range(size) for j in range(size))
            power_sum = sum(power_cells)
            if power_sum > most_power:
                most_power = power_sum
                cell = (x,y)
            index += 1
    
    print(index)
    print(cell, most_power, size)