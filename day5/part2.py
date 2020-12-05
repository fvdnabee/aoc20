import numpy as np

with open('input') as fp:
    tickets = [line[:-1] for line in fp.readlines()]


def bin_part(part, k, j):
    expon = len(part) - 1
    r = 0
    for p in part:
        r += int(p == k) * 2 ** expon
        expon -= 1

    return r


seat_ids = []
for t in tickets:
    row = bin_part(t[:-3], 'B', 'F')
    column = bin_part(t[-3:], 'R', 'L')
    seat_id = row * 8 + column
    seat_ids.append(seat_id)

seat_ids = sorted(seat_ids)
idx = np.argmax(np.diff(seat_ids) == 2)
print(seat_ids[idx], seat_ids[idx+1], seat_ids[idx] + 1)
