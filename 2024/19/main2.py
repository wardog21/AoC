from functools import cache

with open("19/input.txt") as file:
    puzzle = file.readlines()

patterns = puzzle[0].strip().split(', ')

@cache
def countDesign(design):
    counter = 0
    for pattern in patterns:
        if design.find(pattern) == 0:
            myDesign = design[len(pattern):]
            if len(myDesign) == 0:
                counter += 1
            else:
                counter += countDesign(myDesign)
    return counter

result = 0
for i in range(2,len(puzzle)):
    result += countDesign(puzzle[i].strip())
print(result)