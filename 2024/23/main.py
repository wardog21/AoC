import re

with open("23/input.txt") as file:
    connections = [re.findall(r"([a-z][a-z])-([a-z][a-z])",m)[0] for m in file.readlines()]

groups = []
lanGroups = []
for connection in connections:
    numGroups = len(groups)
    groups.append({connection[0], connection[1]})
    for i in range(numGroups):
        if numGroups == 0:
            groups.append({connection[0], connection[1]})
        elif len(groups[i]) == 2:
            if connection[0] in groups[i] or connection[1] in groups[i]:
                groups.append(groups[i].union({connection[0], connection[1]}))
        elif len(groups[i]) == 3:
            if connection[0] in groups[i] and connection[1] in groups[i]:
                for user in groups[i]:
                    if user[0] == 't':
                        lanGroups.append(groups[i])
                        break
print(len(lanGroups))