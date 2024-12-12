with open("12/input.txt") as file:
    gardenPlot = file.readlines()

garden = []
for y in range(len(gardenPlot)):
    row = []
    for x in range(len(gardenPlot[0])-1):
        row.append(True)
    garden.append(row)

def checkRegion(y,x):
    retArea = 1
    retPerimeter = 0
    garden[y][x] = False

    if y > 0:
        if gardenPlot[y][x] == gardenPlot[y-1][x]:
            if garden[y-1][x]:
                area, perimeter = checkRegion(y-1,x)
                retArea += area
                retPerimeter += perimeter
        else:
            retPerimeter += 1
    else:
        retPerimeter += 1
    if x > 0:
        if gardenPlot[y][x] == gardenPlot[y][x-1]:
            if garden[y][x-1]:
                area, perimeter = checkRegion(y,x-1)
                retArea += area
                retPerimeter += perimeter
        else:
            retPerimeter += 1
    else:
        retPerimeter += 1
    if y < len(gardenPlot[0])-2:
        if gardenPlot[y][x] == gardenPlot[y+1][x]:
            if garden[y+1][x]:
                area, perimeter = checkRegion(y+1,x)
                retArea += area
                retPerimeter += perimeter
        else:
            retPerimeter += 1
    else:
        retPerimeter += 1
    if x < len(gardenPlot)-1:
        if gardenPlot[y][x] == gardenPlot[y][x+1]:
            if garden[y][x+1]:
                area, perimeter = checkRegion(y,x+1)
                retArea += area
                retPerimeter += perimeter
        else:
            retPerimeter += 1
    else:
        retPerimeter += 1

    return retArea, retPerimeter

result = 0
for y in range(len(gardenPlot)):
    for x in range(len(gardenPlot[0])-1):
        if garden[y][x]:
            area, perimeter = checkRegion(y,x)
            result += area * perimeter
print(result)