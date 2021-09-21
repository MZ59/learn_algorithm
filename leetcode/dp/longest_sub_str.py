def longest_sub_str(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    res = [[0 for i in range(len2+1)] for j in range(len1+1)]
    result = 0
    index = 0
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i-1] == str2[j-1]:
                res[i][j] = res[i-1][j-1] + 1
                if result < res[i][j]:
                    result = res[i][j]
                    index = i

    return result, str1[index-result :index]


'''
    初始矩阵
 | # a b c d
-|-----------
#| 0 0 0 0 0
a| 0 0 0 0 0
b| 0 0 0 0 0
e| 0 0 0 0 0
'''
lens, ss = longest_sub_str("abcd", "abe")
print(lens)
print(ss)
