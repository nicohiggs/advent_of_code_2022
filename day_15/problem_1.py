import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_15\\input.txt") as f: 
    lines = f.readlines()

y=2000000
cannot_contain_locs = {}
for line in lines:
    line = line.rstrip()
    split_line = line.split(' ')
    sensor_x = int(split_line[2][2:-1])
    sensor_y = int(split_line[3][2:-1])
    beacon_x = int(split_line[8][2:-1])
    beacon_y = int(split_line[9][2:-1])

    # manhattan distance to beacon
    mhd = np.abs(sensor_x - beacon_x) + np.abs(sensor_y - beacon_y)
    # compute straight distance to line
    d2y = np.abs(sensor_y - y)

    if d2y <= mhd: # we have some locations to eliminate
        # check the immediate spot
        if (beacon_x, beacon_y) not in cannot_contain_locs:
            cannot_contain_locs[(beacon_x, beacon_y)] = "B"
        else:
            cannot_contain_locs[(beacon_x, beacon_y)] = "#"
        # check spots in offsets either direction
        offsets_to_check = mhd - d2y
        for i in range(1, offsets_to_check+1):
            #
    