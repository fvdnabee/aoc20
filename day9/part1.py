import itertools


def calc_sums(preamble):
    return [comb[0] + comb[1] for comb in itertools.combinations(preamble, 2)]


def calc_sums_loop(preamble):
    r = []
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            if i > j:
                r.append(preamble[i] + preamble[j])
    return r


assert set(calc_sums(range(25))) == set(calc_sums_loop(range(25)))

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
