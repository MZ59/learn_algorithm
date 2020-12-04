def two_sum(nums, target):
    dict = {}
    for i, v in enumerate(nums):
        if target - v in dict:
            return[dict[target - v], i]
        dict[v] = i

