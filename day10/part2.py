adapters = sorted([int(n) for n in open('input').read()[:-1].split('\n')])
adapters.insert(0, 0)
adapters.append(max(adapters) + 3)

adapters = [0, 1, 2, 5]
print(adapters)

def find_combinations(idx, combo, remainder):
    print(idx, combo, remainder)
    if len(remainder) == 1:
        return combo + adapters[-1:]

    combos = []
    for i in range(idx + 1, min(idx+4, len(adapters) - 1)):
        if adapters[i] - combo[-1] < 4:
            combos.append(find_combinations(i, combo + [adapters[i]], adapters[i+1:]))

    return combos

print(find_combinations(0, adapters[0:1], adapters[1:]))
