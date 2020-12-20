def sequentSearch(arr, target):
    n = len(arr)
    if n <= 0:
        return False
    for i in range(n):
        if arr[i] == target:
            return i
    return False

arr = [2,4,5,3,7]
target = 5
print(sequentSearch(arr, target))