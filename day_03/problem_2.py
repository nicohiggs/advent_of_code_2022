import string

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_03\\input.txt") as f: 
    lines = f.readlines() 
 
alphabet = list(string.ascii_letters)
letter_priority = 1
letter_table = {}
for letter in alphabet:
    letter_table[letter] = letter_priority
    letter_priority += 1

total_priority = 0
group_lines = []
for i in range(0, len(lines), 3):
    group_lines = [
        lines[i].rstrip(), lines[i+1].rstrip(), lines[i+2].rstrip()
    ]
    item_table_1 = {}
    for char in group_lines[0]:
        if char not in item_table_1:
            item_table_1[char] = 1
    item_table_2 = {}
    for char in item_table_1:
        if char in group_lines[1]:
            if char not in item_table_2:
                item_table_2[char] = 1
    for char in item_table_2:
        if char in group_lines[2]:
            total_priority += letter_table[char]
            break
 
print(total_priority)