import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_15\\input.txt") as f: 
    lines = f.readlines()

y = 2000000
beacons_on_y = {}
cannot_line_segments = []
for line in lines:
    line = line.rstrip()
    split_line = line.split(' ')
    sensor_x = int(split_line[2][2:-1])
    sensor_y = int(split_line[3][2:-1])
    beacon_x = int(split_line[8][2:-1])
    beacon_y = int(split_line[9][2:])

    # manhattan distance to beacon
    mhd = np.abs(sensor_x - beacon_x) + np.abs(sensor_y - beacon_y)
    # compute straight distance to line
    d2y = np.abs(sensor_y - y)

    if d2y < mhd: # we have some locations to eliminate
        left_x = sensor_x - (mhd-d2y)
        right_x = sensor_x + (mhd-d2y)
        left_x = np.max((left_x, 0))
        right_x = np.min((right_x, 4000000))
        if right_x < 0 or left_x > 4000000:
            pass
        else:
            cannot_line_segments.append((left_x, right_x))
            if beacon_y == y:
                if (beacon_x, beacon_y) not in beacons_on_y:
                    beacons_on_y[(beacon_x, beacon_y)] = 1

sorted_line_segments = sorted(cannot_line_segments)
i = 0
j = 1
done = False
total_cannot_spots = 0
while not done:
    left_segment = sorted_line_segments[i]
    right_segment = sorted_line_segments[j]
    if left_segment[1] < right_segment[0]: # disjointed
        total_cannot_spots += left_segment[1] - left_segment[0] + 1
        i = j
        j += 1
    elif left_segment[1] < right_segment[1]: # overlap
        total_cannot_spots += right_segment[0] - left_segment[0]
        i = j
        j += 1
    else: # superset
        j += 1
    
    if j >= len(sorted_line_segments):
        total_cannot_spots += sorted_line_segments[i][1] - sorted_line_segments[i][0] + 1
        done = True

num_beacons_on_y = len(beacons_on_y)
total_cannot_spots -= num_beacons_on_y
print(total_cannot_spots)

    