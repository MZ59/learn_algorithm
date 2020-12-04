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
f = ListNode(7)

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

def find_middle(head):
    fast = head.next
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_list(l1, l2):
    dummy = head = ListNode(None)
    change = 1
    while l1 or l2:
        if change == 1:
            head.next = l1
            l1 = l1.next
            change = 2
        else:
            head.next = l2
            l2 = l2.next
            change = 1
        head = head.next
    # change = !change

    head.next = l1 if l1 else l2
    return dummy.next

def reverse_list(l):
    pre = ListNode(None)
    while l:
        tmp = l.next
        l.next = pre
        pre = l
        l = tmp

    return pre

print(v(a))
middle = find_middle(a)
import pdb;pdb.set_trace()
down = middle.next
middle.next = None
down_l = reverse_list(down)
res = merge_list(a, down_l)
print(v(res))
