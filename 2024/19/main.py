with open("19/input.txt") as file:
    puzzle = file.readlines()

patterns = puzzle[0].strip().split(', ')

def checkDesign(design):
    for pattern in patterns:
        if design.find(pattern) == 0:
            myDesign = design[len(pattern):]
            if len(myDesign) == 0:
                return True
            elif checkDesign(myDesign):
                return True
    return False

result = 0
for i in range(2,len(puzzle)):
    if checkDesign(puzzle[i].strip()):
        result += 1
print(result)