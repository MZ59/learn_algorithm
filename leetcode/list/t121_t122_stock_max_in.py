def solution(prices):
    min_price = 100000000
    max_in = 0
    for p in prices:
        max_in = max(p - min_price, max_in)
        min_price = min(p, min_price)
    return max_in


def solution2(prices):
    max_in = 0
    tmp_in = 0
    for i in range(1, len(prices)):
        tmp_in = prices[i] - prices[i-1]
        if tmp_in > 0:
            max_in += tmp_in
    return max_in
