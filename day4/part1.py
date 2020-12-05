MANDATORY_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def validate_passport(lines):
    line = " ".join(lines)
    passport = {}
    for item in line.split(' '):
        key, value = item.split(':')
        passport[key] = value

    return all([field in list(passport.keys()) for field in MANDATORY_FIELDS])


passports = []
with open('input') as fp:
    passport_lines = []
    while line := fp.readline():
        if line == '\n':
            if p := validate_passport(passport_lines):
                passports.append(p)

            passport_lines.clear()
        else:
            passport_lines.append(line[:-1])

print(len(passports))
