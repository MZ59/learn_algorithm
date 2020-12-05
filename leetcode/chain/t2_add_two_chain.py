from list_node import ListNode
def addTwoNumbers(l1, l2):
    head = ListNode(None)
    tail = head  # tail和head头结点，tail用来游走遍历，head返回最终结果
    tmp = 0
    while l1 or l2 or tmp != 0:  # tmp != 0, 原因，可能要使得最后一位加一
        n1 = l1.val if l1 is not None else 0
        n2 = l2.val if l2 is not None else 0
        sum_v = n1 + n2 + tmp
        tail.next = ListNode((sum_v) % 10)
        tmp = (sum_v) // 10
        tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return head.next

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

