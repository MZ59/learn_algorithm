def longestValidParentheses(s):
      stack = list()
      res = 0
      for i, k in  enumerate(s):
          if stack and k == ')' and s[stack[-1]] == '(':
              stack.pop()
              res = max(res, i-(stack[-1]if stack else -1))
          else:
              stack.append(i)
      return res
