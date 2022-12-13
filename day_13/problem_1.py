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

total_idx_correct = 0
for i in range(0, len(lines), 3):
    left = eval(lines[i].rstrip())
    right = eval(lines[i+1].rstrip())
    
    result = compare(left, right)
    print(result)
    if result == "left":
        total_idx_correct += (i/3) + 1
print(total_idx_correct)