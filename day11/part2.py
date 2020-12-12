import copy

seats = [list(f".{l}.") for l in open('input').read().splitlines()]
width = len(seats[0])
seats.insert(0, ['.']*width)
seats.append(['.']*width)
width = len(seats[0])
height = len(seats)


print("\n".join(["".join(c) for c in seats]), '\n')

def n_adjacent(seats, i, j):
    n_empty, n_occupied = (0, 0)
    # Check all eight directions:
    for k in range(1, i):
        if seats[i-k][j] == '#':
            n_occupied += 1
            break
            # print('T')
        if seats[i-k][j] == 'L':
            n_empty += 1
            break

    for k in range(1, height-i):
        if seats[i+k][j] == '#':
            n_occupied += 1
            # print('B')
            break
        if seats[i+k][j] == 'L':
            n_empty += 1
            break

    for k in range(1, j):
        if seats[i][j-k] == '#':
            n_occupied += 1
            # print('L')
            break
        if seats[i][j-k] == 'L':
            n_empty += 1
            break

    for k in range(1, width-j):
        if seats[i][j+k] == '#':
            n_occupied += 1
            # print('R')
            break
        if seats[i][j+k] == 'L':
            n_empty += 1
            break

    for k in range(1, max(width, height)):
        if i - k < 0 or j - k < 0:
            continue
        if seats[i-k][j-k] == '#':
            n_occupied += 1
            # print('TL')
            break
        if seats[i-k][j-k] == 'L':
            n_empty += 1
            break

    for k in range(1, max(width, height)):
        if i + k >= height or j - k < 0:
            continue
        if seats[i+k][j-k] == '#':
            n_occupied += 1
            # print('BL')
            break
        if seats[i+k][j-k] == 'L':
            n_empty += 1
            break

    for k in range(1, max(width, height)):
        if i + k >= height or j + k >= width:
            continue
        if seats[i+k][j+k] == '#':
            n_occupied += 1
            # print('BR')
            break
        if seats[i+k][j+k] == 'L':
            n_empty += 1
            break

    for k in range(1,  max(width, height)):
        if i - k < 0 or j + k >= width:
            continue
        if seats[i-k][j+k] == '#':
            n_occupied += 1
            # print('TR')
            break
        if seats[i-k][j+k] == 'L':
            n_empty += 1
            break

    return n_empty, n_occupied

seen_seats = [seats]
while True:
    seats = seen_seats[-1]
    new_seats = copy.deepcopy(seats)

    for i in range(1, len(seats) - 1):
        for j in range(1, width - 1):
            if seats[i][j] == '.':
                continue
            n_empty, n_occupied = n_adjacent(seats, i, j)
            # print(i, j, n_empty, n_occupied)

            if seats[i][j] == 'L' and n_occupied == 0:
                new_seats[i][j] = '#'
            elif seats[i][j] == '#' and n_occupied >= 5:
                new_seats[i][j] = 'L'

    if new_seats in seen_seats:
        break
    print("\n".join(["".join(c) for c in new_seats]), "\n")
    seen_seats.append(new_seats)

print("ANS")
print("".join(["".join(c) for c in seen_seats[-1]]).count('#'))
