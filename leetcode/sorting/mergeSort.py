def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = int(n / 2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(arr1, arr2):
    i = 0
    m = len(arr1)
    j = 0
    n = len(arr2)
    res = []
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            res.append(arr2[j])
            j += 1
    res += arr1[i:]
    res += arr2[j:]
    return res

arr = [2,6,1,5,3]
print(mergeSort(arr))