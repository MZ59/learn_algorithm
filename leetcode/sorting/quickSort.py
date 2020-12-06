def QuickSort(arr):
    def partiton(arr, left, right):
        key = left
        while left < right:
            while left < right and arr[left] < arr[key]:
                left += 1
            while left < right and arr[right] > arr[key]:
                right -= 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[key] = arr[key], arr[left]
        return left

    def qsort(arr, left, right):
        if left >= right:
            return
        mid = partiton(arr, left, right)
        qsort(arr, left, mid - 1)
        qsort(arr, mid + 1, right)

    n = len(arr)
    if n <= 1:
        return arr
    qsort(arr, 0, n -1)
    return arr


def QuickSort_ini(arr):
    def partition(arr, left, right):
        key = left
        while left < right:
            while left < right and arr[right] >= arr[key]:
            # while arr[right] >= arr[key]:
                right -= 1
            while left < right and arr[left] <= arr[key]:
            # while arr[left] <= arr[key]:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[key], arr[left] = arr[left], arr[key]
        return left

    def quickSort(arr, left, right):
        if left >= right:
            return
        mid = partition(arr, left, right)
        quickSort(arr, left, mid - 1)
        quickSort(arr, mid + 1, right)

    n = len(arr)
    if n <= 1:
        return arr
    quickSort(arr, 0, n -1)
    return arr

arr = [2,6,1,5,3]
print(QuickSort(arr))

