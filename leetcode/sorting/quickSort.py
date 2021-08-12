# def quickSort(arr):
#     n = len(arr)
#     return qsort(arr, 0, n-1)
#
# def qsort(arr, start, end):
#     if start < end:
#         left = start
#         right = end
#         key = arr[left]
#     else:
#         return arr
#     while left < right:
#         while left < right and arr[right] >= key:
#             right -= 1
#         if left < right:
#             arr[left] = arr[right]
#             left += 1
#         while left < right and arr[left] <= key:
#             left += 1
#         if left < right:
#             arr[right] = arr[left]
#             right -= 1
#     arr[left] = key
#     qsort(arr, start, left-1)
#     qsort(arr, left+1, end)
#     return arr

def quickSort(arr):
    n = len(arr)
    return qsort(arr, 0, n-1)

def qsort(arr, start, end):
    if start < end:
        left = start
        right = end
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
    qsort(arr, start, left-1)
    qsort(arr, left+1, end)
    return arr

arr = [2,6,1,5,3]
print(quickSort(arr))
