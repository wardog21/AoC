import sys

with open("16/input.txt") as file:
    puzzle = file.readlines()

maze = []
start = [0,0]
end = [0,0]

sys.setrecursionlimit(1000000)
def walkNext(currentPoints, y, x, r):
    oldY = y
    oldX = x
    if r == 8:
        oldY += 1
    elif r == 6:
        oldX -= 1
    elif r == 2:
        oldY -= 1
    elif r == 4:
        oldX += 1

    if maze[y][x][0] == -2:
        return
    elif maze[y][x][0] == -1 or (maze[y][x][0] >= currentPoints and maze[y][x][0] >= 0):
        maze[y][x][0] = currentPoints
        maze[y][x][1] = oldY
        maze[y][x][2] = oldX
        maze[y][x][3] = r

        if r == 8:
            walkNext(currentPoints+1,y-1,x,8)
            walkNext(currentPoints+1001,y,x+1,6)
            walkNext(currentPoints+1001,y,x-1,4)
        elif r == 6:
            walkNext(currentPoints+1001,y-1,x,8)
            walkNext(currentPoints+1,y,x+1,6)
            walkNext(currentPoints+1001,y+1,x,2)
        elif r == 2:
            walkNext(currentPoints+1001,y,x+1,6)
            walkNext(currentPoints+1,y+1,x,2)
            walkNext(currentPoints+1001,y,x-1,4)
        elif r == 4:
            walkNext(currentPoints+1001,y-1,x,8)
            walkNext(currentPoints+1001,y+1,x,2)
            walkNext(currentPoints+1,y,x-1,4)

for ii in range(len(puzzle)):
    row = []
    for i in range(len(puzzle[0])-1):
        if puzzle[ii][i] == '.':
            row.append([-1,0,0,0])
        elif puzzle[ii][i] == '#':
            row.append([-2])
        elif puzzle[ii][i] == 'S':
            row.append([0,6,0,0])
            start[0] = ii
            start[1] = i
        elif puzzle[ii][i] == 'E':
            row.append([-1,0,0,0])
            end[0] = ii
            end[1] = i
    maze.append(row)

walkNext(0,start[0],start[1],6)
print(maze[end[0]][end[1]][0])