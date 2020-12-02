valid = 0

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    low, line = line.split("-")
    line, password = line.split(": ")
    high, letter = line.split()
    if int(low) <= password.count(letter) <= int(high):
        valid += 1

print(valid)
