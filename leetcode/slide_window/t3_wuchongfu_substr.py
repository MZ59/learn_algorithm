def length_substr(s):
    n = len(s)
    index_r = -1
    ans = 0
    sub_str = set()
    for i in range(n):
        if i != 0:  # 左指针左移
            sub_str.remove(s[i - 1])

        while index_r + 1 < n and s[index_r + 1] not in sub_str:  # 右指针右
            sub_str.add(s[index_r + 1])
            index_r += 1
        ans = max(ans, index_r - i + 1)
    return ans


