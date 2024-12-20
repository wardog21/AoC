with open("20/input.txt") as file:
    puzzle = file.readlines()

maze = []
start = [0,0]
end = [0,0]
for i in range(len(puzzle)):
    row = []
    for ii in range(len(puzzle[0])-1):
        if puzzle[i][ii] == '#':
            row.append(-2)
        else:
            row.append(-1)
            if puzzle[i][ii] == 'S':
                start[0] = i
                start[1] = ii
            elif puzzle[i][ii] == 'E':
                end[0] = i
                end[1] = ii
    maze.append(row)

pos = start
count = 0
while (pos[0] != end[0]) or (pos[1] != end[1]):
    maze[pos[0]][pos[1]] = count
    count += 1
    if maze[pos[0]-1][pos[1]] == -1:
        pos[0] -= 1
    elif maze[pos[0]+1][pos[1]] == -1:
        pos[0] += 1
    elif maze[pos[0]][pos[1]-1] == -1:
        pos[1] -= 1
    elif maze[pos[0]][pos[1]+1] == -1:
        pos[1] += 1
maze[end[0]][end[1]] = count

cheats = []
for i in range(len(maze)):
    for ii in range(len(maze[0])):
        if maze[i][ii] >= 0:
            # tempCheats = []
            for i2 in range(-20,21):
                y = i+i2
                if y < 0 or y >= len(maze):
                    continue
                for ii2 in range(-(20-abs(i2)),(21-abs(i2))):
                    x = ii + ii2
                    if x < 0 or x >= len(maze[0]):
                        continue
                    dist = maze[y][x] - maze[i][ii] - abs(i2) - abs(ii2)
                    if dist > 0:
                        cheats.append(dist)

cheatCounter = 0
for cheat in cheats:
    if cheat >= 100:
        cheatCounter += 1
print(cheatCounter)