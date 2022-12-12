with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_10\\input.txt") as f: 
    lines = f.readlines()

cycle = 0
X = 1
sum_of_signals = 0
for line in lines:
    line = line.rstrip()
    if line == "noop":
        cycle += 1
        if ((cycle - 20) % 40) == 0:
            sum_of_signals += cycle * X
    else:
        cycle += 1
        if ((cycle - 20) % 40) == 0:
            sum_of_signals += cycle * X
        cycle += 1
        if ((cycle - 20) % 40) == 0:
            sum_of_signals += cycle * X
        split_line = line.split(' ')
        V = int(split_line[1])
        X += V
    
    
print(sum_of_signals)