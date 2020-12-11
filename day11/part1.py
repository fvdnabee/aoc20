import copy

seats = [list(f".{l}.") for l in open('input').read().splitlines()]
width = len(seats[0])
seats.insert(0, ['.']*width)
seats.append(['.']*width)

print("\n".join(["".join(c) for c in seats]), '\n')

def n_adjacent(seats, i, j):
    n_empty, n_occupied = (0, 0)
    for k in range(-1, 2):
        for l in range(-1, 2):
            if k == 0 and l == 0:
                continue

            s = seats[i-k][j-l]
            if s in ['L']:
                n_empty += 1
            elif s in ['#']:
                n_occupied += 1

    return n_empty, n_occupied

seen_seats = [seats]
while True:
    seats = seen_seats[-1]
    new_seats = copy.deepcopy(seats)

    for i in range(1, len(seats) - 1):
        for j in range(1, width - 1):
            n_empty, n_occupied = n_adjacent(seats, i, j)

            if seats[i][j] == 'L' and n_occupied == 0:
                new_seats[i][j] = '#'
            elif seats[i][j] == '#' and n_occupied >= 4:
                new_seats[i][j] = 'L'

    if new_seats in seen_seats:
        break
    print("\n".join(["".join(c) for c in new_seats]), "\n")
    seen_seats.append(new_seats)

print("".join(["".join(c) for c in seen_seats[-1]]).count('#'))
