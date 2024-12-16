import sys

with open("16/input.txt") as file:
    puzzle = file.readlines()

maze = []
start = [0,0]
end = [0,0]
tiles = []

sys.setrecursionlimit(1000000)
def walkNext(currentPoints, y, x, r):
    if maze[y][x][0] == -2:
        return
    elif maze[y][x][r] == -1 or (maze[y][x][r] > currentPoints and maze[y][x][r] >= 0):
        maze[y][x][r] = currentPoints

        if r == 0:
            walkNext(currentPoints+1,y-1,x,r)
        elif r == 1:
            walkNext(currentPoints+1,y,x+1,r)
        elif r == 2:
            walkNext(currentPoints+1,y+1,x,r)
        elif r == 3:
            walkNext(currentPoints+1,y,x-1,r)

        walkNext(currentPoints+1000,y,x,(r+1)%4)
        walkNext(currentPoints+1000,y,x,(r+3)%4)

def checkTiles(points, y, x):
    if maze[y][x][0] == -2:
        return
    elif min(maze[y][x]) == 0 and (y,x) not in tiles:
        tiles.append((y,x))
        return
    elif (y,x) not in tiles:
        # fix to remove an unnecessary loop
        found = False
        if maze[y][x][0] < points:
            checkTiles(maze[y][x][0],y+1,x)
            found = True
        if maze[y][x][1] < points:
            checkTiles(maze[y][x][1],y,x-1)
            found = True
        if maze[y][x][2] < points:
            checkTiles(maze[y][x][2],y-1,x)
            found = True
        if maze[y][x][3] < points:
            checkTiles(maze[y][x][3],y,x+1)
            found = True
        if found:
            tiles.append((y,x))

for ii in range(len(puzzle)):
    row = []
    for i in range(len(puzzle[0])-1):
        if puzzle[ii][i] == '.':
            row.append([-1,-1,-1,-1])
        elif puzzle[ii][i] == '#':
            row.append([-2])
        elif puzzle[ii][i] == 'S':
            row.append([-1,-1,-1,-1])
            start[0] = ii
            start[1] = i
        elif puzzle[ii][i] == 'E':
            row.append([-1,-1,-1,-1])
            end[0] = ii
            end[1] = i
    maze.append(row)

walkNext(0,start[0],start[1],1)
print(min(maze[end[0]][end[1]]))
checkTiles(min(maze[end[0]][end[1]])+1,end[0],end[1])
print(len(tiles))

for ii in range(len(maze)):
    for i in range(len(maze[0])):
        maze[ii][i] = '.'

for tile in tiles:
    maze[tile[0]][tile[1]] = '#'

for ii in range(len(maze)):
    myString = ""
    for i in range(len(maze[0])):
        myString += maze[ii][i]
    print(myString)