import math

nav = open('input').read().splitlines()
print(nav)

x, y = (0, 0)  # x (east-west), y (north, south)
w_x, w_y = (10, 1)
angle = 0
for instr in nav:
    t, n = (instr[0], int(instr[1:]))

    if t in ['N', 'S']:
        w_y += n if t == 'N' else -n
    elif t in ['E', 'W']:
        w_x += n if t == 'E' else -n
    elif t in ['F']:
        x += n * w_x
        y += n * w_y
    elif t in ['L', 'R']:
        angle = n if t == 'L' else -n
        angle *= math.pi/180
        w_x, w_y = (round(w_x * math.cos(angle) - w_y * math.sin(angle)), round(w_x * math.sin(angle) + w_y * math.cos(angle)))

    print(instr, w_x, w_y, x, y)

print(x, y, abs(x) + abs(y))
