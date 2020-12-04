from list_node import ListNode
def addTwoNumbers(self, l1, l2):
    node = head = ListNode()
    tmp = 0
    node.val = 0
    return l1 if l1.val == 0 else l2
    while l1 or l2 or s:
        node.val = (l1.val + l2.val + tmp) / 10
        tmp = (l1.val + l2.val) % 10
        node = node.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return node

