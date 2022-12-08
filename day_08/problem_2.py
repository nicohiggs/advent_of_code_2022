import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_08\\input.txt") as f: 
    lines = f.readlines()

list_array = []
for line in lines:
    line = line.rstrip()
    list_array.append(list(line))
tree_array = np.array(list_array, dtype=int)
height, width = tree_array.shape
best_scenic_score = 0
for i in range(1, height - 1):
    for j in range(1, width - 1):
        curr_height = tree_array[i, j]
        up_array = tree_array[:i,j]
        down_array = tree_array[i+1:, j]
        left_array = tree_array[i, :j]
        right_array = tree_array[i, j+1:]
        up_score = 0
        left_score = 0
        down_score = 0
        right_score = 0
        for tree in up_array[::-1]:
            up_score += 1
            if tree >= curr_height:
                break
        for tree in left_array[::-1]:
            left_score += 1
            if tree >= curr_height:
                break
        for tree in down_array:
            down_score += 1
            if tree >= curr_height:
                break
        for tree in right_array:
            right_score += 1
            if tree >= curr_height:
                break
        scenic_score = up_score * left_score * right_score * down_score
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score


print(best_scenic_score)