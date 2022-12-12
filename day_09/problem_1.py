import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_09\\input.txt") as f: 
    lines = f.readlines()

tail_visits = {}
head = (0, 0)
tail = (0, 0)
tail_visits[tail] = 1
for line in lines:
    line = line.rstrip()
    split_line = line.split(' ')
    direction = split_line[0]
    num_steps = int(split_line[1])

    for step in range(1, num_steps+1):
        # move head
        if direction == "R":
            head = (head[0]+1, head[1])
        elif direction == "L":
            head = (head[0]-1, head[1])
        elif direction == "U":
            head = (head[0], head[1]+1)
        else:
            head = (head[0], head[1]-1)
        
        # update tail
        if np.abs(head[0] - tail[0]) <= 1 and np.abs(head[1] - tail[1]) <= 1:
            # tail doesnt need to update
            pass
        elif head[0] == tail[0]: # same column
            if head[1] > tail[1]:
                tail = (tail[0], tail[1]+1)
            else:
                tail = (tail[0], tail[1]-1)
        elif head[1] == tail[1]: # same row
            if head[0] > tail[0]:
                tail = (tail[0]+1, tail[1])
            else:
                tail = (tail[0]-1, tail[1])
        else: # diagonal case
            if head[0] > tail[0]:
                if head[1] > tail[1]:
                    # top right
                    tail = (tail[0]+1, tail[1]+1)
                else:
                    # bottom right
                    tail = (tail[0]+1, tail[1]-1)
            else:
                if head[1] > tail[1]:
                    # top left
                    tail = (tail[0]-1, tail[1]+1)
                else:
                    # bottom left
                    tail = (tail[0]-1, tail[1]-1)
        
        if tail not in tail_visits:
            tail_visits[tail] = 1
        # error check
        assert np.abs(head[0] - tail[0]) <= 1 and np.abs(head[1] - tail[1]) <= 1, "UH OH: Tail update fail"

print(len(tail_visits))