import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_09\\input.txt") as f: 
    lines = f.readlines()

def update_knot(head, tail):
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
    
    # error check
    assert np.abs(head[0] - tail[0]) <= 1 and np.abs(head[1] - tail[1]) <= 1, "UH OH: Tail update fail"
    return tail

tail_visits = {}
knots = {
    "H": (0, 0),
    1: (0, 0),
    2: (0, 0),
    3: (0, 0),
    4: (0, 0),
    5: (0, 0),
    6: (0, 0),
    7: (0, 0),
    8: (0, 0),
    9: (0, 0)
}
tail_visits[knots[9]] = 1
for line in lines:
    line = line.rstrip()
    split_line = line.split(' ')
    direction = split_line[0]
    num_steps = int(split_line[1])

    for step in range(1, num_steps+1):
        # move head
        if direction == "R":
            knots["H"] = (knots["H"][0]+1, knots["H"][1])
        elif direction == "L":
            knots["H"] = (knots["H"][0]-1, knots["H"][1])
        elif direction == "U":
            knots["H"] = (knots["H"][0], knots["H"][1]+1)
        else:
            knots["H"] = (knots["H"][0], knots["H"][1]-1)
        
        for knot in range(1, 10):
            if knot == 1:
                head = knots["H"]
            else:
                head = knots[knot-1]
            
            knots[knot] = update_knot(head, knots[knot])
        
        if knots[9] not in tail_visits:
            tail_visits[knots[9]] = 1

print(len(tail_visits))