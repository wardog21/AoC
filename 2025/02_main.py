from pathlib import Path

code = 0
code2 = 0
validSet = set()

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "02_data.txt") as file:
    line = file.readline()

ranges = line.split(',')
for cRange in ranges:
    start,end = [int(i) for i in cRange.split('-')]
    for id in range(start,end+1):
        strId = str(id)
        if len(strId)%2 == 0:
            if strId[:len(strId)//2] == strId[len(strId)//2:]:
                code += id
                validSet.add(id)
        if len(strId) > 2:
            for pattern in range(3, len(strId)+1):
                if len(strId)%pattern == 0:
                    valid = True
                    patternLen = len(strId)//pattern
                    testPattern = strId[:patternLen]
                    for pCnt in range(2,pattern+1):
                        cPattern = strId[(pCnt-1)*patternLen : (pCnt)*patternLen]
                        if cPattern != testPattern:
                            valid = False
                            break
                    if valid:
                        validSet.add(id)

code2 = sum(validSet)
print(code, code2)