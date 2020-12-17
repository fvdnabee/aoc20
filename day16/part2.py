import itertools
from collections import defaultdict

inp = open('input').read().split('\n\n')

rules = inp[0].split('\n')
my_ticket = inp[1].split('\n')[1]
other_tickets = inp[2][:-1].split('\n')[1:]

def process_rule(valid_numbers_set, valid_numbers_field, f, r_range):
    min, max = [int(i) for i in r_range.split('-')]
    l = list(range(min, max+1))
    valid_numbers_set.update(l)
    valid_numbers_field[f].update(l)

valid_numbers = set()
valid_numbers_per_field = defaultdict(set)
for r in rules:
    rule_field, rule_rules = r.split(':')
    r1, r2 = rule_rules.split(' or ')
    process_rule(valid_numbers, valid_numbers_per_field, rule_field, r1)
    process_rule(valid_numbers, valid_numbers_per_field, rule_field, r2)


# First tabulate all the numbers per field
numbers_per_field = defaultdict(list)
for t in other_tickets:
    ticket_numbers = [int(n) for n in t.split(',')]
    valid_ticket = all([i in valid_numbers for i in ticket_numbers])
    if valid_ticket:
        for field_idx, n in enumerate(ticket_numbers):
            numbers_per_field[field_idx].append(n)

# Now for every field, check which of the rules it matches:
candidate_fields = defaultdict(list)
for field_idx, field_numbers in numbers_per_field.items():
    for field, field_valid_numbers in valid_numbers_per_field.items():
        if all([n in field_valid_numbers for n in field_numbers]):
            candidate_fields[field_idx].append(field)

# As a field may match more than one rule, eliminate rules starting from the
# rule that was only matched once. When a rule is matched only once, we know
# which field it is for
fields = {}
for i in range(20):
    for field_idx in candidate_fields:
        v = candidate_fields[field_idx]
        if len(v) == 1:
            found_rule = v[0]
            print(f"Field {field_idx} matches rules for {found_rule}")
            fields[found_rule] = field_idx
            for k in candidate_fields:
                try:
                    candidate_fields[k].remove(found_rule)
                except ValueError:
                    pass
            continue

# Finally, process my ticket:
my_ticket = [int(n) for n in my_ticket.split(',')]
prod_departure_fields = 1
for rule_key, field_idx in fields.items():
    if rule_key.startswith('departure'):
        prod_departure_fields *= my_ticket[field_idx]

print(prod_departure_fields)
