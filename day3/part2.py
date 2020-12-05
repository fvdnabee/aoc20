with open('input') as fp:
    grid = [line[:-1] for line in fp]

grid_width = len(grid[-1])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
slopes_trees = []
slopes_trees_multiplied = 1
for r, l in slopes:
    n_trees = 0
    x, y = (0, 0)
    while y < len(grid):
        if grid[y][x % grid_width] == '#':
            n_trees += 1
        x += r
        y += l

    slopes_trees_multiplied *= n_trees
    slopes_trees.append(n_trees)

print(slopes_trees)
print(slopes_trees_multiplied)
