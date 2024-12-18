import re
import sys
sys.setrecursionlimit(100000)

size = 71
fallenBytes = 1024

with open("18/input.txt") as file:
    puzzle = file.readlines()

grid = []
for ii in range(size):
    row = []
    for i in range(size):
        row.append(-1)
    grid.append(row)

for i in range(fallenBytes):
    x,y = [int(m) for m in re.findall(r"(\d+),(\d+)", puzzle[i])[0]]
    grid[y][x] = -2

def countSteps(y,x,steps):
    if y < 0 or x < 0 or y >= size or x >= size:
        return
    elif grid[y][x] == -2 or (grid[y][x] <= steps and grid[y][x] >= 0):
        return
    else:
        grid[y][x] = steps
        countSteps(y-1,x,steps+1)
        countSteps(y+1,x,steps+1)
        countSteps(y,x-1,steps+1)
        countSteps(y,x+1,steps+1)

countSteps(0,0,0)
print(grid[size-1][size-1])