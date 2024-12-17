command = [2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0]

def calc(regA):
    output = []
    while True:
        regB = regA % 8
        regB = regB ^ 5
        regC = int( regA // (1 << regB) )
        regB = regB ^ regC
        regA = int( regA // 8 )
        regB = regB ^ 6
        output.append(regB % 8)
        if regA == 0:
            break
    return output

queue = [(15, 0)]
potential_As = []

while queue:
    i, a = queue.pop(0)
    if i < 0:
        continue
    for o in range(8):
        test_a = (a << 3) + o
        output = calc(test_a)
        if not output == command[i:]:
            continue
        if i == 0:
            potential_As.append(test_a)
        queue.append((i-1, test_a))

potential_As.sort()
print(potential_As[0])