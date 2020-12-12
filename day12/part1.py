import math

nav = open('input').read().splitlines()
print(nav)

x, y = (0, 0)  # x (east-west), y (north, south)
angle = 0
for instr in nav:
    dx, dy = (0, 0)
    t, n = (instr[0], int(instr[1:]))

    if t in ['N', 'S']:
        dy = n if t == 'N' else -n
    elif t in ['E', 'W']:
        dx = n if t == 'E' else -n
    elif t in ['F']:
        dx = int(n * math.cos(angle/180*math.pi))
        dy = int(n * math.sin(angle/180*math.pi))
    elif t in ['L', 'R']:
        dangle = n if t == 'L' else -n
        angle = (angle + dangle) % 360

    print(x, y, instr, x + dx, y + dy)
    x += dx
    y += dy

print(x, y, abs(x) + abs(y))
