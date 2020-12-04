class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1-->4-->3-->2-->5-->7
a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(7)

a.next = b
b.next = c
# c.next = d
d.next = e
e.next = f

def v(node):
    r = []
    while node:
        r.append(node.val)
        node = node.next
    return r

def merge_list(l1, l2):
    dummy = head = ListNode(None)
    change = 1
    while l1 and l2:
        if change == 1:
            head.next = l1
            l1 = l1.next
            change = 2
        else:
            head.next = l2
            l2 = l2.next
            change = 1
        head = head.next
    head.next = l1 if l1 else l2
    return dummy.next

import pdb;pdb.set_trace()
merge_list(a, d)