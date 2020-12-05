import re
MANDATORY_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def validate_height(p):
    try:
        number = int(p['hgt'][:-2])
    except ValueError:
        return False
    unit = p['hgt'][-2:]

    try:
        limits = {'cm': (150, 193), 'in': (59, 76)}
        return limits[unit][0] <= number and number <= limits[unit][1]
    except KeyError:
        return False


def validate_fields(p):
    r = []
    r.append(1920 <= int(p['byr']) and int(p['byr']) <= 2002)
    r.append(2010 <= int(p['iyr']) and int(p['iyr']) <= 2020)
    r.append(2020 <= int(p['eyr']) and int(p['eyr']) <= 2030)

    p_hcl = re.compile(r'#[0-9a-z]{6}')
    r.append(re.match(p_hcl, p['hcl']))

    r.append(validate_height(p))
    r.append(p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    r.append(len(p['pid']) == 9)

    return all(r)


def validate_passport(lines):
    line = " ".join(lines)
    passport = {}
    for item in line.split(' '):
        key, value = item.split(':')
        passport[key] = value

    valid_passport = all([field in list(passport.keys()) for field in MANDATORY_FIELDS])
    if valid_passport:
        valid_passport *= validate_fields(passport)

    return valid_passport


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
