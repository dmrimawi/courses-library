from linkedlist import LinkedList

def is_circular(head):
    if head is None:
        return False
    temp = head.next
    while temp is not None and temp is not head:
        temp = temp.next
    return temp is head

ls = LinkedList()

ls.insert_at_start(5)
ls.insert_at_start(7)
ls.insert_at_start(90)
ls.insert_at_start(54)
ls.insert_at_start(60)
ls.insert_at_start(10)

print(ls)
print(is_circular(ls.head))
