def directionalKeypad(input):
    myString = ""
    pos = 'A'
    positions = {
        '^': (0,1),
        '<': (1,0),
        'v': (1,1),
        '>': (1,2),
        'A': (0,2)
    }
    for i in range(len(input)):
        diffY = positions[input[i]][0] - positions[pos][0]
        diffX = positions[input[i]][1] - positions[pos][1]
        if positions[input[i]][1] == 0:
            for ii in range(diffY):
                myString += 'v'
            for ii in range(-diffX):
                myString += '<'
        else:
            if diffX < 0:
                for ii in range(-diffX):
                    myString += '<'
            if diffY > 0:
                for ii in range(diffY):
                    myString += 'v'
            if diffY < 0:
                for ii in range(-diffY):
                    myString += '^'
            if diffX > 0:
                for ii in range(diffX):
                    myString += '>'
        pos = input[i]
        myString += 'A'
        
    return myString

def numericKeypad(input):
    myString = ""
    pos = 'A'
    positions = {
        '0': (3,1),
        '1': (2,0),
        '2': (2,1),
        '3': (2,2),
        '4': (1,0),
        '5': (1,1),
        '6': (1,2),
        '7': (0,0),
        '8': (0,1),
        '9': (0,2),
        'A': (3,2)
    }
    for i in range(len(input)):
        diffY = positions[input[i]][0] - positions[pos][0]
        diffX = positions[input[i]][1] - positions[pos][1]
        if positions[input[i]][1] == 0 and positions[pos][0] == 3:
            for ii in range(-diffY):
                myString += '^'
            for ii in range(-diffX):
                myString += '<'
        elif positions[input[i]][0] == 3 and positions[pos][1] == 0:
            for ii in range(diffX):
                myString += '>'
            for ii in range(diffY):
                myString += 'v'
        else:
            if diffX < 0:
                for ii in range(-diffX):
                    myString += '<'
            if diffY > 0:
                for ii in range(diffY):
                    myString += 'v'
            if diffY < 0:
                for ii in range(-diffY):
                    myString += '^'
            if diffX > 0:
                for ii in range(diffX):
                    myString += '>'
        pos = input[i]
        myString += 'A'
        
    return myString

with open("21/input.txt") as file:
    puzzle = file.readlines()

result = 0
for code in puzzle:
    sequence = directionalKeypad(directionalKeypad(numericKeypad(code.strip())))
    result += len(sequence) * int(code.strip()[:-1])
print(result)