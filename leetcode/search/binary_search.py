'''
    从给定列表中找到目标值得索引
'''

def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid



def binary_search_ini(arr, target):
    n = len(arr)
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return None

arr = [2,4,1,3,5, 7, 6]
target = 5
# import pdb;pdb.set_trace()
print(binary_search(arr, target))