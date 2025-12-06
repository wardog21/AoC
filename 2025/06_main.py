import re
from pathlib import Path
import numpy as np

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "06_data.txt") as file:
    lines = file.readlines()

operands = []
for cOp in range(len(lines)-1):
    operands.append([int(i) for i in re.findall(r"(\d+)",lines[cOp])])
operators = re.findall(r"[*+]",lines[len(lines)-1])

for cCalc in range(len(operators)):
    temp = operands[0][cCalc]
    for calculations in range(1,len(operands)):
        if operators[cCalc] == '*':
            temp *= operands[calculations][cCalc]
        elif operators[cCalc] == '+':
            temp += operands[calculations][cCalc]
    code += temp

lenOperation = [len(op)-1 for op in re.findall(r"([*+] +)",lines[len(lines)-1])]
lenOperation[-1] += 1

cnt = 0
lNr = len(lines)-1
for op in range(len(operators)):
    numbers = []
    for nr in range(lenOperation[op]):
        temp = ''
        for posNr in range(lNr):
            temp += lines[posNr][cnt]
        numbers.append(int(temp))
        cnt += 1
    
    temp = numbers[0]
    for calculations in range(1,lenOperation[op]):
        if operators[op] == '*':
            temp *= numbers[calculations]
        elif operators[op] == '+':
            temp += numbers[calculations]
    code2 += temp

    cnt += 1

print(code, code2)