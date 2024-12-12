with open("02/input.txt") as file:
    reports = file.readlines()

safeReports = 0

for report in reports:
    levels = [int(level) for level in report.split(' ')]

    increasing = (levels[0] < levels[1])
    safeReport = True

    for levelId in range(len(levels)-1):
        if levels[levelId] == levels[levelId+1]:
            safeReport = False
            break
        elif abs(levels[levelId]-levels[levelId+1]) > 3:
            safeReport = False
            break
        elif increasing != (levels[levelId] < levels[levelId+1]):
            safeReport = False
            break
        
    if safeReport:
        safeReports += 1

print(safeReports)