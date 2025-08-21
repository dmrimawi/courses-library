from linkedlist import LinkedList


def find_the_middle_count(ls: LinkedList):
    length = ls.length()
    curr = ls.head
    count = 0
    while count < length // 2:
        count += 1
        curr = curr.next
    return curr

def find_the_middle_pointers(ls: LinkedList):
    curr = ls.head
    double_curr = ls.head
    while double_curr is not None and double_curr.next is not None:
        curr = curr.next
        double_curr = double_curr.next.next
    return curr

def merge_two_lists(ls1: LinkedList, ls2: LinkedList):
    new_lst = LinkedList()
    head_ls1 = ls1.head
    head_ls2 = ls2.head
    while head_ls1 is not None and head_ls2 is not None:
        if head_ls1.data <= head_ls2.data:
            new_lst.insert_at_end(head_ls1.data)
            head_ls1 = head_ls1.next
        else:
            new_lst.insert_at_end(head_ls2.data)
            head_ls2 = head_ls2.next
    not_empty_lst = head_ls1
    if not_empty_lst is None:
        not_empty_lst = head_ls2
    while not_empty_lst is not None:
        new_lst.insert_at_end(not_empty_lst.data)
        not_empty_lst = not_empty_lst.next
    return new_lst

def remove_duplicates(ls: LinkedList):
    curr = ls.head
    while curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
            continue
        curr = curr.next
    return ls

def reverse_linked_list(ls: LinkedList):
    first = None
    curr = ls.head
    while curr is not None:
        temp = curr.next
        curr.next = first
        first = curr
        curr = temp
    ls.head = first
    return ls


ls = LinkedList()

ls.insert_at_start(5)
ls.insert_at_end(7)
ls.insert_at_end(90)
ls.insert_at_index(12, 2)
ls.insert_at_index(8, 2)
ls.insert_at_index(8, 2)
ls.insert_at_index(8, 2)
ls.insert_at_index(54, 6)
ls.insert_at_index(4, 0)

ls2 = LinkedList()
ls2.insert_at_end(0)
ls2.insert_at_end(2)
ls2.insert_at_end(3)
ls2.insert_at_end(9)
ls2.insert_at_end(10)

print(ls2)

print(ls)
print(find_the_middle_count(ls))
print(find_the_middle_pointers(ls2))
ls3 = merge_two_lists(ls, ls2)
print(ls3)
remove_duplicates(ls3)
print(ls3)
reverse_linked_list(ls3)
print(ls3)
