with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_06\\input.txt") as f: 
    lines = f.readlines() 

char_string = lines[0]
start_idx = 0
end_idx = 4
for i in range(len(char_string) - 3):
    curr_string = char_string[start_idx:end_idx]
    unique_dict = {}
    index_found = True
    for char in curr_string:
        if char in unique_dict:
            index_found = False
        else:
            unique_dict[char] = 1
    if index_found:
        break
    else:
        start_idx += 1
        end_idx += 1

print(end_idx)