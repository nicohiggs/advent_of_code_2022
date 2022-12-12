import time
# import numpy as np

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_11\\input.txt") as f: 
    lines = f.readlines()

def perform_round(monkeys, fixit_number):
    for curr_monkey in monkeys:
        for old in monkeys[curr_monkey]["items"]:
            new_item = eval(monkeys[curr_monkey]["operation"])
            new_item = new_item % fixit_number
            # new_item = new_item // 3
            if (new_item % monkeys[curr_monkey]["test"]) == 0:
                true_monkey = monkeys[curr_monkey]["true_monkey"]
                monkeys[true_monkey]["items"].append(new_item)
            else:
                false_monkey = monkeys[curr_monkey]["false_monkey"]
                monkeys[false_monkey]["items"].append(new_item)
            monkeys[curr_monkey]["num_inspected"] += 1
        # 'clean up' this monkeys items (remove them since he threw them all away)
        monkeys[curr_monkey]["items"] = []

    return monkeys

curr_monkey = 0
monkeys = {}
for line in lines:
    line = line.strip()
    if line == '':
        pass
    else:
        if line[0] == "M": # monkey
            curr_monkey = int(line[7])
            monkeys[curr_monkey] = {
                "items": [],
                "operation": "",
                "test": "",
                "true_monkey": None,
                "false_monkey": None,
                "num_inspected": 0
            }
        elif line[0] == "S": # starting items
            split_line = line.split(' ')
            for item in split_line[2:]:
                item = item.replace(',', '') # drop the comma
                monkeys[curr_monkey]["items"].append(int(item))
        elif line[0] == "O": # operation
            monkeys[curr_monkey]["operation"] = line[17:] # e.g. "old + 3"
        elif line[0] == "T": # test
            split_line = line.split(' ')
            monkeys[curr_monkey]["test"] = int(split_line[-1])
        elif line[3] == "t": # true case
            split_line = line.split(' ')
            monkeys[curr_monkey]["true_monkey"] = int(split_line[-1])
        else: # false case
            split_line = line.split(' ')
            monkeys[curr_monkey]["false_monkey"] = int(split_line[-1])

fixit_number = 1
for monkey in monkeys:
    fixit_number *= monkeys[monkey]["test"]
print(fixit_number)

num_rounds = 10000
for i in range(num_rounds):
    monkeys = perform_round(monkeys, fixit_number)

if monkeys[0]["num_inspected"] > monkeys[1]["num_inspected"]:
    two_most_active = (0, 1)
else:
    two_most_active = (1, 0)
for curr_monkey in range(2, len(monkeys)):
    if monkeys[curr_monkey]["num_inspected"] > monkeys[two_most_active[0]]["num_inspected"]:
        two_most_active = (curr_monkey, two_most_active[0])
    elif monkeys[curr_monkey]["num_inspected"] > monkeys[two_most_active[1]]["num_inspected"]:
        two_most_active = (two_most_active[0], curr_monkey)

monkey_business = monkeys[two_most_active[0]]["num_inspected"] * monkeys[two_most_active[1]]["num_inspected"]

print(monkey_business)