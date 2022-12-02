with open("C:\\Users\\nicoh\\advent_of_code\\day_02\\input.txt") as f:
    lines = f.readlines()

total_points = 0
for line in lines:
    opp = line[0]
    you = line[2]
    if opp == "A":
        if you == "X":
            total_points += 0 + 3
        elif you == "Y":
            total_points += 3 + 1
        else:
            total_points += 6 + 2
    elif opp == "B":
        if you == "X":
            total_points += 0 + 1
        elif you == "Y":
            total_points += 3 + 2
        else:
            total_points += 6 + 3
    else:
        if you == "X":
            total_points += 0 + 2
        elif you == "Y":
            total_points += 3 + 3
        else:
            total_points += 6 + 1


print(total_points)