import numpy as np

class Rock(object):
    def __init__(self, bottom_edge, type):
        self.bottom_edge = bottom_edge
        if type == 0:
            self.array = np.array(
                [[False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False],
                 [False, False, True, True, True, True, False]]
            )
        elif type == 1:
            self.array = np.array(
                [[False, False, False, False, False, False, False],
                 [False, False, False, True, False, False, False],
                 [False, False, True, True, True, False, False],
                 [False, False, False, True, False, False, False]]
            )
        elif type == 2:
            self.array = np.array(
                [[False, False, False, False, False, False, False],
                 [False, False, False, False, True, False, False],
                 [False, False, False, False, True, False, False],
                 [False, False, True, True, True, False, False]]
            )
        elif type == 3:
            self.array = np.array(
                [[False, False, True, False, False, False, False],
                 [False, False, True, False, False, False, False],
                 [False, False, True, False, False, False, False],
                 [False, False, True, False, False, False, False]]
            )
        elif type == 4:
            self.array = np.array(
                [[False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False],
                 [False, False, True, True, False, False, False],
                 [False, False, True, True, False, False, False]]
            )
    
    def move_left(self, grid_area):
        if self.array[:, 0].sum() == 0: # we can potentially move left
            new_array = np.array(
                [[False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False]]
            )
            new_array[:, :-1] = self.array[:, 1:]
            if not check_collision(new_array, grid_area):
                self.array = new_array
    
    def move_right(self, grid_area):
        if self.array[:, -1].sum() == 0: # we can potentially move right
            new_array = np.array(
                        [[False, False, False, False, False, False, False],
                        [False, False, False, False, False, False, False],
                        [False, False, False, False, False, False, False],
                        [False, False, False, False, False, False, False]]
                    )
            new_array[:, 1:] = self.array[:, :-1]
            if not check_collision(new_array, grid_area):
                self.array = new_array
    
    def move_down(self, grid_area):
        if not check_collision(self.array, grid_area):
            self.bottom_edge += 1
            return True
        else:
            return False
    
def check_collision(array1, array2):
    array_intersection = np.logical_and(array1, array2)
    if np.sum(array_intersection) > 0:
        return True
    else:
        return False

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_17\\input.txt") as f: 
    lines = f.readlines()

grid_height = 5000
jet_stream = list(lines[0].rstrip())
grid = np.zeros((grid_height+1, 7), dtype=bool)
tallest_rock = grid_height + 1
stream_idx = 0
rock_nums = []
heights = []
for i in range(2022):
    rock_type = i % 5
    if tallest_rock - 3 <= 0:
        print(f'grid too short... got to rock {i+1}')
        break
    curr_rock = Rock(tallest_rock-4, rock_type)
    rock_falling = True
    stream_push = True
    while rock_falling:
        if stream_push: # stream push
            curr_stream = jet_stream[stream_idx]
            curr_grid = grid[curr_rock.bottom_edge-3:curr_rock.bottom_edge+1, :]
            # do the push
            if curr_stream == '<':
                curr_rock.move_left(curr_grid)
            else:
                curr_rock.move_right(curr_grid)
            # update
            stream_idx += 1
            if stream_idx == len(jet_stream):
                stream_idx = 0
            stream_push = False # so we fall next time
        else: # move down
            if curr_rock.bottom_edge == grid_height: # hit the bottom
                rock_falling = False
                grid[curr_rock.bottom_edge-3:curr_rock.bottom_edge+1, :] = np.logical_or(
                    grid[curr_rock.bottom_edge-3:curr_rock.bottom_edge+1, :],
                    curr_rock.array
                )
                ########## tallest might be same still.....
                if grid[curr_rock.bottom_edge-3, :].sum() > 0:
                    curr_rock_top = curr_rock.bottom_edge-3
                elif grid[curr_rock.bottom_edge-2, :].sum() > 0:
                    curr_rock_top = curr_rock.bottom_edge-2
                elif grid[curr_rock.bottom_edge-1, :].sum() > 0:
                    curr_rock_top = curr_rock.bottom_edge-1
                else:
                    curr_rock_top = curr_rock.bottom_edge
                if curr_rock_top < tallest_rock:
                    tallest_rock = curr_rock_top
            else:
                curr_grid = grid[curr_rock.bottom_edge-2:curr_rock.bottom_edge+2, :] # we check 1 down
                if not curr_rock.move_down(curr_grid):
                    rock_falling = False
                    grid[curr_rock.bottom_edge-3:curr_rock.bottom_edge+1, :] = np.logical_or(
                        grid[curr_rock.bottom_edge-3:curr_rock.bottom_edge+1, :],
                        curr_rock.array
                    )
                    if grid[curr_rock.bottom_edge-3, :].sum() > 0:
                        curr_rock_top = curr_rock.bottom_edge-3
                    elif grid[curr_rock.bottom_edge-2, :].sum() > 0:
                        curr_rock_top = curr_rock.bottom_edge-2
                    elif grid[curr_rock.bottom_edge-1, :].sum() > 0:
                        curr_rock_top = curr_rock.bottom_edge-1
                    else:
                        curr_rock_top = curr_rock.bottom_edge
                    if curr_rock_top < tallest_rock:
                        tallest_rock = curr_rock_top
                else:
                    stream_push = True # so we push next time
    rock_nums.append(i+1)
    heights.append(grid_height - tallest_rock + 1)
print(grid_height - tallest_rock + 1)
import matplotlib.pyplot as plt
plt.plot(rock_nums, heights)
plt.show()