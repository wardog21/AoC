import re

width = 101
height = 103

with open("14/input.txt") as file:
    puzzle = file.readlines()

maxGrouping = 0
for step in range(10000):
    if(step % 100 == 0):
        print(step//100, maxGrouping)
        maxGrouping = 0
    groups = []

    for robot in puzzle:
        pX,pY,vX,vY = [int(m) for m in re.findall(r"p\=(\d+),(\d+) v\=(-?\d+),(-?\d+)", robot)[0]]
        x = (pX + step*vX) % width
        y = (pY + step*vY) % height
        
        grouped = False
        for group in groups:
            for rob in group:
                if abs(rob[0]-x) < 3 and abs(rob[1]-y) < 3:
                    group.append((x,y))
                    grouped = True
                    break
            if grouped:
                break
        if not grouped:
            groups.append([(x,y)])

    mergedGroups = []
    for group in groups:
        merged = False
        for robot in group:
            for mGroup in mergedGroups:
                for mRobot in mGroup:
                    if abs(robot[0]-mRobot[0]) < 3 and abs(robot[1]-mRobot[1]) < 3:
                        merged = True
                        break
                if merged:
                    mGroup.extend(group)
                    break
            if merged:
                break
        if not merged:
            mergedGroups.append(group)
            
    maxGrouping = max(maxGrouping, max([len(m) for m in mergedGroups]))

    if max([len(m) for m in mergedGroups]) > 200:
        print(step, maxGrouping)
        image = []
        for i in range(height):
            row = []
            for ii in range(width):
                row.append(' ')
            image.append(row)
        
        for group in mergedGroups:
            for robot in group:
                image[robot[1]][robot[0]] = '+'
        
        for row in image:
            myStr = ""
            for char in row:
                myStr += char
            print(myStr)
        