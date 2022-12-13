import numpy as np
import heapq

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_12\\input.txt") as f: 
    lines = f.readlines()

rows = []
for line in lines:
    line = line.rstrip()
    rows.append(list(line))
grid = np.array(rows)
start_idx = np.argwhere(grid == "S")[0]
start_loc = (start_idx[0], start_idx[1])
end_idx = np.argwhere(grid == "E")[0]
end_loc = (end_idx[0], end_idx[1])

grid[start_loc] = 'a'
starting_positions = np.argwhere(grid == "a")

no_go_length = grid.shape[0] * grid.shape[1] + 1
path_lengths = np.ones(grid.shape) * no_go_length

class Square:
    def __init__(self, path_length, loc):
        self.path_length = path_length
        self.loc = loc
    def __lt__(self, other):
        return self.path_length < other.path_length
squares_to_check = []
initial_square = Square(0, end_loc)
heapq.heappush(squares_to_check, initial_square)

# start_found = False
while len(squares_to_check) > 0:
    curr_square = heapq.heappop(squares_to_check)
    curr_height = grid[curr_square.loc]
    if curr_height == "E":
        curr_height = 'z'
    # check upwards
    check_loc = (curr_square.loc[0]-1, curr_square.loc[1])
    check_length = curr_square.path_length + 1
    if check_loc[0] >= 0 and grid[check_loc] == "S":
        start_found = True
    if (check_loc[0] >= 0 and
        ord(curr_height) - ord(grid[check_loc]) <= 1 and
        path_lengths[check_loc] > (check_length)):
        path_lengths[check_loc] = check_length
        new_square = Square(check_length, (check_loc))
        heapq.heappush(squares_to_check, new_square)
    # check downwards
    check_loc = (curr_square.loc[0]+1, curr_square.loc[1])
    check_length = curr_square.path_length + 1
    if check_loc[0] < grid.shape[0] and grid[check_loc] == "S":
        start_found = True
    if (check_loc[0] < grid.shape[0] and
        ord(curr_height) - ord(grid[check_loc]) <= 1 and
        path_lengths[check_loc] > (check_length)):
        path_lengths[check_loc] = check_length
        new_square = Square(check_length, (check_loc))
        heapq.heappush(squares_to_check, new_square)
    # check left
    check_loc = (curr_square.loc[0], curr_square.loc[1]-1)
    check_length = curr_square.path_length + 1
    if check_loc[1] >= 0 and grid[check_loc] == "S":
        start_found = True
    if (check_loc[1] >= 0 and
        ord(curr_height) - ord(grid[check_loc]) <= 1 and
        path_lengths[check_loc] > (check_length)):
        path_lengths[check_loc] = check_length
        new_square = Square(check_length, (check_loc))
        heapq.heappush(squares_to_check, new_square)
    # check right
    check_loc = (curr_square.loc[0], curr_square.loc[1]+1)
    check_length = curr_square.path_length + 1
    if check_loc[1] < grid.shape[1] and grid[check_loc] == "S":
        start_found = True
    if (check_loc[1] < grid.shape[1] and
        ord(curr_height) - ord(grid[check_loc]) <= 1 and
        path_lengths[check_loc] > (check_length)):
        path_lengths[check_loc] = check_length
        new_square = Square(check_length, (check_loc))
        heapq.heappush(squares_to_check, new_square)

min_length = no_go_length
for position in starting_positions:
    start_loc = (position[0], position[1])
    if path_lengths[start_loc] < min_length:
        min_length = path_lengths[start_loc]



print(min_length)