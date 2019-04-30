import re

def manhattan_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])

with open('input.txt') as input:
    bots = [list(map(int, re.findall(r"(-?\d+)", x))) for x in input.readlines()]
    strongest = max(bots, key=lambda x:x[3])

    bots_in_range = [bot for bot in bots if manhattan_dist(bot, strongest) <= strongest[3]] 
    result = len(bots_in_range)
    print(result)