import re

# text_rules, messages = open('sample_input_partB').read().split('\n\n')
text_rules, messages = open('input').read().split('\n\n')

rules = {}
for rule in text_rules.split('\n'):
    rule_n, rule_cond = rule.split(':')
    rules[int(rule_n)] = rule_cond.strip()

# Completely determine all rules:
# All numbers must be surrounded by spaces, so that we don't substitute
# individual digits, e.g. subs ' 88 ' by ' rules[88] ' but not by ' rules[8]rules[8] '
for rule_n in rules:
    rules[rule_n] = f" {rules[rule_n]} "
    while re.search('[0-9]', rules[rule_n]):
        rule_cond = rules[rule_n]
        pieces = rule_cond.split(" ")
        for p in set(pieces):
            try:
                n = int(p)
            except:
                continue

            rule_cond = re.sub(f" {p} ", f" ( {rules[n]} ) ", rule_cond)

        rules[rule_n] = rule_cond

    rules[rule_n] = rules[rule_n].replace('"', '').replace(' ', '')

# Part 1:
# n_matches_0 = 0
# pat = re.compile(f"^{rules[0]}$")
# for m in messages.split('\n'):
#     if re.match(pat, m):
#         print(f"{m} matches")
#         n_matches_0 += 1
# print(n_matches_0)
# exit()

rules[8] = f"({rules[8]})+"

new_rule_11 = f"({rules[42]})({rules[31]})"
print(new_rule_11)
for i in range(2, 10):  # not really infinite repetitions, but suffices
    p1 = f"({rules[42]})"*i
    p2 = f"({rules[31]})"*i
    new_rule_11 = new_rule_11 + "|" + "(" + f"({p1})" + f"({p2})" + ")"

rules[11] = new_rule_11

rules[0] = f"({rules[8]})({rules[11]})"

n_matches_0 = 0
pat = re.compile(f"^{rules[0]}$")
for m in messages.split('\n'):
    if re.match(pat, m):
        print(f"{m} matches")
        n_matches_0 += 1

print(n_matches_0)
