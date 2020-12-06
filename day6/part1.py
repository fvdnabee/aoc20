counts = list()
with open('input') as fp:
    answers = []
    while line := fp.readline():
        if line == '\n':
            counts += set(answers)
            answers = list()
        else:
            answers += [c for c in line[:-1]]

print(len(counts))
