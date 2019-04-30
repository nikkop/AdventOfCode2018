import re
import math
import time

def get_aabb(vectors):
    min_x = min(vectors, key=lambda v:v['x'])['x']
    min_y = min(vectors, key=lambda v:v['y'])['y']
    max_x = max(vectors, key=lambda v:v['x'])['x']
    max_y = max(vectors, key=lambda v:v['y'])['y']
    return (min_x, min_y, max_x, max_y)

def get_center(vectors):
    min_x, min_y, max_x, max_y = get_aabb(vectors)
    center = dict({
        'x': (min_x + max_x) / 2,
        'y': (min_y + max_y) / 2
    })
    return center 

def get_avg_dist(vectors):
    center = get_center(vectors)
    distances = [get_dist(point, center) for point in vectors]
    return sum(distances) / len(distances)

def get_dist(p1, p2):
    return math.sqrt((p2['x'] - p1['x'])**2 + (p2['y'] - p1['y'])**2)

def visualize_heaven(vectors):
    min_x, min_y, max_x, max_y = get_aabb(vectors)
    vectors = [(v['x'], v['y']) for v in vectors]
    for y in range(min_y, max_y+1):
        row = list()
        for x in range(min_x, max_x+1):
            if (x,y) in vectors:
                row.append('#')
            else:
                row.append('.')
        print(row)

with open('input.txt') as input:
    vertices = [tuple(map(int, re.findall(r"-?\d+", vertex))) for vertex in input.readlines()]

    vectors = list()
    for x,y,vx,vy in vertices:
        vector = dict({'x': x,'y': y,'vx': vx,'vy': vy})
        vectors.append(vector)
    
    start = time.time()
    index = 0
    while True:
        index += 1
        prev_dist = get_avg_dist(vectors)
        for v in vectors:
            v['x'] += v['vx']
            v['y'] += v['vy']
        if get_avg_dist(vectors) > prev_dist:
            for v in vectors:
                v['x'] -= v['vx']
                v['y'] -= v['vy']
            break
    end = time.time()
    
    visualize_heaven(vectors)
    print(index)
    print(end-start)