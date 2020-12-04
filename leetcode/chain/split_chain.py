class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 3-->2-->4-->1-->5-->6
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

def v(node):
    r = []
    while node:
        r.append(node.val)
        node = node.next
    return r

def split_chain(head, x):
    if not head:
        return head
    up_head = up = ListNode(None)
    down_head = down = ListNode(None)
    # import pdb;pdb.set_trace()
    while head:
        if head.val < x:
            up.next = head
            up = up.next
        else:
            down.next = head
            down = down.next
        head = head.next

    import pdb;pdb.set_trace()
    down.next = None #最后一个down.next = 小于x的数，等同于up
    # up = None
    up.next = down_head.next
    return up_head.next

result = split_chain(a, 3)
print(v(result))

