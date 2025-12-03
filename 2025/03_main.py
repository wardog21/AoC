import re
from pathlib import Path

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "03_data.txt") as file:
    lines = file.readlines()

def getJolts(batteries, amount):
    finalBatteries = []
    while len(finalBatteries) < amount:
        firstHigh = max(batteries[:len(batteries)-amount+1+len(finalBatteries)])
        finalBatteries.append(firstHigh)
        batteries = batteries[batteries.index(firstHigh)+1:]
    return int(''.join(map(str,finalBatteries)))

for line in lines:
    batteries = [int(b) for b in re.findall(r"(\d)",line)]
    code  += getJolts(batteries, 2)
    code2 += getJolts(batteries,12)

print(code, code2)