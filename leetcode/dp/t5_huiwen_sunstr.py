def longestPalindrome(s):
    size = len(s)
    if size == 1:
        return s
    dp = [[False for i in range(size)] for j in range(size)]
    max_len = 1
    start = 0
    for i in range(size):
        dp[i][i] = True
    for j in range(1, size):
        for i in range(j):
            if j-1 - (i+ 1) <= 0: # 如果掐头去尾只有一个字符
                if s[i] == s[j]: # 若头尾相同
                    dp[i][j] = True
                    cur_len = j-i+1
                else: # 掐头去尾还有多个字符
                    if s[i] == s[j] and dp[i+1][j-1]: # 若头尾相同，且掐头去尾后还是回文
                        dp[i][j] = True
                        cur_len = j-i+1
            if dp[i][j]:
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start:start+max_len], dp

a = "bb"
ss, dp = longestPalindrome(a)
print(ss)
print(dp)