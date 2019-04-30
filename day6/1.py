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
            if (i_x, i_y) not in coords:
                dists = [(manhattan_dist((i_x, i_y), coord), coord, i) for i, coord in enumerate(coords)]
                pure_dists = [dist[0] for dist in dists]
                closest = min(dists, key=lambda x:x[0])
                if pure_dists.count(closest[0]) < 2:
                    grid[i_x][i_y] = closest[2]
    
    flat_grid = [item for grid in grid for item in grid]
    all_cells = set([cell for cell in flat_grid if cell != '.'])
    unique_cells = set(all_cells)
    for cell in all_cells:
        x_len, y_len = grid_size
        should_remove = False
        for y in grid[0]:
            print(cell, y)
            if cell == y:
                should_remove = True
        for y in grid[x_len]:
            if cell == y:
                should_remove = True
        for x in grid:
            if x[0] == cell or x[y_len] == cell:
                should_remove = True 

        if should_remove:
            unique_cells.remove(cell)

    print(unique_cells)
    largest_unique_cell = max([flat_grid.count(cell) for cell in unique_cells])
    print(largest_unique_cell)