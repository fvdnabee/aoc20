counts = list()
with open('input') as fp:
    answers = []
    n_persons = 0
    while line := fp.readline():
        if line == '\n':
            answered_everyone = set(filter(lambda x: answers.count(x) == n_persons, answers))  # set to include only unique answers: e.g. [q,q,q] -> {q}
            counts += answered_everyone
            answers = list()
            n_persons = 0
        else:
            n_persons += 1
            answers += [c for c in line[:-1]]

print(len(counts))
