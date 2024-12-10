import re

charstr='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

with open ("08/input.txt") as file:
    mapInput = file.readlines()

antinodes = []
for i in range(len(mapInput)):
    row = []
    for ii in range(len(mapInput[0])-1):
        row.append(False)
    antinodes.append(row)

for antennaType in charstr:
    antennas = []
    for y in range(len(mapInput)):
        for x in range(len(mapInput[0])-1):
            if mapInput[y][x] == antennaType:
                antennas.append((x,y))
    
    if len(antennas) > 1:
        for a in antennas:
            for b in antennas:
                if a != b:
                    diffX = b[0]-a[0]
                    diffY = b[1]-a[1]
                    x = b[0]
                    y = b[1]
                    while x >= 0 and x < len(antinodes[0]) and y >= 0 and y < len(antinodes):
                        antinodes[y][x] = True
                        x += diffX
                        y += diffY


result = 0
for i in range(len(antinodes)):
    for ii in range(len(antinodes[0])):
        if antinodes[i][ii]:
            result += 1
print(result)