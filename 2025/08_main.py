import re
from pathlib import Path
import numpy as np

code = 0
code2 = 0

ROOT_DIR = Path(__file__).parent
with open(ROOT_DIR / "08_example.txt") as file:
    lines = file.readlines()

boxes = [[int(i) for i in re.findall(r"(\d+)", line)] for line in lines]

distances = set()

for id,box in enumerate(boxes):
    for id2,box2 in enumerate(boxes):
        if id != id2:
            distances.add((min(id,id2),max(id,id2),((box[0]-box2[0])**2+(box[1]-box2[1])**2+(box[2]-box2[2])**2)**0.5))

distances = list(distances)
distances = sorted(distances, key=lambda x: x[2])

numbersInGroups = set()
groups = []
