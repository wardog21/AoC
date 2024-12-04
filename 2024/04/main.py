import re

def countXMAS(input):
    count = 0
    for line in input:
        count += len(re.findall(r"(SAMX)",line))
        count += len(re.findall(r"(XMAS)",line))
    return count

def transpose(input):
    output = []
    for x in range(len(input[0])-1):
        row = ''
        for y in range(len(input)):
            row += input[y][x]
        output.append(row)
    return output

def turn45(input):
    output = []
    for y in range(len(input)):
        row = ''
        for x in range(min(y+1,len(input))):
            row += input[y-x][x]
        output.append(row)
    for x in range(1, len(input[0])-1):
        row = ''
        for y in range(len(input)-1,max(0,x)-1,-1):
            row += input[y][x+len(input)-1-y]
        output.append(row)
    return output

def turn135(input):
    output = []
    for x in range(len(input[0])-2, -1, -1):
        row = ''
        for y in range(len(input[0])-1-x):
            row += input[y][x+y]
        output.append(row)
    for y in range(1, len(input)):
        row = ''
        for x in range(len(input)-y):
            row += input[y+x][x]
        output.append(row)
    return output

with open("input.txt") as file:
    lines = file.readlines()

totalCount = countXMAS(lines)
totalCount += countXMAS(transpose(lines))
totalCount += countXMAS(turn45(lines))
totalCount += countXMAS(turn135(lines))

print(totalCount)