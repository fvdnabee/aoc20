import re

rules_graph = {}
for rule in open('input').read()[:-1].split('\n'):
    s = rule.split('contain')

    k = s[0][0:s[0].find(' bags '):]
    if k not in rules_graph:
        rules_graph[k] = []

    p = re.compile(r'\s?(?P<num>\d?) (?P<color>\w+ \w+) bags?\.?')
    for content in s[1].split(','):
        m = re.match(p, content)
        if m is not None:
            rules_graph[k].append((m['color'], int(m['num']) if len(m['num']) > 0 else 0))


def travel_graph(r, color):
    if isinstance(color, str) and rules_graph[color][0] == ('no other', 0):
        return r
    else:
        for c in rules_graph[color]:
            r.append(c[0])
            travel_graph(r, c[0])
        return r


traveled_graph = {c: travel_graph([], c) for c in rules_graph.keys()}
print(len(list(filter(lambda k: 'shiny gold' in traveled_graph[k], traveled_graph.keys()))))


def count_bags(color):
    if isinstance(color, str) and rules_graph[color][0] == ('no other', 0):
        return 0
    else:
        r = 0
        for c in rules_graph[color]:
            r += c[1] + c[1]*count_bags(c[0])
        return r


print(count_bags('shiny gold'))
