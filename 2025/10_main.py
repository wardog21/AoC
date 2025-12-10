import re
from pathlib import Path
import numpy as np
from z3 import *

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "10_data.txt") as file:
    lines = file.readlines()

for line in lines:
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
    m = np.matrix(buttons).T
    x = [Int(f"x_{i}") for i in range(m.shape[1])]
    opt = Optimize()

    for i in range(m.shape[0]):
        equation = Sum(m[i, j] * x[j] for j in range(m.shape[1]))
        opt.add(equation == jolts[i])
    
    for var in x:
        opt.add(var >= 0)

    objective = opt.minimize(Sum(x))

    if opt.check() == sat:
        model = opt.model()
        solution = np.array([model[var].as_long() for var in x])
        code2 += sum(solution)
    
print(code, code2)
