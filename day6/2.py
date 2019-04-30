def manhattan_dist(c, n):
    return abs(n[0]-c[0]) + abs(n[1]-c[1])

with open('input.txt') as input:
    coords = [tuple(map(int, coord.strip().split(', '))) for coord in input.readlines()]

    grid_size = (max(coords, key=lambda x:x[0])[0], max(coords, key=lambda x:x[1])[1])
    grid = list()

    for x in range(grid_size[0]+1):
        grid.append(list())
        for y in range(grid_size[1]+1):
            grid[x].append('.')
    
    for i, (x,y) in enumerate(coords):
        grid[x][y] = i
    
    for i_x, x in enumerate(grid):
        for i_y, y in enumerate(x):
            dists = [(manhattan_dist((i_x, i_y), coord), coord, i) for i, coord in enumerate(coords)]
            pure_dists = [dist[0] for dist in dists]
            if sum(pure_dists) < 10000:
                grid[i_x][i_y] = '#'
    

    forgotten = 0
    for i_x, x in enumerate(grid):
        for i_y, y in enumerate(x):
            if y != '#' and y != '.':
                if grid[i_x][i_y-1] == '#' and grid[i_x][i_y+1] == '#' and grid[i_x-1][i_y] == '#' and grid[i_x+1][i_y] == '#':
                    forgotten += 1

    flat_grid = [item for grid in grid for item in grid]
    print(flat_grid.count('#') + forgotten)