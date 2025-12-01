import re
import math
from pathlib import Path

dial = 50
code = 0
code2 = 0
currentZero = False
lastZero = False

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "01_data.txt") as file:
    lines = file.readlines()

for line in lines:
    command = re.findall(r"([LR])(\d+)",line)
    direction = command[0][0]
    amount = int(command[0][1])
    if direction == "L":
        dial = dial-amount
    else:
        dial = dial+amount
    
    if dial%100 == 0:
        code += 1
        currentZero = True

    
    if amount >= 100:
        fullRotations = math.floor(amount/100)
        code2 += fullRotations
        if direction == "L":
            dial += fullRotations * 100
        else:
            dial -= fullRotations * 100


    if dial != dial%100 or dial == 0:
        code2 += 1

        if direction == "L" and lastZero:
            code2 -= 1
        
    if lastZero:
        lastZero = False
    
    if currentZero:
        lastZero = True
        currentZero = False

    dial %= 100
    
print(code, code2)