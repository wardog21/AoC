import re
from pathlib import Path
import numpy as np
import time

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "10_data.txt") as file:
    lines = file.readlines()

startTime = time.time()
for lineId,line in enumerate(lines):
    print(lineId,len(lines),time.time()-startTime)
    leds = np.array([1 if l=='#' else 0 for l in re.findall(r"\[([.#]+)\]",line)[0]])

    buttons = []
    buttonList = re.findall(r"\([\d+,]+\)",line)
    for button in buttonList:
        wires = np.zeros(len(leds),np.int_)
        for b in re.findall(r"(\d+)",button):
            wires[int(b)] = 1
        buttons.append(wires)
    
    temp = re.findall(r"\{([\d+,]+)\}",line)[0]
    jolts = np.array([int(j) for j in re.findall(r"(\d+)",temp)])

    # code1
    cnt = 99999
    for b in range(2**len(buttons)):
        config = format(b,'0'+str(len(buttons))+'b')
        led = np.zeros(len(leds),np.int_)
        for id,c in enumerate(config):
            if int(c) == 1:
                led = (led+buttons[id])%2
        if all(led==leds):
            cnt = min(cnt,config.count('1'))
    code += cnt

    # code2
    cnt = -1
    upper = max(jolts)
    current = np.zeros(len(buttons),np.int_)
    tooHigh = []
    while True:
        current[0] += 1
        for c in range(len(current)):
            if current[c] > upper:
                current[c] = 0
                current[c+1] += 1
        if all(current >= np.full(len(buttons),upper)):
            break
        
        if cnt > 0 and sum(current) > cnt:
            continue

        highTriggered = False
        for high in tooHigh:
            if all(high <= current):
                highTriggered = True
                break
        if highTriggered:
            continue
        
        jolt = np.zeros(len(leds),np.int_)
        next = False
        for i,tc in enumerate(current):
            jolt += buttons[i]*tc

        if any(jolt > jolts):
            tooHigh.append(np.copy(current))
            continue

        if all(jolt == jolts):
            if cnt < 0:
                cnt = sum(current)
            else:
                cnt = min(cnt,sum(current))
    
    code2 += cnt

print(code, code2)
