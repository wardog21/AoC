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
            if i > 1:
                if maze[i-2][ii] >= 0 and maze[i-2][ii] > maze[i][ii]+2:
                    cheats.append(maze[i-2][ii]-maze[i][ii]-2)
            if i < len(maze)-2:
                if maze[i+2][ii] >= 0 and maze[i+2][ii] > maze[i][ii]+2:
                    cheats.append(maze[i+2][ii]-maze[i][ii]-2)
            if ii > 1:
                if maze[i][ii-2] >= 0 and maze[i][ii-2] > maze[i][ii]+2:
                    cheats.append(maze[i][ii-2]-maze[i][ii]-2)
            if ii < len(maze[0])-2:
                if maze[i][ii+2] >= 0 and maze[i][ii+2] > maze[i][ii]+2:
                    cheats.append(maze[i][ii+2]-maze[i][ii]-2)

cheatCounter = 0
for cheat in cheats:
    if cheat >= 100:
        cheatCounter += 1
print(cheatCounter)