import re
from pathlib import Path
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
    # print(cnt,value,len(area))
    a = (min(tile[0],tile2[0]), min(tile[1],tile2[1]))
    b = (max(tile[0],tile2[0]), max(tile[1],tile2[1]))
    
    checkPoints = list(set([a,b,(a[0],b[1]),(b[0],a[1])]).difference(validTiles))
    if len(checkPoints) > 0 and not all(path.contains_points(checkPoints)):
        continue

    valid = True
    for i in range(len(tiles)):

        if tiles[i][0] == tiles[i-1][0]:
            if a[0] < tiles[i][0] and b[0] > tiles[i][0] and a[1] < max(tiles[i][1], tiles[i-1][1]) and b[1] > min(tiles[i][1], tiles[i-1][1]):
                valid = False
                break
        elif tiles[i][1] == tiles[i-1][1]:
            if a[1] < tiles[i][1] and b[1] > tiles[i][1] and a[0] < max(tiles[i][0], tiles[i-1][0]) and b[0] > min(tiles[i][0], tiles[i-1][0]):
                valid = False
                break
        
    if valid:
        code2 = value
        break
        
print(code,code2)
