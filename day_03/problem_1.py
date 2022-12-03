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
for line in lines:
    line = line.rstrip()
    len_of_first_compartment = len(line) // 2
    item_table = {}
    for char in line[:len_of_first_compartment]:
        if char in item_table:
            pass
        else:
            item_table[char] = 1
    for char in line[len_of_first_compartment:]:
        if char in item_table:
            total_priority += letter_table[char]
            break
 
print(total_priority)