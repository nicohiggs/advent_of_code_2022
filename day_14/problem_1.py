import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_14\\input.txt") as f: 
    lines = f.readlines()

grid = []
for i in range(200):
    new_row = []
    for j in range(200):
        new_row.append('.')
    grid.append(new_row)

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
            if pt1[0] > pt2[0]:
                step = -1
            else:
                step = 1
            for j in range(pt1[0], pt2[0]+step, step):
                grid[j][pt1[1]] = "#"

starting_point = (100, 0)
num_at_rest = 0
flowing_out_bottom = False
while not flowing_out_bottom:
    curr_sand = starting_point
    can_move = True
    while can_move:
        if grid[curr_sand[0]][curr_sand[1]+1] == '.': # down
            curr_sand = (curr_sand[0], curr_sand[1]+1)
        elif grid[curr_sand[0]-1][curr_sand[1]+1] == '.': # bottom left
            curr_sand = (curr_sand[0]-1, curr_sand[1]+1)
        elif grid[curr_sand[0]+1][curr_sand[1]+1] == '.': # bottom right
            curr_sand = (curr_sand[0]+1, curr_sand[1]+1)
        else: # at rest
            can_move = False
            grid[curr_sand[0]][curr_sand[1]] = 'o'
            num_at_rest += 1
        
        if curr_sand[1] >= 199: # flowing out bottom
            can_move = False
            flowing_out_bottom = True

print(num_at_rest)
