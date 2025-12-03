import re
from pathlib import Path

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "03_data.txt") as file:
    lines = file.readlines()

for line in lines:
    batteries = [int(b) for b in re.findall(r"(\d)",line)]
    
    # code
    high = max(batteries)
    posHigh = batteries.index(high)
    if len(batteries) == posHigh+1:
        secHigh = max(batteries[:-1])
        code += 10*secHigh+high
    else:
        secHigh = max(batteries[posHigh+1:])
        code += 10*high+secHigh
    
    # code2
    setPos = 0
    finalBatteries = []
    while len(finalBatteries) < 12:
        firstHigh = max(batteries[:len(batteries)-11+len(finalBatteries)])
        finalBatteries.append(firstHigh)
        batteries = batteries[batteries.index(firstHigh)+1:]
    code2 += int(''.join(map(str,finalBatteries)))

print(code, code2)