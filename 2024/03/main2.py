import re

with open("03/input.txt") as input:
    lines = input.readlines()

result = 0
mul_enabled = True

for line in lines:
    commands = re.findall(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", line)

    for command in commands:
        if command == "do()":
            mul_enabled = True
        elif command == "don't()":
            mul_enabled = False
        elif mul_enabled:
            pair = re.findall(r"mul\((\d*),(\d*)\)", command)
            result += int(pair[0][0]) * int(pair[0][1])

print(result)