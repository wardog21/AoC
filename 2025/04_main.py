import re
from pathlib import Path
import numpy as np

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "04_data.txt") as file:
    lines = file.readlines()

mY = len(lines)
mX = len(lines[0])-1

input = np.zeros((mY,mX),dtype=bool)
for y in range(mY):
    for x in range(mX):
        input[y,x] = lines[y][x] == '@'

while True:
    cnt = np.zeros((mY,mX),dtype=int)
    
    for y in range(mY):
        for x in range(mX):
            if input[y,x]:
                for b in range(max(0,y-1),min(y+2,mY)):
                    for a in range(max(0,x-1),min(x+2,mX)):
                        cnt[b,a] += 1
                cnt[y,x] -= 1

    for y in range(mY):
        for x in range(mX):
            if not input[y,x]:
                cnt[y,x] = 10

    if code == 0:
        code = (cnt < 4).sum()
    
    removed = (cnt < 4)
    input[removed] = False

    if removed.sum() == 0:
        break

    code2 += removed.sum()


    print(code, code2)