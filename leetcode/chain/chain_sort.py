class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        def sortFunc(head, tail):
            if not head:
                return head
            if head.next == tail: #列表中只有一个节点
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow # 找到链表的中间节点
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1, head2):
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)

def sortList(head, tail = None):
    if not head:
        return head
    if head.next == tail:
        head.next = None
        return head
    slow = head
    fast = head
    while fast != tail:
        slow = slow.next
        fast = fast.next
        if fast != tail:
            fast = fast.next
    mid = slow
    return merge(sortList(head, mid), sortList(mid, tail))

def merge(head1, head2):
    dummyNode = ListNode(0)
    tmp, tmp1, tmp2 = dummyNode, head1, head2
    while tmp1 and tmp2:
        if tmp1.val <= tmp2.val:
            tmp.next = tmp1
            tmp1 = tmp1.next
        else:
            tmp.next = tmp2
            tmp2 = tmp2.next
        tmp = tmp.next
    if tmp1:
        tmp.next = tmp1
    if tmp2:
        tmp.next = tmp2
    return dummyNode.next


