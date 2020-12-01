import sys

expenses = {}

with open('input.txt') as f:
    for line in f:
        value = int(line)
        if value in expenses:
            print(value * expenses[value])
            break
        expenses[2020 - value] = value
