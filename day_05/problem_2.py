with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_05\\input.txt") as f: 
    lines = f.readlines() 

parsed_stacks = False
started_moves = False
stacks = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}
for line in lines:
    if not parsed_stacks:
        if line[1] == "1":
            parsed_stacks = True
        else:
            for i in range(9):
                stack_num = i+1
                stack_idx = i*4 + 1
                if line[stack_idx] != " ":
                    stacks[stack_num].insert(0, line[stack_idx])
    else:
        if line[0] == "m":
            split_line = line.split(' ')
            num_crates = int(split_line[1])
            from_stack = int(split_line[3])
            to_stack = int(split_line[5])
            
            insertion_list = []
            for i in range(num_crates):
                popped_crate = stacks[from_stack].pop()
                insertion_list.insert(0, popped_crate)
            stacks[to_stack].extend(insertion_list)


final_string = ''
for stack in stacks:
    final_string += stacks[stack][-1]

 
print(final_string)