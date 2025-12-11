import re
from pathlib import Path
from functools import cache

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "11_data.txt") as file:
    lines = file.readlines()

devices = {}
for line in lines:
    temp = re.findall(r"([a-z]{3})",line)
    devices[temp[0]] = temp[1:]

@cache
def countNode(key,node):
    devicesList = list(set(devices[key]))

    if node in devicesList:
        return 1
    elif devicesList == ["out"]:
        return 0
    
    cnt = 0
    for d in devicesList:
        cnt += countNode(d,node)
    
    return cnt

code = countNode("you","out")
code2 = countNode("svr","fft") * countNode("fft","dac") * countNode("dac","out")

print(code,code2)
