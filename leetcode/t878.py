'''
    y = x//a + x//b - x//lcm(a,b)
    小于等于x的数中能被a或b整除的个数 = 小于等于x的数中能被a整除的个数 + 小于等于x的数中能被a整除的个数 - 小于等于x的数中能被a和b整除的个数
'''

def solution(n, a, b):
    left = min(a, b)
    right = n * min(a, b)
    c = lcm(a, b)  # 最小公倍数
    while left <= right:
        mid = (left + right) // 2
        cnt = mid // a + mid // b - mid // c
        if cnt >= n:
            right = mid - 1
        else:
            left = mid + 1

    return (right + 1) % (10 ** 9 + 7)