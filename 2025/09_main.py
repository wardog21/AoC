import re
from pathlib import Path
import numpy as np
from matplotlib.path import Path as MathPath

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "09_data.txt") as file:
    lines = file.readlines()

tiles = [[int(i) for i in re.findall(r"(\d+)", line)] for line in lines]

area = set()
for tile in tiles:
    for tile2 in tiles:
        area.add(( (abs(tile[0]-tile2[0])+1) * (abs(tile[1]-tile2[1])+1), tuple(tile), tuple(tile2) ))
area = sorted(area, key=lambda x: x[0], reverse=True)
code = area[0][0]

validTiles = set()
for i in range(len(tiles)):
    if tiles[i][0] == tiles[i-1][0]:
        x = tiles[i][0]
        a = min(tiles[i][1], tiles[i-1][1])
        b = max(tiles[i][1], tiles[i-1][1])
        for y in range(a,b+1):
            validTiles.add((x,y))
    else:
        y = tiles[i][1]
        a = min(tiles[i][0], tiles[i-1][0])
        b = max(tiles[i][0], tiles[i-1][0])
        for x in range(a,b+1):
            validTiles.add((x,y))

path = MathPath(tiles)

for cnt, (value,tile,tile2) in enumerate(area):
    if cnt < 100000:
        continue
    print(cnt,len(area))
    a = (min(tile[0],tile2[0]), min(tile[1],tile2[1]))
    b = (max(tile[0],tile2[0]), max(tile[1],tile2[1]))
    
    checkPoints = set()
    checkPoints2 = set([a,b,(a[0],b[1]),(b[0],a[1])])
    for x in range(a[0], b[0]+1):
        checkPoints.add((x,a[1]))
        checkPoints.add((x,b[1]))
    for y in range(a[1], b[1]+1):
        checkPoints.add((a[0],y))
        checkPoints.add((b[0],y))
    
    checkPoints = list(checkPoints.difference(validTiles))
    checkPoints2 = list(checkPoints2.difference(validTiles))
    
    if len(checkPoints) == 0:
        code2 = value
        break
    elif len(checkPoints2) > 0 and not all(path.contains_points(checkPoints2)):
        continue
    else:
        containedPoints = path.contains_points(checkPoints)
        for i in range(len(containedPoints)):
            if containedPoints[i]:
                validTiles.add(checkPoints[i])
        if all(containedPoints):
            code2 = value
            break

print(code,code2)
