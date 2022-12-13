import copy

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_13\\input.txt") as f: 
    lines = f.readlines()

def compare(left, right):

    if not (isinstance(left, list) or isinstance(right, list)):
        if left == right:
            return "equals"
        elif left < right:
            return "left"
        else:
            return "right"
    elif isinstance(left, list) and isinstance(right, list):
        result = "equals"
        while result == "equals":
            if len(left) == 0 and len(right) > 0:
                return "left"
            elif len(right) == 0 and len(left) > 0:
                return "right"
            elif len(left) == 0 and len(right) == 0:
                return "equals"
            result = compare(left.pop(0), right.pop(0))
        return result
    else:
        if not isinstance(left, list):
            left = [left]
        else:
            right = [right]
        return compare(left, right)

packets = []
for line in lines:
    line = line.rstrip()
    if line == '':
        pass
    else:
        packets.append(eval(line))
packets.append([[2]])
packets.append([[6]])

# bubble sort!
for i in range(len(packets) - 1):
    for j in range(len(packets) - 1):
        result = compare(copy.deepcopy(packets[j]), copy.deepcopy(packets[j+1]))
        if result == "right":
            # we need to swap
            temp = packets[j]
            packets[j] = packets[j+1]
            packets[j+1] = temp

for i in range(len(packets)):
    if packets[i] == [[2]]:
        idx_2 = i + 1
    elif packets[i] == [[6]]:
        idx_6 = i + 1
print(idx_2 * idx_6)