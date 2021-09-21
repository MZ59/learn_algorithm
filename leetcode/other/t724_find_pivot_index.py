def pivot_index(nums):
    pre_sum = 0
    sums = sum(nums)
    n = len(nums)
    for i in range(n):
        if pre_sum == sums - pre_sum - nums[i]:
            return i
        pre_sum += nums[i]
    return -1
