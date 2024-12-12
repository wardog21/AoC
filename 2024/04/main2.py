with open("04/input.txt") as file:
    lines = file.readlines()
totalCount = 0

for y in range(1, len(lines)-1):
    for x in range(1, len(lines[0])-2):
        if lines[y][x] == 'A':
            if lines[y-1][x-1] == 'M' and lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S' and lines[y+1][x+1] == 'S':
                totalCount += 1
            elif lines[y-1][x-1] == 'M' and lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M' and lines[y+1][x+1] == 'S':
                totalCount += 1
            elif lines[y-1][x-1] == 'S' and lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M' and lines[y+1][x+1] == 'M':
                totalCount += 1
            elif lines[y-1][x-1] == 'S' and lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S' and lines[y+1][x+1] == 'M':
                totalCount += 1

print(totalCount)