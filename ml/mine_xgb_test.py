from sklearn.datasets import load_iris, load_boston,load_iris
from xgboost import XGBClassifier,XGBRegressor
import pandas as pd


boston = load_boston()

train = pd.DataFrame(boston['data'])
label = pd.Series(boston["target"], name='label')
full = pd.concat((train, label), axis= 1)
print(full)
model = XGBRegressor(n_estimators=3,max_depth=1,reg_lambda=0,reg_alpha=0)
model.fit(train,label)
xgb_res = model.get_booster().trees_to_dataframe()
print(xgb_res)

# import pdb;pdb.set_trace()
# 回归任务，损失函数为均方误差
full["g"] = full["label"] - 0 # 为什么是-0.5
full["h"] = 1
root_score = full["g"].sum()**2 / full.shape[0] # 根节点506个数据
left_df = full[full.iloc[:,5] < 6.9410]
right_df = full[full.iloc[:,5] >= 6.9410]
left_leaf = left_df["g"].sum() / left_df["h"].sum() # 左子树430个数据
right_leaf = right_df["g"].sum() / right_df["h"].sum() # 右子树76个数据


# left_df = full[full.iloc[:,12] < 9.725]
# right_df = full[full.iloc[:,12] >= 9.725]

left_score = left_df["g"].sum() ** 2 / left_df.shape[0]
right_score = right_df["g"].sum() ** 2 / right_df.shape[0]
print('The Gain for Root is left node score {} + right node score {} - root score {} = {},\nleft leaf: {}, right_leaf: {}' \
      .format(left_score, right_score, root_score, right_score + left_score - root_score, left_leaf, right_leaf))
