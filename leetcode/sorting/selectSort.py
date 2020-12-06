'''
    选择排序：从基准元素后边选择比基准元素小的元素，与基准元素交换
    从最左边开始最为基准元素，选择基准元素之后最小的数，与基准元素交换，最小的 会首先排到左边
'''

def selectSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr




def selectSort_ini(arr):
    n = len(arr)
    for i in range(n-1): # 基准元素从零开始，直到末尾的前一个
        min_index = i
        for j in range(i + 1, n): # 待比较元素从i + 1开始，知道末尾
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [2,6,1,5,3]
print(selectSort(arr))

