'''
输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
'''


def decode(s):
    stack = []
    for i in s:
        stack.append(i)
    import pdb;pdb.set_trace()
    m_num = " "
    str_ = ""
    m = False
    res = ""
    while len(stack) >= 0:
        arg = stack.pop()
        if arg == "]":
            continue
        if arg == "[":
            m = True
        if arg.isalpha():
            if m:
                res = int(m_num.strip()) * str_ + res
                m_num = " "
                str_ = ""
            str_ = arg + str_
        if arg.isdigit():
            m_num = arg + m_num

# def decode(s):
#     res = ""
#     stack = []
#     m_num = " "
#     for i in s[::-1]:
#         if i == "]":
#             r = ""
#             if m_num != " ":
#                 while 1:
#                     top_n = stack.pop()
#                     if top_n != "]":
#                         r += top_n
#                     else:
#                         break
#                 # if i.isdigit():
#                 stack.append(r * int(m_num.strip()))
#                 m_num = ""
#             stack.append(i)
#         if i.isalpha(): #or i == "]":
#             stack.append(i)
#         if i == "[":
#             continue
#         if i.isdigit():
#             m_num = i + m_num
#     while len(stack) > 0:
#         top_2 = stack.pop()
#         res += top_2
#     return res

# import pdb;pdb.set_trace()
print(decode("10[bc]"))