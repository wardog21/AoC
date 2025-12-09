import re
from pathlib import Path
import numpy as np

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "09_data.txt") as file:
    lines = file.readlines()

tiles = [[int(i) for i in re.findall(r"(\d+)", line)] for line in lines]

area = set()
for tile in tiles:
    for tile2 in tiles:
        area.add((abs(tile[0]-tile2[0])+1) * (abs(tile[1]-tile2[1])+1))
code = max(area)

validTiles = set()
invalidTiles = set()
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

sizeY = max([i[0] for i in validTiles])
sizeX = max([i[1] for i in validTiles])

for y in range(sizeX):
    print(y,sizeX)
    for x in range(sizeY):
        if (x,y) in validTiles:
            continue
        if y == 0 or x == 0 or y == sizeY or x == sizeX:
            invalidTiles.add((x,y))
            continue

        checkedTiles = set()
        checkedTiles.add((x,y))
        # left
        valid = True
        a = x
        b = y
        while True:
            a -= 1
            if (a,b) in validTiles:
                break
            elif (a,b) in invalidTiles:
                valid = False
                break
            checkedTiles.add((a,b))
        
        if not valid:
            invalidTiles.update(checkedTiles)
            continue

        # right
        a = x
        b = y
        while True:
            a += 1
            if (a,b) in validTiles:
                break
            elif (a,b) in invalidTiles:
                valid = False
                break
            checkedTiles.add((a,b))
        
        if not valid:
            invalidTiles.update(checkedTiles)
            continue

        # up
        a = x
        b = y
        while True:
            b -= 1
            if (a,b) in validTiles:
                break
            elif (a,b) in invalidTiles:
                valid = False
                break
            checkedTiles.add((a,b))
        
        if not valid:
            invalidTiles.update(checkedTiles)
            continue

        # down
        a = x
        b = y
        while True:
            b += 1
            if (a,b) in validTiles:
                break
            elif (a,b) in invalidTiles:
                valid = False
                break
            checkedTiles.add((a,b))
        
        if not valid:
            invalidTiles.update(checkedTiles)
            continue
        else:
            validTiles.update(checkedTiles)

area2 = set()
for tile in tiles:
    for tile2 in tiles:
        a = (min(tile[0],tile2[0]), min(tile[1],tile2[1]))
        b = (max(tile[0],tile2[0]), max(tile[1],tile2[1]))
        validArea = True
        for x in range(a[0], b[0]+1):
            for y in range(a[1], b[1]+1):
                if not (x,y) in validTiles:
                    validArea = False
                    break
            if not validArea:
                break
        
        if validArea:
            area2.add((b[0]-a[0]+1) * (b[1]-a[1]+1))

code2 = max(area2)

print(code,code2)
