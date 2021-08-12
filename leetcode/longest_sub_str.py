def sub_str(str1, str2):
    # TODO 最长公共子串
    import pdb;pdb.set_trace()
    len1 = len(str1)
    len2 = len(str2)
    if len1 == 0 or len2 == 0:
        return 0
    res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    result = 0
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if str2[i - 1] == str1[j - 1]:
                res[i][j] = res[i-1][j-1] + 1
                result = max(result, res[i][j])
    return result

print(sub_str("杨倩全红婵等奥运健儿获中国青年五四奖章", "中国跳水队用3dai技术训练"))