with open("07/input.txt") as file:
    equations = file.readlines()

result = 0

for index, equation in enumerate(equations):
    print(index, len(equations))
    testValue = int(equation.split(':')[0])
    numbers = [int(x) for x in equation.split(':')[1].strip().split(' ')]

    operator = []
    for i in range(len(numbers)-1):
        operator.append(0)

    while(True):
        currentValue = numbers[0]

        for operatorID in range(len(operator)):
            if operator[operatorID] == 0:
                currentValue *= numbers[operatorID+1]
            elif operator[operatorID] == 1:
                currentValue += numbers[operatorID+1]
            else:
                currentValue = int(str(currentValue)+str(numbers[operatorID+1]))
        
        if currentValue == testValue:
            result += testValue
            break
        
        toggle = True
        for operatorID in range(len(operator)):
            if toggle:
                operator[operatorID] += 1
                if operator[operatorID] > 2:
                    operator[operatorID] = 0
                else:
                    toggle = False
        
        if toggle:
            break

print(result)