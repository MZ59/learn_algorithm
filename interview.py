# L(p, p`)= -(a(1-p`)^b*plog(p`) + (1-a)p`^b(1-p)log(1-p'))

# 数组，数组判断分成两部分，和相等

def  solution(ini_arr):
    n = len(ini_arr)
    total = sum(ini_arr)
    if total % 2 != 0:
        return False
    tgt = total // 2
    ini_arr.sort()
    for i in range(n):
        if sum(ini_arr[:i]) < tgt:
            continue
        elif sum(ini_arr[:i]) == tgt:
            return True
        else:
            return False

if __name__ == '__main__':
    print(solution([1,5,11,5,2,2]))
