import re

# width = 11
# height = 7
width = 101
height = 103
seconds = 100

with open("14/input.txt") as file:
    puzzle = file.readlines()

quadrants = [0,0,0,0]

for robot in puzzle:
    pX,pY,vX,vY = [int(m) for m in re.findall(r"p\=(\d+),(\d+) v\=(-?\d+),(-?\d+)", robot)[0]]
    x = (pX + seconds*vX) % width
    y = (pY + seconds*vY) % height
    
    if x != width//2 and y != height//2:
        if x < width//2:
            if y < height//2:
                quadrants[0] += 1
            else:
                quadrants[2] += 1
        else:
            if y < height//2:
                quadrants[1] += 1
            else:
                quadrants[3] += 1

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])