with open('input') as fp:
    lines = fp.readlines()

numbers = [int(line[:-1]) for line in lines]
for n in numbers:
    comp = 2020 - n
    if comp in numbers:
        print(n, comp, n*comp)
        break
