# -*- coding: utf-8 -*-
from numpy import *

def pro_transfer(a):  # 构建概率转移矩阵
    b = transpose(a)  # b为a的转置矩阵
    c = zeros((a.shape), dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if b[j].sum() > 0:
                c[i][j] = a[i][j] / (b[j].sum())
            else:
                c[i][j] = 0.0
    print("=================概率转移矩阵==================")
    print(c)
    return c


def init_pr(M):  # PageRank值初始化
    pr = zeros((M.shape[0], 1), dtype=float)  # 构造一个存放pr值得矩阵
    for i in range(M.shape[0]):
        pr[i] = float(1) / M.shape[0]

    print("==================初始pr====================")
    print(pr)
    return pr

def page_rank(m, v):  # 计算pageRank值

    # while ((v == dot(m, v)).all() == False):
    #判断pr矩阵是否收敛,(v == dot(m, v)).all()判断前后的pr矩阵是否相等，若相等则停止循环
    v = dot(m, v)
    return v


def page_rank_d(d, m, v):  # 计算pageRank值,增加阻尼系数

    # while ((v == d * dot(m, v) + (1 - d) / m.shape[0]).all() == False):
        # 判断pr矩阵是否收敛,(v == d * dot(m, v) + (1 - d) / m.shape[0]).all()判断前后的pr矩阵是否相等，若相等则停止循环
    v = d * dot(m, v) + (1 - d) / m.shape[0]
    return v


if __name__ == "__main__":
    a_matrix = array([[0, 0, 0, 1],
                      [1, 0, 0, 1],
                      [1, 0, 1, 0],
                      [1, 1, 0, 1]], dtype=float)  # 构建邻接矩阵
    M = pro_transfer(a_matrix)  # 构建概率转移矩阵
    pr = init_pr(M)
    d = 0.85  # 阻尼系数
    for i in range(100):
        pr = page_rank(M, pr)
        print("===============no d, round %s===================" % str(i+1))
        print(pr)  # 计算pr值,无阻尼系数
    # for i in range(10):
    #     pr = page_rank_d(d, M, pr)
    #     print("===============with d, round %s===================" % str(i + 1))
    #     print(pr)# 计算pr值,有阻尼系数