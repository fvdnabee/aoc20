starting_numbers = [int(n) for n in open('input').read()[:-1].split(',')]
print(starting_numbers)

pos_numbers = {}
for pos in range(1, 2021):
    if pos < len(starting_numbers) + 1:
        last_number = starting_numbers[pos-1]
    else:
        if last_number in pos_numbers and len(pos_numbers[last_number]) > 1:  # number has been seen before
            last_number = pos_numbers[last_number][-1] - pos_numbers[last_number][-2]
        else:
            last_number = 0

    if last_number not in pos_numbers:
        pos_numbers[last_number] = []  # init empty list

    print(last_number)
    pos_numbers[last_number].append(pos)

print(pos_numbers)
