
def solution(nums, queries):
    n = len(nums)
    dp = [[0] * 101 for _ in range(n + 1)]
    # 前缀和记录每个数在区间内出现的次数
    for i in range(n):
        for j in range(1, 101):
            dp[i + 1][j] = dp[i][j]
            dp[i + 1][nums[i]] += 1

    res = [-1] * len(queries)
    # 顺序查询
    for i, (l, r) in enumerate(queries):
        minv = float("inf") #极大值
        pre = -float("inf") #极小值
        # 判断区间内是否有不同数字出现
        for j in range(1, 101):
            if dp[r + 1][j] - dp[l][j] > 0:
                minv = min(minv, j - pre)
                pre = j
        # 区间内存在不同的数字 
        if minv != float("inf"):
            res[i] = minv

    return res


if __name__ == '__main__':
    nums = [1, 3, 4, 8]
    queries = [[0,1],[1,2],[2,3],[0,3]]
    print(solution(nums, queries))
