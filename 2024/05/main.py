with open("05\input.txt") as file:
    input = file.readlines()

rules = []
updates = []

for line in input:
    if line.find('|') > 0:
        rules.append(line.strip().split('|'))
    elif line.find(',') > 0:
        updates.append(line.strip())

result = 0

for update in updates:
    valid = True
    for rule in rules:
        id_a = update.find(rule[0])
        id_b = update.find(rule[1])
        if id_a >= 0 and id_b >= 0 and id_a > id_b:
            valid = False
            break
    
    if valid:
        updateList = update.split(',')
        result += int(updateList[int((len(updateList)-1)/2)])

print(result)