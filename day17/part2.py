inp = open('input').read().splitlines()

active_cubes = {}
for y, row in enumerate(inp):
    for x, cube in enumerate(row):
        if cube == '#':
            active_cubes[x, y, 0, 0] = '#'
cubes_epochs = [active_cubes]

print(active_cubes)

# Start simulating cycles:
for epoch in range(6):
    active_cubes = cubes_epochs[epoch]
    new_active_cubes = {}

    # Determine over which coords we should iterate this epoch
    coords_epoch = set()
    for coord in active_cubes:
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        coords_epoch.add((coord[0]+i, coord[1]+j, coord[2]+k, coord[3]+l))

    # Now visit all these coords:
    for coord in coords_epoch:
        cube = active_cubes.get(coord, '.')
        # Consider neighbours of cube:
        n_neighbours_active = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (i, j, k, l) == (0, 0, 0, 0):
                            continue

                        neighbour = active_cubes.get((coord[0]+i, coord[1]+j, coord[2]+k, coord[3]+l), '.')
                        if neighbour == '#':
                            n_neighbours_active += 1

        # print(coord, cube, n_neighbours_active)
        if cube == '.' and n_neighbours_active in [3]:
            new_active_cubes[coord] = '#'
        elif cube == '#' and n_neighbours_active in [2, 3]:
            new_active_cubes[coord] = '#'

    cubes_epochs.append(new_active_cubes)

print(len(cubes_epochs[-1]))
