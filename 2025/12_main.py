import re
from pathlib import Path

code = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "12_data.txt") as file:
    lines = file.readlines()

for line in lines:
    temp = re.findall(r"(\d+)x(\d+):(.*)",line)
    if len(temp) > 0:
        temp = temp[0]
        area = int(temp[0])*int(temp[1])
        shapes = sum([int(d) for d in re.findall(r"(\d+)",temp[2])])*9
        if area >= shapes:
            code += 1
print(code)