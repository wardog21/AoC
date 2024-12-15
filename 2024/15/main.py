warehouse = []
movements = []
robot = []

with open("15/input.txt") as file:
    puzzle = file.readlines()

def moveBox(y,x,d,r):
    moved = True

    if warehouse[y][x] == '#':
        return False
    elif warehouse[y][x] == '.' and not r:
        return True
    else:
        moved = False
        if d == '^':
            if moveBox(y-1,x,d,False):
                warehouse[y-1][x] = warehouse[y][x]
                warehouse[y][x] = '.'
                if r:
                    robot[0] = y-1
                    robot[1] = x
                moved = True
        elif d == '<':
            if moveBox(y,x-1,d,False):
                warehouse[y][x-1] = warehouse[y][x]
                warehouse[y][x] = '.'
                if r:
                    robot[0] = y
                    robot[1] = x-1
                moved = True
        elif d == '>':
            if moveBox(y,x+1,d,False):
                warehouse[y][x+1] = warehouse[y][x]
                warehouse[y][x] = '.'
                if r:
                    robot[0] = y
                    robot[1] = x+1
                moved = True
        elif d == 'v':
            if moveBox(y+1,x,d,False):
                warehouse[y+1][x] = warehouse[y][x]
                warehouse[y][x] = '.'
                if r:
                    robot[0] = y+1
                    robot[1] = x
                moved = True
    return moved

for ii,line in enumerate(puzzle):
    if len(movements) == 0 and line[0] != '\n':
        row = []
        for i in range(len(puzzle[0])-1):
            if line[i] == '@':
                robot = [ii,i]
                row.append('@')
            else:
                row.append(line[i])
        warehouse.append(row)
    else:
        movements.append(line)

for sequence in movements:
    for move in sequence:
        if move == '\n':
            continue
        else:
            moveBox(robot[0],robot[1],move,True)

result = 0
for ii in range(len(warehouse)):
    for i in range(len(warehouse[0])-1):
        if warehouse[ii][i] == 'O':
            result += 100*ii+i
print(result)