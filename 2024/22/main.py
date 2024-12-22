def calcSecret(input, iterations):
    secret = input
    for i in range(iterations):
        secret ^= (secret*64)
        secret %= 16777216
        secret ^= (secret//32)
        secret %= 16777216
        secret ^= (secret*2048)
        secret %= 16777216
    return secret

with open("22/input.txt") as file:
    puzzles = file.readlines()

result = 0
for puzzle in puzzles:
    result += calcSecret(int(puzzle.strip()),2000)
print(result)