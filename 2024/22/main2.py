def calcSecret(secret, iterations):
    for i in range(iterations):
        secret ^= (secret*64)
        secret %= 16777216
        secret ^= (secret//32)
        secret %= 16777216
        secret ^= (secret*2048)
        secret %= 16777216
    return secret

def createSequences(input, dictornary, iterations):
    secret = input
    price = secret%10
    curDict = []
    curSeq = []
    for i in range(4):
        secret = calcSecret(secret,1)
        curPrice = secret%10
        curSeq.append(curPrice-price)
        price = curPrice
    mySeq = tuple(curSeq)
    curDict.append(mySeq)
    if mySeq in dictornary:
        dictornary[mySeq] += price
    else:
        dictornary.update({mySeq:price})
    for i in range(iterations-4):
        secret = calcSecret(secret,1)
        curPrice = secret%10
        curSeq.append(curPrice-price)
        price = curPrice
        mySeq = tuple(curSeq[-4:])
        if not mySeq in curDict:
            curDict.append(mySeq)
            if mySeq in dictornary:
                dictornary[mySeq] += price
            else:
                dictornary.update({mySeq:price})
    return dictornary

with open("22/input.txt") as file:
    puzzles = file.readlines()

myDict = {}
for i, puzzle in enumerate(puzzles):
    myDict = createSequences(int(puzzle.strip()),myDict,2000)
print(max(myDict, key=myDict.get), max(myDict.values()))