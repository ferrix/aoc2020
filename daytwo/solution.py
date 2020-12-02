
test_lines = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

valid = 0

for line in test_lines.splitlines():
    low, line = line.split("-")
    line, password = line.split(": ")
    high, letter = line.split()
    print(low, password.count(letter), int(high))
    if int(low) <= password.count(letter) <= int(high):
        valid += 1

print(valid)
