import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_14\\input.txt") as f: 
    lines = f.readlines()

grid = [['.']*200]*200
for line in lines:
    line = line.strip()
    points = line.split(' -> ')
    pts = []
    for point in points:
        pt = eval(f"({point})")
        pts.append((pt[0]-400, pt[1]))
    for i in range(1, len(pts)):
        pt1 = pts[i-1]
        pt2 = pts[i]
        if pt1[0] == pt2[0]: # same x coord means vertical line
            if pt1[1] > pt2[1]:
                step = -1
            else:
                step = 1
            for j in range(pt1[1], pt2[1]+step, step):
                grid[pt1[0]][j] = "#"
        else: # same y coord means horizontal line
        