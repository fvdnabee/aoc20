inp = open('input').read().splitlines()

def calc_expr(expr):
    r = 0
    expr_length = 0
    idx = 0
    while idx < len(expr):
        c = expr[idx]
        expr_length += 1
        if c == '(':
            sub_expr_r, sub_expr_l = calc_expr(expr[idx+1:])
            if r == 0:
                r = sub_expr_r
            else:
                if op == '*':
                    r *= sub_expr_r
                elif op == '+':
                    r += sub_expr_r
            idx += sub_expr_l
            expr_length += sub_expr_l
            print('subexpr', sub_expr_r, sub_expr_l, r, idx, len(expr))

        elif c == ')':
            print(c, expr_length)
            return r, expr_length
        elif ord(c) in range(ord('0'), ord('9') + 1):  # a number
            n = int(c)
            if r == 0:
                r = n
            else:
                if op == '*':
                    r *= n
                elif op == '+':
                    r += n
            print(idx, r)
        elif c == '*':
            op = '*'
        elif c == '+':
            op = '+'
        idx += 1

    return r


running_sum = 0
for expr in inp:
    r = calc_expr(expr)
    print(expr, r, '\n')
    running_sum += r

print(running_sum)
