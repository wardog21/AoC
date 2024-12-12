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
    retRegion = [(y,x)]
    garden[y][x] = False

    if y > 0:
        if gardenPlot[y][x] == gardenPlot[y-1][x]:
            if garden[y-1][x]:
                area, perimeter, region = checkRegion(y-1,x)
                retArea += area
                retPerimeter += perimeter
                retRegion.extend(region)
        else:
            retPerimeter += 1
    else:
        retPerimeter += 1
    if x > 0:
        if gardenPlot[y][x] == gardenPlot[y][x-1]:
            if garden[y][x-1]:
                area, perimeter, region = checkRegion(y,x-1)
                retArea += area
                retPerimeter += perimeter
                retRegion.extend(region)
        else:
            retPerimeter += 1
    else:
        retPerimeter += 1
    if y < len(gardenPlot[0])-2:
        if gardenPlot[y][x] == gardenPlot[y+1][x]:
            if garden[y+1][x]:
                area, perimeter, region = checkRegion(y+1,x)
                retArea += area
                retPerimeter += perimeter
                retRegion.extend(region)
        else:
            retPerimeter += 1
    else:
        retPerimeter += 1
    if x < len(gardenPlot)-1:
        if gardenPlot[y][x] == gardenPlot[y][x+1]:
            if garden[y][x+1]:
                area, perimeter, region = checkRegion(y,x+1)
                retArea += area
                retPerimeter += perimeter
                retRegion.extend(region)
        else:
            retPerimeter += 1
    else:
        retPerimeter += 1

    return retArea, retPerimeter, retRegion

result = 0
for y in range(len(gardenPlot)):
    for x in range(len(gardenPlot[0])-1):
        if garden[y][x]:
            area, perimeter, region = checkRegion(y,x)

            for reg in region:
                if (reg[0],reg[1]+1) in region and not (reg[0]-1,reg[1]) in region and not (reg[0]-1,reg[1]+1) in region:
                    perimeter -= 1
                if (reg[0],reg[1]+1) in region and not (reg[0]+1,reg[1]) in region and not (reg[0]+1,reg[1]+1) in region:
                    perimeter -= 1
                if (reg[0]+1,reg[1]) in region and not (reg[0],reg[1]+1) in region and not (reg[0]+1,reg[1]+1) in region:
                    perimeter -= 1
                if (reg[0]+1,reg[1]) in region and not (reg[0],reg[1]-1) in region and not (reg[0]+1,reg[1]-1) in region:
                    perimeter -= 1
                    
            result += area * perimeter
print(result)
