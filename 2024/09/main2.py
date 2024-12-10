with open("09/input.txt") as file:
    diskMap = [int(m) for m in file.readline()]

disk = []

id = 0
isEmpty = False
for i in range(len(diskMap)):
    if diskMap[i] > 0:
        if isEmpty:
            disk.append((diskMap[i],-1))
        else:
            disk.append((diskMap[i],id))
    isEmpty = not isEmpty
    if isEmpty:
        id += 1

while id > 0:
    if id % 100 == 0:
        print(int(id/100))
    for i in range(len(disk)-1,-1,-1):
        if disk[i][1] == id:
            for ii in range(0, i):
                if disk[ii][1] == -1 and disk[ii][0] >= disk[i][0]:
                    diff = disk[ii][0] - disk[i][0]
                    disk[ii] = disk[i]
                    disk[i] = (disk[i][0], -1)
                    if diff > 0:
                        disk.insert(ii+1,(diff,-1))
                    break
    id -= 1

checksum = 0
multi = 0
for i in range(len(disk)):
    for ii in range(disk[i][0]):
        if disk[i][1] >= 0:
            checksum += disk[i][1]*multi
        multi += 1

print(checksum)