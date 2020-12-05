import re

def validate_password_pol1(password, ll, up, char):
    return int(ll) <= password.count(char) <= int(up)

def validate_password_pol2(password, ll, up, char):
    try:
        idx_l = int(ll) - 1
        idx_r = int(up) - 1
        return (password[idx_l] == char) != (password[idx_r] == char)  # XOR
    except IndexError:
        return False

def validate_line(line, pol):
    p = re.compile(r"(?P<ll>\d+)-(?P<up>\d+) (?P<char>.{1}): (?P<password>\w+)")
    if m := re.match(p, line):
        return pol(m['password'], m['ll'], m['up'], m['char']), m['password']

    return False, None

POL = validate_password_pol1
# POL = validate_password_pol2

r = []
with open('input') as fp:
    for line in fp.readlines():
        valid, password = validate_line(line, pol=POL)
        if valid:
            r.append(password)

print(len(r))
