with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_01\\input.txt") as f:
    lines = f.readlines()

curr_calories = 0
curr_best = 0
for line in lines:
    if line == '\n':
        if curr_calories > curr_best:
            curr_best = curr_calories

        curr_calories = 0        
    else:
        curr_calories+=int(line)


print(curr_best)
