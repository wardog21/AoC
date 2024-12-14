import re

priceA = 3
priceB = 1

with open("13/input.txt") as file:
    puzzle = file.readlines()

result = 0

for nr in range(len(puzzle)//4+1):
    aX, aY = [int(n) for n in re.findall(r"X\+(\d+), Y\+(\d+)", puzzle[nr*4])[0]]
    bX, bY = [int(n) for n in re.findall(r"X\+(\d+), Y\+(\d+)", puzzle[nr*4+1])[0]]
    pX, pY = [int(n) for n in re.findall(r"X=(\d+), Y=(\d+)", puzzle[nr*4+2])[0]]

    pX += 10000000000000
    pY += 10000000000000

    a = round((pX/bX-pY/bY) / (aX/bX-aY/bY))
    b = round((pX/aX-pY/aY) / (bX/aX-bY/aY))

    
    if a * aX + b * bX == pX and a * aY + b * bY == pY:
        result += priceA * a + priceB * b
    
print(result)