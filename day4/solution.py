import re
from functools import partial


def valid_range(lo, hi, token):
    return token.isnumeric() and lo <= int(token) <= hi


def valid_hgt(token):
    _, num, unit = re.split(r'(\d+)', token)
    return (unit == 'in' and valid_range(59, 76, num) or
            unit == 'cm' and valid_range(150, 193, num))


ecl_options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

keys = {
    'byr': partial(valid_range, 1920, 2002),
    'iyr': partial(valid_range, 2010, 2020),
    'eyr': partial(valid_range, 2020, 2030),
    'hgt': valid_hgt,
    'hcl': partial(re.fullmatch, '#[a-f0-9]{6}'),
    'ecl': lambda token: token in ecl_options,
    'pid': partial(re.fullmatch, '[0-9]{9}'),
}

with open('../input/2020/day4.txt') as f: content = f.read()
entries = content.split("\n\n")
valid = new_valid = 0

for entry in entries:
    tokens = dict(x.split(":") for x in entry.replace("\n", " ").split())

    all_keys = all_valid = True
    for key, validator in keys.items():
        all_keys &= key in tokens.keys()
        all_valid &= all_keys and bool(validator(tokens[key]))

    valid += int(all_keys)
    new_valid += int(all_keys and all_valid)

print(f"{valid}\n{new_valid}")
