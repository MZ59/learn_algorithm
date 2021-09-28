
def solution(nums):
    res = []
    n = len(nums)
    def mine_sort(first=0):
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            mine_sort(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    mine_sort()
    return res

print(solution([1,2,3,4]))
