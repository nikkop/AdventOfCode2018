def manhattan_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3])

def get_something(i, coords):
    coord = coords[i]
    constellation = [coord]
    for c in coords:
        if c is not coord and (manhattan_dist(coord, c) <= 3 or manhattan_dist(constellation[-1], c) <= 3):
            constellation.append(c)
    return constellation
        
with open('input.txt') as input:
    coords = [list(map(int, c.split(','))) for c in input.readlines()]

    groups = list()
    for i in range(len(coords)):
        group = get_something(i, coords)
        groups.append(group)
    
    for group in groups:
        for x in groups:
            if group is x:
                break
            else:
                in_g = [x in g for g in group]
                if all(in_g):
                    print(group)


    """
    groups = list()
    curr_i = 0
    while not groups or groups[-1][-1] is not coords[-1]:
        group = get_something(curr_i, coords)
        curr_i = coords.index(group[-1]) + 1
        groups.append(group)
    
    constellations = [g for g in groups if len(g) > 1]
    for g in groups:
        print(g)
    """