with open("../input/2020/day3.txt") as f:
    lines = f.read().splitlines()

count = 0

count_r1d1 = 0
count_r5d1 = 0
count_r7d1 = 0
count_r1d2 = 0

for coord, line in enumerate(lines):
    ll = len(line)
    if line[coord % ll] == '#':
        count_r1d1 += 1
    if coord % 2 == 0 and line[int(coord/2) % ll] == '#':
        count_r1d2 += 1
    if line[coord*3 % ll] == '#':
        count += 1
    if line[coord*5 % ll] == '#':
        count_r5d1 += 1
    if line[coord*7 % ll] == '#':
        count_r7d1 += 1

print(count)
print(count*count_r1d1*count_r1d2*count_r5d1*count_r7d1)