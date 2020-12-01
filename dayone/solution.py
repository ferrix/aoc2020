import sys

expenses = {}

with open('input.txt') as f:
    for line in f:
        value = int(line)
        if value in expenses:
            print(value * expenses[value])
            break
        expenses[2020 - value] = value

del expenses

with open('input.txt') as f:
    lines = [int(line) for line in f]

expenses = {}

for i in range(0, len(lines)-1):
    for j in range(i+1, len(lines)):
        if lines[j] in expenses:
            print(lines[j] * expenses[lines[j]][0] * expenses[lines[j]][1])
            sys.exit(0)
        expenses[2020 - lines[i] - lines[j]] = (lines[i], lines[j])
