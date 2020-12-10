adapters = sorted([int(n) for n in open('input').read()[:-1].split('\n')])
adapters.insert(0, 0)
adapters.append(max(adapters) + 3)
# adapters = [0, 1, 2, 4, 5, 8, 9, 12]
print(adapters)
print(len(adapters))

def find_combinations(idx, combo, remainder):
    if len(remainder) == 1:
        return [combo + adapters[-1:]]  # a list containing a list, so we can pass it to list.extend()

    combos = []
    for i in range(idx + 1, min(idx + 4, len(adapters) - 1)):
        print(i, end='\r')
        if adapters[i] - combo[-1] < 4:
            combos.extend(find_combinations(i, combo + [adapters[i]], adapters[i+1:]))

    return combos

r = find_combinations(0, adapters[0:1], adapters[1:])
print(r)
print(len(r))
