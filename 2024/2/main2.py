def checkReport(levels):
    increasing = (levels[0] < levels[1])
    safeReport = True

    for levelId in range(len(levels)-1):
        levelA = levels[levelId]
        levelB = levels[levelId+1]
        
        if levelA == levelB:
            safeReport = False
            break
        elif abs(levelA-levelB) > 3:
            safeReport = False
            break
        elif increasing != (levelA < levelB):
            safeReport = False
            break

    return safeReport


with open("input.txt") as file:
    reports = file.readlines()
safeReports = 0

for report in reports:
    levels = [int(level) for level in report.split(' ')]
    
    if checkReport(levels):
        safeReports += 1
    else:
        for removedLevel in range(len(levels)):
            tempLevels = levels[0:removedLevel] + levels[removedLevel+1:]
            if checkReport(tempLevels):
                safeReports += 1
                break

print(safeReports)