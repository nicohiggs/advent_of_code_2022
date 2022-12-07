class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def compute_directory_size(node):
    split_name = node.name.split(' ')
    if len(split_name) == 2: # ['123', 'filename']
        return int(split_name[0])
    else:
        dir_size = 0
        dir_name = split_name[0]
        for child_node in node.children:
            dir_size += compute_directory_size(child_node)
        if dir_name in dir_sizes:
            for i in range(100):
                new_name = dir_name + str(i)
                if new_name not in dir_sizes:
                    dir_name = new_name
                    break
        dir_sizes[dir_name] = dir_size
        return dir_size

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_07\\input.txt") as f: 
    lines = f.readlines() 

root_node = Node("/")
current_node = root_node
for line in lines:
    line = line.rstrip()
    if line[:4] == "$ cd":
        # update current node
        if line[5:] == "..":
            current_node = current_node.parent
        elif line[5:] == "/":
            current_node = root_node
        else:
            dir_name = line[5:]
            for child in current_node.children:
                if dir_name == child.name:
                    current_node = child
                    break
    elif line[:4] == "$ ls":
        # do nothing as the next lines we loop will be added as children
        pass
    elif line[:3] == "dir":
        dir_name = line[4:]
        dir_already_exists = False
        for child in current_node.children:
            if child.name == dir_name:
                print('uh oh')
                dir_already_exists = True
        if not dir_already_exists:
            new_node = Node(name=dir_name, parent=current_node)
            current_node.add_child(new_node)
    else: # file size and file name case
        new_node = Node(name=line, parent=current_node)
        current_node.add_child(new_node)

dir_sizes = {}
root_size = compute_directory_size(root_node)

total_less_than = 0
for directory in dir_sizes:
    dir_size = dir_sizes[directory]
    if dir_size <= 100000:
        total_less_than += dir_size
print(total_less_than)