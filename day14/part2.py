inp = open('input').read().splitlines()

memory = {}
for l in inp:
    if l.startswith('mask'):
        m = l.split('=')[1].strip()
        print(m)
        and_mask, or_mask = (2**36 - 1, 0)
        floating_positions = [0]
        for idx, b in enumerate(m[::-1]):
            if b == '1':
                or_mask += 2**idx  # flip bit at position idx to one
            elif b == 'X':
                and_mask -= 2**idx  # flip bith at position idx to zero
                new_positions = [item + 2**idx for item in floating_positions]
                floating_positions.extend(new_positions)

    elif l.startswith('mem'):
        addr, value = [int(x.strip()) for x in l.replace('mem[', '').replace(']','').split('=')]
        masked_addr = addr & and_mask
        masked_addr = masked_addr | or_mask
        for fp in floating_positions:
            write_addr = masked_addr + fp
            memory[write_addr] = value
            print(write_addr, value)

print("sum =", sum(memory.values()))
