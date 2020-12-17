import itertools

inp = open('input').read().split('\n\n')

rules = inp[0].split('\n')
my_ticket = inp[1].split('\n')[1]
other_tickets = inp[2][:-1].split('\n')[1:]

def process_rule(valid_numbers_set, r):
    min, max = [int(i) for i in r.split('-')]
    valid_numbers_set.update(list(range(min, max+1)))

valid_numbers = set()
for r in rules:
    rule_key, rule_rules = r.split(':')
    r1, r2 = rule_rules.split(' or ')
    process_rule(valid_numbers, r1)
    process_rule(valid_numbers, r2)

running_sum_invalid = 0
for t in other_tickets:
    ticket_numbers = [int(n) for n in t.split(',')]
    ticket_numbers_invalid_selectors = [i not in valid_numbers for i in ticket_numbers]
    running_sum_invalid += sum(list(itertools.compress(ticket_numbers, ticket_numbers_invalid_selectors)))

print(running_sum_invalid)
