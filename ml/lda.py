# lda主题模型

import numpy as np
# import seaborn as sns

'''
    V: money, loan, bank, river, stream
    T: T1, T2
    P(money|T1) = 1/3, P(load|T1) = 1/3, P(bank|T1) = 1/3
    P(bank|T2) = 1/3, P(stream|T2) = 1/3, P(river|T2) = 1/3
'''

vocab = ["money", "loan", "bank", "river", "stream"]
z_1 = np.array([1/3, 1/3, 1/3, .0, .0])
z_2 = np.array([.0, .0, 1/3, 1/3, 1/3])

#初始化
#topic到word的分布
phi_actual = np.array([z_1, z_2]).T.reshape([len(z_2), 2])
# print(phi_actual)

# 生成文档
D = 16 # doc num
mean_length = 10 #avg word num of doces
len_doc = np.random.poisson(mean_length, size= D) # 利用泊松分布，对每个文档生成句子长度
T = 2

docs = []
orig_topics = []
for i in range(D):
    z = np.random.randint(0, 2) # 哪一个topic
    if z == 0:
        words = np.random.choice(vocab, size= (len_doc[i]), p= z_1).tolist()
    else:
        words = np.random.choice(vocab, size= (len_doc[i]), p= z_2).tolist()

    orig_topics.append(z)
    docs.append(words)
# print(orig_topics[0])
# print(docs[0])

w_i = []
i = []
d_i = []
z_i = []
counter = 0

for doc_idx, doc in enumerate(docs):
    for word_idx, word in enumerate(doc):
        w_i.append(np.where(np.array(vocab) == word)[0][0])
        i.append(counter)
        d_i.append(doc_idx)
        z_i.append(np.random.randint(0, T)) # 初始化主题分布
        counter += 1
w_i = np.array(w_i)
d_i = np.array(d_i)
z_i = np.array(z_i)
# import pdb;pdb.set_trace()

# 创建单词-话题(WT)，话题-文档(DT)分布
WT = np.zeros((len(vocab), T)) # 5 * 2, 每个话题下，不同单词出现的次数
for idx, word_ in enumerate(vocab):
    topics = z_i[np.where(w_i == idx)] # 先找出vocab中word_单词在w_i分布中的索引，在根据这些索引在主题分布中找出word_对应的主题
    for t in range(T):
        WT[idx, t] = sum(topics == t) # WT中的一行， word_这个单词对应t这个topic的总次数

DT = np.zeros((D, T)) # 16 * 2， 每个话题下，不同文档出现的次数（每个文档中，不同topic出现的次数）
for idx, doc_ in enumerate(range(D)):
    topics = z_i[np.where(d_i == idx)]
    for t in range(T):
        DT[idx, t] = sum(topics == t)

# import pdb;pdb.set_trace()

WT_orig = WT.copy()
DT_orig = DT.copy()

# LDA model
# 吉布斯采样记录仪，记录下每一个phi的变化结果？
phi_1 = np.zeros((len(vocab), 100))
phi_2 = np.zeros((len(vocab), 100))

iters = 100

# dirichlet先验分布
beta = 1.
alpha = 1.

for step in range(iters):
    for current in i:
        # 取出D和W
        doc_idx = d_i[current]
        w_idx = w_i[current]

        #将取出的D和W从总体集合中减去
        DT[doc_idx, z_i[current]] -= 1
        WT[w_idx, z_i[current]] -= 1

        #计算新的W、D分布
        prob_word = (WT[w_idx, :] + beta) / (WT[:,:].sum(axis=0) + len(vocab) * beta)
        prob_document = (DT[doc_idx, :] + alpha) / (DT.sum(axis=0) + D * alpha)
        # P(w|d) = P(w|t) * P(t|d)
        prob = prob_word *prob_document

        #更新z（topic分布）
        z_i[current] = np.random.choice([0, 1], 1, p= prob/prob.sum())[0]

        # 更新计数器
        DT[doc_idx, z_i[current]] += 1
        WT[w_idx, z_i[current]] += 1

        # 记录phi变化
        phi = WT / (WT.sum(axis= 0))

        phi_1[:, step] = phi[:, 0]
        phi_2[:, step] = phi[:, 1]


phi = WT / (WT.sum(axis= 0))
theta = DT / (DT.sum(axis= 0))
theta = theta / np.sum(theta, axis= 1).reshape(16, 1)
np.argmax(theta, axis= 1) == orig_topics
import pdb;pdb.set_trace()







