import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_08\\input.txt") as f: 
    lines = f.readlines()

list_array = []
for line in lines:
    line = line.rstrip()
    list_array.append(list(line))
tree_array = np.array(list_array, dtype=int)
height, width = tree_array.shape
total_visible = 0
for i in range(1, height - 1):
    for j in range(1, width - 1):
        curr_height = tree_array[i, j]
        up_array = tree_array[:i,j]
        down_array = tree_array[i+1:, j]
        left_array = tree_array[i, :j]
        right_array = tree_array[i, j+1:]
        if up_array.max() < curr_height:
            total_visible += 1
        elif down_array.max() < curr_height:
            total_visible += 1
        elif left_array.max() < curr_height:
            total_visible += 1
        elif right_array.max() < curr_height:
            total_visible += 1
total_visible += height*2 + width*2 - 4
print(total_visible)