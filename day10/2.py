import re

def get_aabb(vectors):
    min_x = min(vectors, key=lambda v:v['x'])['x']
    min_y = min(vectors, key=lambda v:v['y'])['y']
    max_x = max(vectors, key=lambda v:v['x'])['x']
    max_y = max(vectors, key=lambda v:v['y'])['y']
    return (min_x, min_y, max_x, max_y)

def get_area(vectors):
    min_x, min_y, max_x, max_y = get_aabb(vectors)
    width = max_x - min_x
    height = max_y - min_y
    return width * height

def create_heaven(vectors):
    min_x, min_y, max_x, max_y = get_aabb(vectors)
    vectors = [(v['x'], v['y']) for v in vectors]
    grid = list()
    for y in range(min_y, max_y+1):
        row = list()
        for x in range(min_x, max_x+1):
            if (x,y) in vectors:
                row.append('#')
            else:
                row.append('.')
        grid.append(row)
    return grid

with open('input.txt') as input:
    vertices = [tuple(map(int, re.findall(r"-?\d+", vertex))) for vertex in input.readlines()]

    vectors = [dict({'x':v[0],'y':v[1],'vx': v[2],'vy':v[3]}) for v in vertices]
    
    index = 0
    while True:
        index += 1
        prev_area = get_area(vectors)
        for v in vectors:
            v['x'] += v['vx']
            v['y'] += v['vy']
        if get_area(vectors) > prev_area:
            for v in vectors:
                v['x'] -= v['vx']
                v['y'] -= v['vy']
            break
    
    heaven = create_heaven(vectors)
    for row in heaven:
        print(row)
    print(index)