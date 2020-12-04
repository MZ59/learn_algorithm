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
c.next = d
d.next = e
e.next = f
# f.next = d

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
        fast = fast.next.next
        slow = slow.next
    return slow


def if_same(l1, l2):
    while l1 and l2:
        if l1.val == l2.val:
            l1 = l1.next
            l2 = l2.next
        else:
            return False
    return True


def reverse(head):
    if not head:
        return head
    pre = None
    while head:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre

def split_chain(head):
    cur = head
    # one_head = cur
    copy_head = cur.next
    while cur and cur.next:
        tmp = cur.next
        cur.next = cur.next.next
        cur = tmp
    return copy_head, head


# test = ListNode(1)
# test_2 = ListNode(2)
# test.next = test_2
# import pdb;pdb.set_trace()
# middle = find_middle(test)
# tail = middle.next
# middle.next = None
# r_tail = reverse(tail)
# print(if_same(test, r_tail))

# 1-->4-->3-->2-->5-->7
# import pdb;pdb.set_trace()
l1, l2 = split_chain(a)
print(v(l1))
print(v(l2))