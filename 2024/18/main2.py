import re
import sys
sys.setrecursionlimit(100000)

size = 71
fallenBytes = 1500
with open("18/input.txt") as file:
    puzzle = file.readlines()

grid = []
for i in range(size):
    row = []
    for ii in range(size):
        row.append(-1)
    grid.append(row)
path = []

for i in range(len(puzzle)):
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

def resetGrid():
    for i in range(size):
        for ii in range(size):
            if grid[i][ii] >= 0:
                grid[i][ii] = -1

for i in range(len(puzzle)-1,fallenBytes,-1):
    countSteps(0,0,0)
    if grid[size-1][size-1] > 0:
        print(puzzle[i+1])
        break
    resetGrid()
    x,y = [int(m) for m in re.findall(r"(\d+),(\d+)", puzzle[i])[0]]
    grid[y][x] = -1