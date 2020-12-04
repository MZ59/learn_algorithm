def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(m + 1):
        dp[0][i] = i
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1)
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    # import pdb;pdb.set_trace()
    return dp[n][m]


print(edit_distance("你好", "你好个屁"))


