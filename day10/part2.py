adapters = sorted([int(n) for n in open('input').read()[:-1].split('\n')])
adapters.insert(0, 0)
adapters.append(max(adapters) + 3)
adapters = adapters[::-1]

n_paths = {167: 1}
for i in range(1, len(adapters)):
    adap = adapters[i]
    n_jumps = 0
    for j in range(1, min(3, i)+1):
        prev_adap = adapters[i-j]
        if prev_adap - adap < 4:
            n_jumps += 1 * n_paths[prev_adap]

    n_paths[adap] = n_jumps

print(n_paths[0])
