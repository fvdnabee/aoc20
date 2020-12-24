inp = open('input').read().splitlines()

def find_parens(expr):
    """From https://stackoverflow.com/a/29992065/170154"""
    parens = {}
    pstack = []

    for i, ch in enumerate(expr):
        if ch == '(':
            pstack.append(i)
        elif ch == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            parens[pstack.pop()] = i

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return parens


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
running_sum = 0
for expr in inp:
    p0, p1 = (0, 0)
    idx, n = (0, len(expr))

    new_expr = expr
    while idx < n:
        c = new_expr[idx]
        if c == '+':
            parens = find_parens(new_expr)
            if new_expr[idx - 2] in numbers:
                p0 = idx - 2
            elif new_expr[idx - 2] == ')':
                p0 = [key for key, value in parens.items() if value == idx - 2][0]

            if new_expr[idx + 2] in numbers:
                p1 = idx + 2
            elif new_expr[idx + 2] == '(':
                p1 = parens[idx + 2]

            new_expr = new_expr[:p0] + '(' + new_expr[p0:]
            new_expr = new_expr[:p1 + 2] + ')' + new_expr[p1 + 2:]

            idx += 2
            n += 2

        idx += 1

    r = eval(new_expr)
    print(expr, "\t\t\t", new_expr, r)
    running_sum += r

print(running_sum)
