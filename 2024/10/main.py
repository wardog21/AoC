with open("10/input.txt") as file:
    topo = file.readlines()

nodes = []
topId = 0

for y in range(len(topo)):
    for x in range(len(topo[0])-1):
        if topo[y][x] == '.':
            nodes.append([-1,[]])
        elif topo[y][x] == '9':
            nodes.append([9,[topId]])
            topId += 1
        else:
            nodes.append([int(topo[y][x]),[]])
            if x > 0:
                if topo[y][x-1] != '.':
                    if int(topo[y][x-1]) == int(topo[y][x])+1:
                        nodes[-1][1].append(y*(len(topo[0])-1)+x-1)
            if y > 0:
                if topo[y-1][x] != '.':
                    if int(topo[y-1][x]) == int(topo[y][x])+1:
                        nodes[-1][1].append((y-1)*(len(topo[0])-1)+x)
            if x < len(topo[0])-2:
                if topo[y][x+1] != '.':
                    if int(topo[y][x+1]) == int(topo[y][x])+1:
                        nodes[-1][1].append(y*(len(topo[0])-1)+x+1)
            if y < len(topo)-1:
                if topo[y+1][x] != '.':
                    if int(topo[y+1][x]) == int(topo[y][x])+1:
                        nodes[-1][1].append((y+1)*(len(topo[0])-1)+x)

for height in range(8,-1,-1):
    for node in nodes:
        if node[0] == height:
            temp = []
            for nodeId in node[1]:
                temp.extend(nodes[nodeId][1])
            node[1] = temp

trailheads = 0
for node in nodes:
    if node[0] == 0:
        trailheads += len(set(node[1]))
print(trailheads)