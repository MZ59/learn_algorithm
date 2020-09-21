# 熵
import numpy as np
from collections import Counter
import math


def entropy(x, sample_weight=None):
    x = np.asarray(x)
    # x中元素个数
    x_num = len(x)
    # 如果sample_weight为None设均设置一样
    if sample_weight is None:
        sample_weight = np.asarray([1.0] * x_num)
    x_counter = {}
    weight_counter = {}
    # 统计各x取值出现的次数以及其对应的sample_weight列表
    for index in range(0, x_num):
        x_value = x[index]
        if x_counter.get(x_value) is None:
            x_counter[x_value] = 0
            weight_counter[x_value] = []
        x_counter[x_value] += 1
        weight_counter[x_value].append(sample_weight[index])

    # 计算熵， ent = sum(-P(x_i) + log(P(x_i)))
    ent = .0
    for key, value in x_counter.items():
        p_i = 1.0 * value * np.mean(weight_counter.get(key)) / x_num # x_i的概率
        ent += -p_i * math.log(p_i)
    return ent
# import pdb;pdb.set_trace()
# entropy([1, 2, 1])

# 条件熵 H(Y|X) = sum( P(x_i) * H(Y|x_i))
def cond_entropy(x, y,sample_weight=None):
    """
    计算条件熵:H(y|x)
    """
    x=np.asarray(x)
    y=np.asarray(y)
    # x中元素个数
    x_num = len(x)
    #如果sample_weight为None设均设置一样
    if sample_weight is None:
        sample_weight=np.asarray([1.0]*x_num)
    # 计算
    ent = .0
    for x_value in set(x):
        x_index=np.where(x==x_value)
        new_x=x[x_index]
        new_y=y[x_index]
        new_sample_weight=sample_weight[x_index]
        p_i=1.0*len(new_x)/x_num
        ent += p_i * entropy(new_y,new_sample_weight)
    return ent

import pdb;pdb.set_trace()
cond_entropy([1,2,1],[1,2,3])

# 信息增益
def muti_info(x, y,sample_weight=None):
    """
    互信息/信息增益:H(y)-H(y|x)
    """
    x_num=len(x)
    if sample_weight is None:
        sample_weight=np.asarray([1.0]*x_num)
    return entropy(y,sample_weight) - cond_entropy(x, y,sample_weight)
