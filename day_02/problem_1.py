with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_02\\input.txt") as f:
    lines = f.readlines()

total_points = 0
for line in lines:
    opp = line[0]
    you = line[2]
    if opp == "A":
        if you == "X":
            total_points += 3
        elif you == "Y":
            total_points += 6
        else:
            total_points += 0
    elif opp == "B":
        if you == "X":
            total_points += 0
        elif you == "Y":
            total_points += 3
        else:
            total_points += 6
    else:
        if you == "X":
            total_points += 6
        elif you == "Y":
            total_points += 0
        else:
            total_points += 3
    
    if you == "X":
        total_points += 1
    elif you == "Y":
        total_points += 2
    else:
        total_points += 3

print(total_points)
