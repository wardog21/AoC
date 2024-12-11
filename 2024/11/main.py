with open("11/input.txt") as file:
    stones = file.readline().strip().split(' ')

for blinks in range(25):
    temp = []
    for stone in stones:
        if stone == '0':
            temp.append('1')
        elif len(stone)%2 == 0:
            temp.append(stone[:len(stone)//2])
            temp.append(str(int(stone[len(stone)//2:])))
        else:
            temp.append(str(int(stone)*2024))
    stones = temp


print(len(stones))