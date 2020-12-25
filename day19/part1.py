import re

text_rules, messages = open('input').read().split('\n\n')

rules = {}
for rule in text_rules.split('\n'):
    rule_n, rule_cond = rule.split(':')
    rules[int(rule_n)] = rule_cond.strip()

# All numbers must be surrounded by spaces, so that we don't substitute
# individual digits, e.g. subs ' 88 ' by ' rules[88] ' but not by ' rules[8]rules[8] '
rules[0] = f" {rules[0]} "
while re.search('[0-9]', rules[0]):
    rule_cond = rules[0]
    pieces = rule_cond.split(" ")
    for p in set(pieces):
        try:
            n = int(p)
        except:
            continue

        rule_cond = re.sub(f" {p} ", f" ( {rules[n]} ) ", rule_cond)

    rules[0] = rule_cond

rules[0] = re.sub("\"", "", rules[0])
rules[0] = re.sub(" ", "", rules[0])

n_matches_0 = 0
pat = re.compile(f"^{rules[0]}$")
for m in messages.split('\n'):
    if re.match(pat, m):
        n_matches_0 += 1

print(n_matches_0)
