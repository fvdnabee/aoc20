inp = open('input').read().splitlines()
ts = int(inp[0])
buses = [int(t) for t in inp[1].replace('x,', '').split(',')]

print(ts, buses)
wait_times = []
min_wait_time, min_b = (1e30, -1)
for b in buses:
    wait_time = (-(ts % b)) % b
    print(b, wait_time)

    if wait_time < min_wait_time:
        min_wait_time = wait_time
        min_b = b

print(min_wait_time * min_b)
