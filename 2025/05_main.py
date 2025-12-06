import re
from pathlib import Path

code = 0
code2 = 0

freshIngredients = []
ingredients = []

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "05_data.txt") as file:
    while len(line := file.readline().rstrip()) > 0:
        freshIngredients.append([int(i) for i in re.findall(r"(\d+)",line)])
    while len(line := file.readline().rstrip()) > 0:
        ingredients.append(int(line))

for i in ingredients:
    for f in freshIngredients:
        if i >= f[0] and i <= f[1]:
            code += 1
            break

while True:
    changed = False
    for rId, cRange in enumerate(freshIngredients):
        for fId, cFresh in enumerate(freshIngredients):
            if rId == fId: continue
            if cFresh[0] >= cRange[0] and cFresh[0] <= cRange[1]:
                cRange[1] = max(cRange[1], cFresh[1])
                freshIngredients.pop(fId)
                changed = True
                break
            elif cRange[0] >= cFresh[0] and cRange[0] <= cFresh[1]:
                cFresh[1] = max(cRange[1], cFresh[1])
                freshIngredients.pop(rId)
                changed = True
                break
        if changed: break

    if not changed: break

for ranges in freshIngredients:
    code2 += ranges[1] - ranges[0] + 1

print(code, code2)