def maxSubArray(nums):
    m = len(nums)
    dp = [0 for i in range(m)]
    index_dp = [0 for i in range(m)]
    dp[0] = nums[0]
    for i in range(1, m):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

        if dp[i - 1] < 0: # 当前元素之前元素和小于0，则从当前元素开始计算接下来列表的元素和
            index_dp[i] = i
        else:
            index_dp[i] = index_dp[i - 1]
    sum_max = max(dp)
    index_max = dp.index(sum_max)
    sub_list = nums[index_dp[index_max]: index_max + 1]
    return max(dp), sub_list