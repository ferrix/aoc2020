import re

with open('../input/2020/day4.txt') as f:
    content = f.read()

optional_keys = ['cid']

entries = content.split("\n\n")

valid = 0
new_valid = 0


def valid_byr(token):
    if token.isnumeric():
        return 1920 <= int(token) <= 2002
    return False


def valid_iyr(token):
    if token.isnumeric():
        return 2010 <= int(token) <= 2020
    return False


def valid_eyr(token):
    if token.isnumeric():
        return 2020 <= int(token) <= 2030
    return False


def valid_hgt(token):
    _, num, unit = re.split('(\d+)', token)
    if not num.isnumeric() or not unit.isalpha():
        return False
    if unit == 'in':
        return 59 <= int(num) <= 76
    if unit == 'cm':
        return 150 <= int(num) <= 193
    return False


def valid_hcl(token):
    match = re.fullmatch('#[a-f0-9]{6}', token)
    return match


def valid_ecl(token):
    return token in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def valid_pid(token):
    return re.fullmatch('[0-9]{9}', token)


keys = {
    'byr': valid_byr,
    'iyr': valid_iyr,
    'eyr': valid_eyr,
    'hgt': valid_hgt,
    'hcl': valid_hcl,
    'ecl': valid_ecl,
    'pid': valid_pid,
}


for entry in entries:
    entry = entry.replace("\n", " ")
    tokens = dict(x.split(":") for x in entry.split())

    all_keys = True
    all_valid = True
    for key, validator in keys.items():
        if key in tokens.keys():
            if not validator(tokens[key]):
                all_valid = False
                print("invalid:", key, tokens[key])
            else:
                pass
                #print("valid:", key, tokens[key])
        else:
            all_keys = False

    if all_keys:
        valid += 1
    if all_keys and all_valid:
        new_valid += 1

print(valid)
print(new_valid)