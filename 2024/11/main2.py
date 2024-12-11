from functools import cache

with open("11/input.txt") as file:
    stones = file.readline().strip().split(' ')

@cache
def blinking(stone, blinks):
    if blinks == 0:
        return 1
    if stone == '0':
        return blinking('1', blinks-1)
    elif len(stone)%2 == 0:
        return blinking(stone[:len(stone)//2], blinks-1) + blinking(str(int(stone[len(stone)//2:])), blinks-1)
    else:
        return blinking(str(int(stone)*2024), blinks-1)

counter = 0
for stone in stones:
    counter += blinking(stone, 75)
print(counter)