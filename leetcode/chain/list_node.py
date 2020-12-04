class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1-->4-->3-->2-->5-->2
a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f