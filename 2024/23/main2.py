import re

with open("23/input.txt") as file:
    puzzle = [re.findall(r"([a-z][a-z])-([a-z][a-z])",m)[0] for m in file.readlines()]

connections = {}
groups = []
for connection in puzzle:
    groups.append({connection[0], connection[1]})
    for i in range(2):
        if connection[i] in connections:
            connections[connection[i]].add(connection[(i+1)%2])
        else:
            connections[connection[i]] = {connection[(i+1)%2]}

l = len(connections)
for c, i in enumerate(connections):
    print(c,'/',l)
    lenGroups = len(groups)
    for ii in range(lenGroups):
        if groups[ii].issubset(connections[i]):
            groups.append(groups[ii].union({i}))

group = list(max(groups, key=len))
group.sort()
code = ""
for member in group:
    code += member + ','
print(code[:-1])