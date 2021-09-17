from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier

X_train, Y_train = datasets.make_classification(n_samples=100,n_features=10,n_redundant=0,n_informative=1,n_clusters_per_class=1)

# gbm1 = GradientBoostingClassifier(n_estimators=50, random_state=10, subsample=0.6, max_depth=7, min_samples_split=900)
# gbm1.fit(X_train, Y_train)
# train_new_feature = gbm1.apply(X_train)
# train_new_feature = train_new_feature.reshape(-1, 50)
# for l in train_new_feature:
#     print(l)
# import pdb;pdb.set_trace()
# enc = OneHotEncoder()
# enc.fit(train_new_feature)
# train_new_feature2 = np.array(enc.transform(train_new_feature).toarray())

import lightgbm as lgb
params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': {'binary_logloss'},
    'num_leaves': 64,
    'num_trees': 100,
    'learning_rate': 0.01,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}
# number of leaves,will be used in feature transformation
num_leaf = 64

print('Start training...')
# train
gbm = lgb.train(params=params,
                train_set=X_train,
                valid_sets=Y_train, )


print('Start predicting...')
# y_pred分别落在100棵树上的哪个节点上
y_pred = gbm.predict(X_train, pred_leaf=True)
y_pred_prob = gbm.predict(X_train)

import pdb;pdb.set_trace()
result = []
threshold = 0.5
for pred in y_pred_prob:
    result.append(1 if pred > threshold else 0)
print('result:', result)


print('Writing transformed training data')
transformed_training_matrix = np.zeros([len(y_pred), len(y_pred[1]) * num_leaf],
                                       dtype=np.int64)  # N * num_tress * num_leafs
for i in range(0, len(y_pred)):
    # temp表示在每棵树上预测的值所在节点的序号（0,64,128,...,6436 为100棵树的序号，中间的值为对应树的节点序号）
    temp = np.arange(len(y_pred[0])) * num_leaf + np.array(y_pred[i])
    # 构造one-hot 训练数据集
    transformed_training_matrix[i][temp] += 1

y_pred = gbm.predict(x_test, pred_leaf=True)
print('Writing transformed testing data')
transformed_testing_matrix = np.zeros([len(y_pred), len(y_pred[1]) * num_leaf], dtype=np.int64)
for i in range(0, len(y_pred)):
    temp = np.arange(len(y_pred[0])) * num_leaf + np.array(y_pred[i])
    # 构造one-hot 测试数据集
    transformed_testing_matrix[i][temp] += 1