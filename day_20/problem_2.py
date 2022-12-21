class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_20\\input.txt") as f: 
    lines = f.readlines()

decryption_key = 811589153
len_list = len(lines)-1
original_order_table = {}
i = 0
for line in lines:
    line = int(line.rstrip())
    original_order_table[i] = Node(line*decryption_key)
    i += 1

for node_idx in original_order_table:
    if node_idx == 0:
        original_order_table[node_idx].next = original_order_table[node_idx+1]
        original_order_table[node_idx].prev = original_order_table[len(original_order_table)-1]
    elif node_idx == len(original_order_table)-1:
        original_order_table[node_idx].next = original_order_table[0]
        original_order_table[node_idx].prev = original_order_table[node_idx-1]
    else:
        original_order_table[node_idx].next = original_order_table[node_idx+1]
        original_order_table[node_idx].prev = original_order_table[node_idx-1]
    
    if original_order_table[node_idx].data == 0:
        zero_node = original_order_table[node_idx]

for _ in range(10):
    for node_idx in original_order_table:
        moving_node = original_order_table[node_idx]
        steps = moving_node.data
        if steps > 0:
            for i in range(steps % len_list):
                next_node = moving_node.next
                prev_node = moving_node.prev
                # update moving node
                moving_node.next = next_node.next
                next_node.next.prev = moving_node
                moving_node.prev = next_node
                # update original next node
                next_node.next = moving_node
                next_node.prev = prev_node
                # update original prev node
                prev_node.next = next_node
        elif steps < 0:
            for i in range(-steps % len_list):
                next_node = moving_node.next
                prev_node = moving_node.prev
                # update moving node
                moving_node.next = prev_node
                moving_node.prev = prev_node.prev
                prev_node.prev.next = moving_node
                # update original prev node
                prev_node.next = next_node
                prev_node.prev = moving_node
                # update original next node
                next_node.prev = prev_node

curr_node = zero_node
grove_sum = 0
for i in range(1, 3001):
    curr_node = curr_node.next
    if i % 1000 == 0:
        print(curr_node.data)
        grove_sum += curr_node.data
print(grove_sum)