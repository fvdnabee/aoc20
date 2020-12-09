import itertools


def calc_sums(preamble):
    return [comb[0] + comb[1] for comb in itertools.combinations(preamble, 2)]


numbers = [int(n) for n in open('input').read()[:-1].split('\n')]
preamble = numbers[:25]
for i in range(25, len(numbers)):
    n = numbers[i]
    if n not in calc_sums(preamble):
        break

    # Update preamble
    preamble.pop(0)
    preamble.append(n)

print(f"number {n} is not a sum of the previous 25 values")

# Solution 1 with loops:
for start in range(len(numbers)):
    for stop in range(start, len(numbers)):
        cont_set = numbers[start:stop]
        if sum(cont_set) == n:
            print("range:", start, stop, "min:", min(cont_set), "max:", max(cont_set), "max + min:", max(cont_set) + min(cont_set), "cont set:", cont_set)

# solution 2 with indexing (appears slower):
for cont_set in [numbers[i:i+j] for i in range(0, len(numbers)) for j in range(1, len(numbers)-i+1)]:
    if sum(cont_set) == n:
        start = numbers.index(cont_set[0])
        stop = start + len(cont_set)
        print("range:", start, stop, "min:", min(cont_set), "max:", max(cont_set), "max + min:", max(cont_set) + min(cont_set), "cont set:", cont_set)
        break
