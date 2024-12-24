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

gId = 0
while len(gates) > 0:
    if gId >= len(gates):
        gId = 0
    gate = gates[gId]
    if gate[0] in connections and gate[1] in connections:
        if gate[2] == "AND":
            connections.update({gate[3]:(connections[gate[0]] and connections[gate[1]])})
        elif gate[2] == "OR":
            connections.update({gate[3]:(connections[gate[0]] or connections[gate[1]])})
        elif gate[2] =="XOR":
            connections.update({gate[3]:(connections[gate[0]] ^ connections[gate[1]])})
        else:
            print("Error:",gate[2])
        gates.pop(gId)
    else:
        gId += 1

result = 0
resList = list(connections)
resList.sort(reverse=True)
for connection in resList:
    if connection[0] == 'z':
        if connections[connection]:
            result += 2**int(connection[1:])
print(result)