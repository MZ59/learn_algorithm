def longest_sub_str(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    result = 0
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if str1[j-1] == str2[i-1]:
                res[i][j] = res[i-1][j-1]+1
                result = max(result, res[i][j])
    return result


'''
    初始矩阵
 | # a b c d
-|-----------
#| 0 0 0 0 0
a| 0 0 0 0 0
b| 0 0 0 0 0
e| 0 0 0 0 0
'''
print(longest_sub_str("abcd", "abc"))
