with open("05/input.txt") as file:
    input = file.readlines()

rules = []
updates = []
ruleOrder = []

for line in input:
    if line.find('|') > 0:
        rules.append(list(map(int, line.strip().split('|'))))
    elif line.find(',') > 0:
        updates.append(list(map(int, line.strip().split(','))))

result = 0

for update in updates:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                changed = True
                while changed:
                    changed = False
                    for rul in rules:
                        if rul[0] in update and rul[1] in update:
                            if update.index(rul[0]) > update.index(rul[1]):
                                changed = True
                                id = update.index(rul[0])
                                update.remove(rul[1])
                                update.insert(id, rul[1])
                                break
                result += update[int((len(update)-1)/2)]
                break

print(result)