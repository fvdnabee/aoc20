instructions = open('input').read().split('\n')[:-1]
acc, pcs = (0, [0])  # keep a list of visited program counters

while pcs.count(pcs[-1]) == 1:
    code, op = instructions[pcs[-1]].split(' ')

    pc_incr = 1

    if code == 'acc':
        acc += int(op)
    elif code == 'jmp':
        pc_incr = int(op)

    pcs.append(pcs[-1] + pc_incr)  # Update program counter

print(acc)
