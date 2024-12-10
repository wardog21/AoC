with open("09/input.txt") as file:
    diskMap = file.readline()

disk = []

id = 0
isEmpty = False
for i in range(len(diskMap)):
    for ii in range(int(diskMap[i])):
        if isEmpty:
            disk.append(-1)
        else:
            disk.append(id)
    isEmpty = not isEmpty
    if isEmpty:
        id += 1

currentLast = len(disk)-1
checksum = 0

for i in range(len(disk)):
    if i > currentLast:
        break
    if disk[i] >= 0:
        checksum += i * disk[i]
    else:
        while(disk[currentLast] < 0):
            currentLast -= 1
        if i >= currentLast:
            break
        else:
            checksum += i * disk[currentLast]
            currentLast -= 1

print(checksum)