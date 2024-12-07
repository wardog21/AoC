with open("07/input.txt") as file:
    equations = file.readlines()

result = 0

for equation in equations:
    testValue = int(equation.split(':')[0])
    numbers = [int(x) for x in equation.split(':')[1].strip().split(' ')]

    isMultiplication = []
    for i in range(len(numbers)-1):
        isMultiplication.append(False)

    while(True):
        currentValue = numbers[0]

        for operator in range(len(isMultiplication)):
            if isMultiplication[operator]:
                currentValue *= numbers[operator+1]
            else:
                currentValue += numbers[operator+1]
        
        if currentValue == testValue:
            result += testValue
            break
        
        toggle = True
        for operator in range(len(isMultiplication)):
            if toggle:
                if not isMultiplication[operator]:
                    toggle = False
                isMultiplication[operator] = not isMultiplication[operator]
        
        if toggle:
            break

print(result)