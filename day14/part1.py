inp = open('input').read().splitlines()

memory = {}
for l in inp:
    if l.startswith('mask'):
        m = l.split('=')[1].strip()
        print(m)
        and_mask, or_mask = (2**36 - 1, 0)
        for idx, b in enumerate(m[::-1]):
            if b == '1':
                or_mask += 2**idx  # flip bit at position idx to one
            elif b == '0':
                and_mask -= 2**idx  # flip bith at position idx to zero
    elif l.startswith('mem'):
        addr, value = [int(x.strip()) for x in l.replace('mem[', '').replace(']','').split('=')]
        masked_value = value & and_mask
        masked_value = masked_value | or_mask
        print(addr, value)
        memory[addr] = masked_value

print("sum =", sum(memory.values()))
