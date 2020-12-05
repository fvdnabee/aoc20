with open('input') as fp:
    grid = [line[:-1] for line in fp]

grid_width = len(grid[-1])
x, y = (0, 0)
n_trees = 0
while y < len(grid):
    if grid[y][x % grid_width] == '#':
        n_trees += 1
    x += 3
    y += 1

print(n_trees, "trees")
