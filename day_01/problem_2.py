with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_01\\input.txt") as f:
    lines = f.readlines()

calories = []
curr_calories = 0
for line in lines:
    if line == '\n':
        calories.append(curr_calories)
        curr_calories = 0        
    else:
        curr_calories+=int(line)

calories.sort(reverse=True)
print(sum(calories[:3]))
