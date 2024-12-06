with open("06/input.txt") as file:
    labMap = file.readlines()

posX = -1
posY = -1
direction = 8 #8 up, 6 right, 2 down, 4 left
maxHeight = len(labMap)
maxWidth = len(labMap[0])-1
result = 0

for x in range(maxHeight):
    print(x, maxHeight)
    for y in range(maxWidth):
        if labMap[y][x] == '#' or labMap[y][x] == '^':
            continue

        positions = []
        for height in range(maxHeight):
            row = []
            for width in range(maxWidth):
                if labMap[height][width] == '^':
                    row.append(8)
                    posX = width
                    posY = height
                    direction = 8
                else:
                    row.append(5)
            positions.append(row)

        while posX in range(maxWidth) and posY in range(maxHeight):
            if direction == 4:
                if posX > 0:
                    if (labMap[posY][posX-1] == '#') or (posY==y and posX-1==x):
                        direction = 8
                        continue
                    elif positions[posY][posX-1] == 4:
                        result += 1
                        break
                    else:
                        positions[posY][posX-1] = 4
                posX -= 1
            elif direction == 2:
                if posY < maxWidth-1:
                    if (labMap[posY+1][posX] == '#') or (posY+1==y and posX==x):
                        direction = 4
                        continue
                    elif positions[posY+1][posX] == 2:
                        result += 1
                        break
                    else:
                        positions[posY+1][posX] = 2
                posY += 1
            elif direction == 6:
                if posX < maxHeight-1:
                    if (labMap[posY][posX+1] == '#') or (posY==y and posX+1==x):
                        direction = 2
                        continue
                    elif positions[posY][posX+1] == 6:
                        result += 1
                        break
                    else:
                        positions[posY][posX+1] = 6
                posX += 1
            elif direction == 8:
                if posY > 0:
                    if (labMap[posY-1][posX] == '#') or (posY-1==y and posX==x):
                        direction = 6
                        continue
                    elif positions[posY-1][posX] == 8:
                        result += 1
                        break
                    else:
                        positions[posY-1][posX] = 8
                posY -= 1

print(result)