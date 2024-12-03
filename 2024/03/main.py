import re

with open("input.txt") as input:
    lines = input.readlines()

result = 0

for line in lines:
    pairs = re.findall(r"mul\((\d*),(\d*)\)", line)

    for pair in pairs:
        result += int(pair[0]) * int(pair[1])

print(result)