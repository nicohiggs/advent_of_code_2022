import string

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_04\\input.txt") as f: 
    lines = f.readlines() 

assignment_pairs = 0
for line in lines:
    line_split = line.split(",")
    first_split = line_split[0].split("-")
    second_split = line_split[1].split("-")
    first_lower = int(first_split[0])
    first_upper = int(first_split[1])
    second_lower = int(second_split[0])
    second_upper = int(second_split[1])
    if (first_lower < second_lower) and (first_upper < second_lower):
        pass
    elif (first_lower > second_upper) and (first_upper > second_upper):
        pass
    else:
        assignment_pairs += 1


 
print(assignment_pairs)