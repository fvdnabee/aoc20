import itertools

with open('input') as fp:
    lines = fp.readlines()

numbers = [int(line[:-1]) for line in lines]
for c in itertools.combinations(numbers, 2):
    n, m = c
    comp = 2020 - n - m
    if comp in numbers:
        print(n, m, comp, n*m*comp)
        break
