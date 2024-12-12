with open("06/input.txt") as file:
    labMap = file.readlines()

posX = -1
posY = -1
direction = 8 #8 up, 6 right, 2 down, 4 left
maxHeight = len(labMap)
maxWidth = len(labMap[0])-1

positions = []
for height in range(maxHeight):
    row = []
    for width in range(maxWidth):
        if labMap[height][width] == '^':
            row.append(True)
            posX = width
            posY = height
        else:
            row.append(False)
    positions.append(row)

while posX in range(maxWidth) and posY in range(maxHeight):
    if direction == 4:
        if posX > 0:
            if labMap[posY][posX-1] == '#':
                direction = 8
                continue
            else:
                positions[posY][posX-1] = True
        posX -= 1
    elif direction == 2:
        if posY < maxWidth-1:
            if labMap[posY+1][posX] == '#':
                direction = 4
                continue
            else:
                positions[posY+1][posX] = True
        posY += 1
    elif direction == 6:
        if posX < maxHeight-1:
            if labMap[posY][posX+1] == '#':
                direction = 2
                continue
            else:
                positions[posY][posX+1] = True
        posX += 1
    elif direction == 8:
        if posY > 0:
            if labMap[posY-1][posX] == '#':
                direction = 6
                continue
            else:
                positions[posY-1][posX] = True
        posY -= 1

result = 0
for height in range(maxHeight):
    for width in range(maxWidth):
        if positions[height][width]:
            result += 1
print(result)