import re
from pathlib import Path
import numpy as np

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "08_data.txt") as file:
    lines = file.readlines()

boxes = [[int(i) for i in re.findall(r"(\d+)", line)] for line in lines]

distances = set()

for id,box in enumerate(boxes):
    for id2,box2 in enumerate(boxes):
        if id != id2:
            distances.add((min(id,id2),max(id,id2),((box[0]-box2[0])**2+(box[1]-box2[1])**2+(box[2]-box2[2])**2)**0.5))

distances = list(distances)
distances = sorted(distances, key=lambda x: x[2])

numbersInGroups = set()
groups = []

for cnt, cConnection in enumerate(distances):
    
    if cConnection[0] in numbersInGroups:
        if cConnection[1] in numbersInGroups:
            id0, id1 = -1,-1
            for id,group in enumerate(groups):
                if cConnection[0] in group:
                    id0 = id
                elif cConnection[1] in group:
                    id1 = id
                if id0 >= 0 and id1 >= 0:
                    break
            if id0 >= 0 and id1 >= 0:
                groups[id0].update(groups[id1])
                groups.pop(id1)
            
        else:
            for group in groups:
                if cConnection[0] in group:
                    group.add(cConnection[1])
                    break
        
    elif cConnection[1] in numbersInGroups:
        for group in groups:
            if cConnection[1] in group:
                group.add(cConnection[0])
                break
    
    else:
        groups.append({cConnection[0],cConnection[1]})
    
    numbersInGroups.add(cConnection[0])
    numbersInGroups.add(cConnection[1])

    # if cnt == 9:
    if cnt == 999:
        groups = sorted(groups, key=lambda x: len(x), reverse=True)
        code = len(groups[0])*len(groups[1])*len(groups[2])
    
    if len(boxes) == len(numbersInGroups) and len(groups) == 1:
        code2 = boxes[cConnection[0]][0]*boxes[cConnection[1]][0]
        break

print(code, code2)