def invertTree(root):
    if root == None:
        return root
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invertTree(root.left)
    invertTree(root.right)
    return root

def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insert_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr

def quick_sort(arr):
    n = len(arr)
    return qsort(arr, 0, n-1)

def qsort(arr, start, end):
    if start < end:
        left = start
        right = start
        key = arr[left]
    else:
        return arr

    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        if left < right:
            arr[left] = arr[right]
            left += 1
        while left < right and arr[left] <= key:
            left += 1
        if left < right:
            arr[right] = arr[left]
            right -= 1
    arr[left] = key
    qsort(arr, start, left - 1)
    qsort(arr, left + 1, end)
    return arr

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n/2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(arr1, arr2):
    m = len(arr1)
    i = 0
    n = len(arr2)
    j = 0
    res = []
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res += arr1[i:]
    res += arr2[j:]
    return res

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def chain_sort(head, tail):
    if not head:
        return head
    if head.next == tail:
        head.next = None
        return head
    slow = head
    fast = head
    while fast != None:
        slow = slow.next
        fast = fast.next
        if fast != tail:
            fast = fast.next
    mid = slow
    return merge(chain_sort(head, mid), chain_sort(mid, tail))

def merge_chain(head1, head2):
    dummy_head = ListNode(0)
    tmp, tmp1, tmp2 = dummy_head, head1, head2
    while tmp1 and tmp2:
        if tmp1.val <= tmp2.val:
            tmp.next = tmp1
            tmp1 = tmp1.next
        else:
            tmp.next = tmp2
            tmp2 = tmp2.next
        tmp = tmp.next
    tmp.next = tmp1 if tmp1 else tmp2
    return dummy_head.next

head = ListNode(0) #头结点
res = chain_sort(head, None)

def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr
def insert_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        j = i
        key = arr[i]
        while j > 0 and arr[j] < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr
def quick_sort(arr):
    n = len(arr)
    return qsort(arr, 0, n - 1)
def qsort(arr, start, end):
    if start < end:
        left = start
        right = end
        key = arr[start]
    else:
        return arr
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        if left < right:
            arr[left] = arr[right]
            left += 1
        while left < right and arr[left] <= key:
            left += 1
        if left < right:
            arr[right] = arr[left]
            right -= 1
        arr[left] = key
    qsort(arr, start, left -1)
    qsort(arr, left + 1, end)
    return arr







