'''
    从给定列表中找到目标值得索引
'''

def binary_search_ini(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


arr = [1, 2,4,5, 7, 9, 10, 17]
target = 10
# import pdb;pdb.set_trace()
print(binary_search_ini(arr, target))