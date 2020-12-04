with open('../input/2020/day4.txt') as f:
    content = f.read()

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_keys = ['cid']

entries = content.split("\n\n")

valid = 0
new_valid = 0

for entry in entries:
    entry = entry.replace("\n", " ")
    tokens = dict(x.split(":") for x in entry.split())

    all_keys = True
    for key in keys:
        if key in tokens.keys():
            continue
        else:
            all_keys = False

    if all_keys:
        valid += 1

print(valid)