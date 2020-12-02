valid = 0
new_valid = 0

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    low, line = line.split("-")
    line, password = line.split(": ")
    high, letter = line.split()
    if int(low) <= password.count(letter) <= int(high):
        valid += 1
    if (password[int(low)-1] == letter) != (password[int(high)-1] == letter):
        new_valid += 1

print(valid)
print(new_valid)
