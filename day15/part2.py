from collections import defaultdict
import tqdm
starting_numbers = [int(n) for n in open('input').read()[:-1].split(',')]
print(starting_numbers)

pos_numbers = defaultdict(list)
for pos in range(1, len(starting_numbers) + 1):
    last_number = starting_numbers[pos-1]

    pos_numbers[last_number].append(pos)  # init empty list

for pos in tqdm.tqdm(range(len(starting_numbers) + 1, 30000001)):
    if last_number in pos_numbers and len(pos_numbers[last_number]) > 1:  # number has been seen before
        last_number = pos_numbers[last_number][-1] - pos_numbers[last_number][-2]
    else:
        last_number = 0

    pos_numbers[last_number].append(pos)

print(len(pos_numbers))
print(last_number)
