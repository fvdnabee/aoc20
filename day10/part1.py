adapters = sorted([int(n) for n in open('input').read()[:-1].split('\n')])
adapters.insert(0, 0)
adapters.append(max(adapters) + 3)

joltage_dist = {k: 0 for k in range(5)}
for idx in range(1, len(adapters)):
    joltage_diff = adapters[idx] - adapters[idx-1]
    if joltage_diff > 3:
        raise ValueError(f"Encountered joltage diff > 3: {joltage_diff} for {adapters[idx]} and {adapters[idx-1]} at index {idx}")

    joltage_dist[joltage_diff] += 1
print(joltage_dist[1] * joltage_dist[3])
