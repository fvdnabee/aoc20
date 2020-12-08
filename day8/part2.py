instructions = open('input').read().split('\n')[:-1]

for n_nop_jmp in range(1, len(instructions) + 1):
    acc, pcs = (0, [0])  # keep a list of visited program counters

    while pcs.count(pcs[-1]) == 1:
        code, op = instructions[pcs[-1]].split(' ')
        if len(pcs) == n_nop_jmp and code in ['nop', 'jmp']:
            code = 'nop' if code == 'jmp' else 'jmp'  # switch instruction

        pc_incr = 1

        if code == 'acc':
            acc += int(op)
        elif code == 'jmp':
            pc_incr = int(op)

        pcs.append(pcs[-1] + pc_incr)  # Update program counter

        if pcs[-1] + pc_incr == len(instructions):  # program exits gracefully
            print('gracefull exit', acc)
            break
