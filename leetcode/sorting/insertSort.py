'''
    插入排序：目标元素左边的列表是有序的，把目标元素插入有序列表中指定位置
    左边元素是排好的元素，从右边开始选一个元素插入到排好的元素里
'''

def insertSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        target = arr[i]
        j = i
        while j > 0 and target < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = target
    return arr

def insertSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        j = i
        target = arr[j]
        while j > 0 and target < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = target
    return arr



def insertSort_ini(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n): # 从无序序列的第一个开始
        j = i
        target = arr[i] # 待插入元素
        while j > 0 and target < arr[j - 1]: # target > arr[j - 1]时，待插入序列已经排好序
            arr[j] = arr[j - 1] # 大的元素后移
            j = j - 1
        arr[j] = target
    return arr

arr = [2,6,1,5,3]
print(insertSort(arr))


def insertSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0 and key < arr[j-1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key
    return arr
