'''
    冒泡排序：从最左边开始，比较相邻两个元素，交换位置
    从左往右。左边数大于右边数，左右互换，这样最大的数会先冒泡到最右边位置
'''


def bubbleSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubbleSort(arr):
    n = len(arr)
    if n < 1:
        return arr
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



def bubbleSort_ini(arr):
        n = len(arr)
        if n <= 1:
            return arr
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
arr = [2,6,1,5,3]
# import pdb;pdb.set_trace()
print(bubbleSort(arr))
# bubbleSort(arr)