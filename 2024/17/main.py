import re

with open("17/input.txt") as file:
    puzzle = file.readlines()

regA = int(re.findall(r"Register A: (\d+)",puzzle[0])[0])
regB = int(re.findall(r"Register B: (\d+)",puzzle[1])[0])
regC = int(re.findall(r"Register C: (\d+)",puzzle[2])[0])
reg = [regA,regB,regC]
commands = [int(m) for m in re.findall(r"Program: ([\d,]+)", puzzle[4])[0].split(',')]
output = []

pointer = 0

while pointer < len(commands):
    instruction = commands[pointer]
    operand = commands[pointer+1]
    combo = operand
    if combo > 3:
        combo = reg[combo-4]

    # adv
    if instruction == 0:
        reg[0] = int(reg[0]//(2**combo))
    # bxl
    elif instruction == 1:
        reg[1] = reg[1] ^ operand
    # bst
    elif instruction == 2:
        reg[1] = combo % 8
    # jnz
    elif instruction == 3:
        if reg[0] != 0:
            pointer = operand-2
    # bxc
    elif instruction == 4:
        reg[1] = reg[1] ^ reg[2]
    # out
    elif instruction == 5:
        output.append(combo % 8)
    # bdv
    elif instruction == 6:
        reg[1] = int(reg[0]/(2**combo))
    # cdv
    elif instruction == 7:
        reg[2] = int(reg[0]/(2**combo))
    else:
        print("Error, instruction not found:", instruction)

    pointer += 2

strOut = ""
for out in output:
    strOut += str(out) + ','
print(strOut)