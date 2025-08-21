size = 50

mem = [-1] * size


def initalize():
    for i in range(size):
        mem[i] = -1
    mem[0] = 0

def free_list(lid):
    while lid + 1 < size and mem[lid + 1] != -1:
        mem[lid] = -1
        mem[0] = mem[lid + 1]
        mem[lid + 1] = -1
        lid = mem[0]
    mem[0] = 0

def print_list(lid):
    while lid + 1 < size:
        if mem[lid] == -1:
            break
        print(f"[{mem[lid]}] ", end="->")
        lid = mem[lid + 1]
    print(" -1")

def new_node():
    for i in range(1, size, 2):
        if i + 1 < size and mem[i] == -1 and mem[i + 1] == -1:
            return i
    return -1

def insert(lid, data):
    # Find last index in list - lid
    while lid + 1 < size and mem[lid + 1] != -1:
        lid = mem[lid + 1]
    # Find next empty slot index
    if mem[lid] == -1:
        mem[lid] = data
    else:
        mem[lid + 1] = new_node()
        if mem[lid + 1] != -1:
            mem[mem[lid + 1]] = data
        else:
            print("Memory is FULL!")

def delete_node_by_data(lid, data):
    while lid + 1 < size and mem[lid + 1] != -1:
        if mem[lid] == data:
            mem[mem[0] + 1] = mem[lid + 1]
            mem[lid] = -1
            mem[lid + 1] = -1
            mem[0] = 0
            return
        mem[0] = lid # previous
        lid = mem[lid + 1]

initalize()
l1 = new_node()
insert(l1, 5)
insert(l1, 10)
insert(l1, 5)
insert(l1, 5)
print_list(l1)
print(mem)

l2 = new_node()
insert(l2, 6)
insert(l2, 6)
insert(l2, 6)
insert(l2, 6)
print_list(l2)
print(mem)

l3 = new_node()
insert(l3, 7)
insert(l3, 7)
insert(l3, 7)
insert(l3, 7)
print_list(l3)
print(mem)

free_list(l2)
print(mem)
print_list(l1)
print_list(l2)
print_list(l3)

l4 = new_node()
insert(l4, 1)
insert(l4, 2)
insert(l4, 3)
insert(l4, 1)
insert(l4, 2)
insert(l4, 3)
print_list(l4)
delete_node_by_data(l4, 3)
print_list(l4)
print(mem)
