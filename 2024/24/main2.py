import re

with open("24/input.txt") as file:
    puzzle = file.readlines()

connections = {}
gates = []
countOutput = 0

toggleGatesInput = False
for line in puzzle:
    if toggleGatesInput:
        con0, gate, con1, res = re.findall(r"([a-z0-9]+) ([A-Z]+) ([a-z0-9]+) -> ([a-z0-9]+)",line)[0]
        gates.append((con0,con1,gate,res))
    elif line == "\n":
        toggleGatesInput = True
    else:
        con, val = re.findall(r"([xy]\d+): ([01])",line)[0]
        connections.update({con:(val=='1')})

result = []

for con0, con1, gate, res in gates:
    if res[0] == 'z' and gate != "XOR" and res != "z45":
        result.append(res)
        continue
    elif (gate == "XOR" and res[0] not in ['x', 'y', 'z'] and con0[0] not in ['x', 'y', 'z'] and con1[0] not in ['x', 'y', 'z']):
        result.append(res)
        continue
    elif gate == "AND" and "x00" not in [con0,con1]:
        for conn0, conn1, gatee, resu in gates:
            if (res == conn0 or res == conn1) and gatee != "OR":
                result.append(res)
                break
    if gate == "XOR":
        for conn0, conn1, gatee, resu in gates:
            if (res == conn0 or res == conn1) and gatee == "OR":
                result.append(res)
                break

result.sort()
resString = ""
for res in result:
    resString += res + ','
print(resString[:-1])