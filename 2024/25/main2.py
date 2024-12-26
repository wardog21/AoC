with open("25/input.txt") as file:
    puzzle = file.readlines()

locks = []
keys = []

mode = 0
for line in puzzle:
    if mode == 0:
        if line.strip() == "#####":
            locks.append([0,0,0,0,0])
            mode = 1
        elif line.strip() == ".....":
            keys.append([0,0,0,0,0])
            mode = 2
    elif mode == 1:
        if line == "\n":
            mode = 0
        else:
            for i in range(5):
                if line[i] == '#':
                    locks[-1][i] += 1
    elif mode == 2:
        if line == "\n":
            for i in range(5):
                keys[-1][i] -= 1
            mode = 0
        else:
            for i in range(5):
                if line[i] == '#':
                    keys[-1][i] += 1
if mode == 2:
    for i in range(5):
        keys[-1][i] -= 1

result = 0
for lock in locks:
    for key in keys:
        fit = True
        for i in range(5):
            if lock[i] + key[i] > 5:
                fit = False
                break
        if fit:
            result += 1
print(result)