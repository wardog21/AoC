import re
from pathlib import Path
import numpy as np

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "07_data.txt") as file:
    lines = file.readlines()

beams = []
beams2 = [0] * (len(lines[0])-1)

for id, line in enumerate(lines):
    print("id:",id)
    newBeams = set()
    newBeams2 = [0] * (len(lines[0])-1)
    if (sfound := line.find('S')) >= 0:
        newBeams.add(sfound)
        newBeams2[sfound] = 1
        code2 += 1
    else:
        for beam in beams:
            if line[beam] == '.':
                newBeams.add(beam)
                newBeams2[beam] += beams2[beam]
            elif line[beam] == '^':
                code += 1
                if beam > 0:
                    newBeams.add(beam-1)
                    newBeams2[beam-1] += beams2[beam]
                    code2 += beams2[beam]
                if beam < len(lines[0])-1:
                    newBeams.add(beam+1)
                    newBeams2[beam+1] += beams2[beam]
                    code2 += beams2[beam]
                code2 -= beams2[beam]
            else:
                print("error", beam)
    beams = list(newBeams)
    beams2 = newBeams2

print(code, code2)